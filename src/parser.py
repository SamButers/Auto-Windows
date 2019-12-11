from collections import ChainMap, namedtuple
from typing import Union
from .symbol import Symbol, var

class Node():
	def print(self, indent=0):
		raise NotImplementedError

	def eval(self, env):
		raise NotImplementedError

	def check(self, env):
		raise NotImplementedError

	def getDefaultEnv(self):
		return {
			Symbol('print'): (None, (...,)),
			Symbol('read'): (None, (...,)),
			Symbol('readLine'): (None, ((Symbol.STRING,), (Symbol.FILE, Symbol.STRING))),
			Symbol('open'): (None, ((Symbol.FILE, Symbol.STRING, Symbol.CHAR),)),
			Symbol('close'): (None, ((Symbol.FILE, Symbol.CHAR),)),
			Symbol('moveCursor'): (None, ((Symbol.INT, Symbol.INT), (Symbol.INT, Symbol.INT, Symbol.INT), (Symbol.INT, Symbol.INT, Symbol.INT, Symbol.FLOAT))),
			Symbol('click'): (None, ((Symbol.INT, Symbol.INT), (Symbol.INT, Symbol.INT, Symbol.INT), (Symbol.INT, Symbol.INT, Symbol.INT, Symbol.FLOAT))),
			Symbol('type'): (None, ((Symbol.STRING, Symbol.FLOAT),)),
			Symbol('sleep'): (None, ((Symbol.INT,),)),
			Symbol('sin'): (Symbol.FLOAT, ((Symbol.FLOAT,),)),
			Symbol('cos'): (Symbol.FLOAT, ((Symbol.FLOAT,),)),
			Symbol('tan'): (Symbol.FLOAT, ((Symbol.FLOAT,),)),
			Symbol('acos'): (Symbol.FLOAT, ((Symbol.FLOAT,),)),
			Symbol('asin'): (Symbol.FLOAT, ((Symbol.FLOAT,),)),
			Symbol('atan'): (Symbol.FLOAT, ((Symbol.FLOAT,),)),
			Symbol('sqrt'): (Symbol.FLOAT, ((Symbol.FLOAT, Symbol.FLOAT),)),
			Symbol('ln'): (Symbol.FLOAT, ((Symbol.FLOAT,),)),
			Symbol('log'): (Symbol.FLOAT, ((Symbol.FLOAT,),)),
			Symbol('PI'): Symbol.FLOAT,
			Symbol('MOUSE_X'): Symbol.INT,
			Symbol('MOUSE_Y'): Symbol.INT,
			Symbol('SCREEN_H'): Symbol.INT,
			Symbol('SCREEN_W'): Symbol.INT
		}

	def type_simplify(self, mod_type):
		if(mod_type in self.MODIFIED_INT):
			return Symbol.INT

		if(mod_type == Symbol.LFLOAT):
			return Symbol.FLOAT

		return mod_type

	types = [
		Symbol.INT,
		Symbol.LINT,
		Symbol.UINT,
		Symbol.ULINT,
		Symbol.SINT,
		Symbol.USINT,
		Symbol.FLOAT,
		Symbol.LFLOAT,
		Symbol.CHAR,
		Symbol.STRING,
		Symbol.BOOL,
		Symbol.ARRAY,
		Symbol.FILE
	]

	legal_operations = {
		(Symbol.INT, Symbol.INT): Symbol.INT,
		(Symbol.INT, Symbol.FLOAT): Symbol.FLOAT,
		(Symbol.INT, Symbol.CHAR): Symbol.INT,
		(Symbol.FLOAT, Symbol.FLOAT): Symbol.FLOAT,
		(Symbol.FLOAT, Symbol.CHAR): Symbol.FLOAT,
		(Symbol.STRING, Symbol.STRING): Symbol.STRING
	}

	INT_AUX = (Symbol.INT, Symbol.LINT, Symbol.SINT, Symbol.ULINT, Symbol.USINT, Symbol.CHAR)
	FLOAT_AUX = (Symbol.FLOAT, Symbol.LFLOAT, Symbol.INT, Symbol.LINT, Symbol.SINT, Symbol.ULINT, Symbol.USINT, Symbol.CHAR)
	PRINT_READ_AUX = (Symbol.INT, Symbol.LINT, Symbol.SINT, Symbol.ULINT, Symbol.USINT, Symbol.CHAR, Symbol.FLOAT, Symbol.LFLOAT, Symbol.BOOL, Symbol.STRING)

	MODIFIED_INT = (Symbol.LINT, Symbol.SINT, Symbol.UINT, Symbol.ULINT, Symbol.USINT)

	legal_assignments = {
			Symbol.INT: INT_AUX,
			Symbol.LINT: INT_AUX,
			Symbol.SINT: INT_AUX,
			Symbol.ULINT: INT_AUX,
			Symbol.USINT: INT_AUX,
			Symbol.CHAR: INT_AUX,
			Symbol.BOOL: (Symbol.BOOL,),
			Symbol.FLOAT: FLOAT_AUX,
			Symbol.LFLOAT: FLOAT_AUX,
			Symbol.STRING: (Symbol.STRING,),
			Symbol.FILE: (Symbol.FILE,)
	}

	reserved_words = [
		Symbol('cout'),
		Symbol('cin'),
		Symbol('include'),
		Symbol('long'),
		Symbol('short'),
		Symbol('unsigned'),
		Symbol('signed'),
		Symbol('DEFAULT_FUNCTIONS'),
		Symbol('DefaultFunctions'),
		Symbol('AND'),
		Symbol('and'),
		Symbol('OR'),
		Symbol('or'),
	]

	std_cpp = [
		Symbol('print'),
		Symbol('read')
	]

	std_auto = [
		Symbol('moveCursor'),
		Symbol('click'),
		Symbol('type'),
		Symbol('sleep'),
		Symbol('MOUSE_X'),
		Symbol('MOUSE_Y'),
		Symbol('SCREEN_H'),
		Symbol('SCREEN_W'),
		Symbol('readLine'),
		Symbol('open'),
		Symbol('close')
	]

	comp_op = ['==', '!=', '>', '<', '>=', '<=', Symbol('OR'), Symbol('AND')]
	
	unary_op = [Symbol('NOT')]

class CPP_Code(Node):
	functions: list
	env: ChainMap

	def __init__(self, SExpr):
		self.env = ChainMap(self.getDefaultEnv())
		self.functions = []
		for function in SExpr:
			self.functions.append(CPP_Function(function, self.env))

		self.check(self.env)

	def check(self, env):
		main = False

		for function in self.functions:
			if str(function.name) == 'main':
				main = True
				break

		if(not main):
			raise Exception('Main function not found.')

	def print(self, indent = 0):
		print("""#include <windows.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

#define True true
#define False false
#define AND &&
#define OR ||
#define NOT !

typedef long int Lint;
typedef short int Sint;
typedef unsigned long int ULint;
typedef unsigned short int USint;
typedef double Lfloat;

using namespace std;

class DefaultFunctions {
	private:
		int c, x;
		float y;
		POINT mouseCoords;
		INPUT input;
	
	public:
		int getScreenW() {
			return GetSystemMetrics(SM_CXSCREEN);
		}
		
		int getScreenH() {
			return GetSystemMetrics(SM_CYSCREEN);
		}
		
		int getCursorX() {
			GetCursorPos(&mouseCoords);
			return (int) mouseCoords.x;
		}
		
		int getCursorY() {
			GetCursorPos(&mouseCoords);
			return (int) mouseCoords.y;
		}
		
		void sleep(int ms) {
			Sleep(ms);
		}
		
		void moveCursor(int x, int y) {
				SetCursorPos(x, y);
		}
		
		void moveCursor(int x, int y, int mode) {
			GetCursorPos(&mouseCoords);
			this->x = mouseCoords.x;
			this->y = mouseCoords.y;
			x += this->x;
			y += this->y;
			
			SetCursorPos(x, y);
		}
		
		void moveCursor(int x, int y, int mode, float speed) {
			if(speed <= 0)
				SetCursorPos(x, y);
						
			if(speed > 1)
				speed = 1;
			
			speed *= 20;
			
			GetCursorPos(&mouseCoords);
			this->x = mouseCoords.x;
			this->y = mouseCoords.y;
			
			if(mode) {
				x += this->x;
				y += this->y;
			}
			
			int xOffset = x - this->x;
			int absOffset = abs(xOffset);
			
			float yIncrement = (y - this->y)/absOffset;
			int xIncrement = (xOffset > 0) ? 1 : -1;
			
			for(c = 0; c < absOffset - 1; c++, this->x += xIncrement, this->y += yIncrement) {
				SetCursorPos(this->x, (int) this->y);
				Sleep(speed);
			}
			
			SetCursorPos(x, y);
		}
		
		void click(int x, int y, int mode = 0, float speed = 0) {
			moveCursor(x, y, mode, speed);
			
			input.type = INPUT_MOUSE;
			input.mi.dx = 0;
			input.mi.dy = 0;
			input.mi.time = 0;
			input.mi.dwExtraInfo = 0;
			input.mi.mouseData = 0;
			
			input.mi.dwFlags = MOUSEEVENTF_LEFTDOWN;
			SendInput(1, &input, sizeof(INPUT));
			
			input.mi.dwFlags = MOUSEEVENTF_LEFTUP;
			SendInput(1, &input, sizeof(INPUT));
			Sleep(speed);
		}
		
		void type(string text, float speed) {
			input.type = INPUT_KEYBOARD;
			input.ki.time = 0;
			input.ki.dwExtraInfo = 0;
			
			if(speed > 1)
				speed = 1;
			
			else if(speed < 0)
				speed = 0;
			
			speed *= 20;
			
			if(text == "{ENTER}") {
				input.ki.dwFlags = 0;
				input.ki.wScan = 0;
				input.ki.wVk = VK_RETURN;
				SendInput(1, &input, sizeof(INPUT));
				
				input.ki.dwFlags = KEYEVENTF_KEYUP;
				SendInput(1, &input, sizeof(INPUT));
				Sleep(speed);
			}
			
			else if(text == "{TAB}") {
				input.ki.dwFlags = 0;
				input.ki.wScan = 0;
				input.ki.wVk = VK_TAB;
				SendInput(1, &input, sizeof(INPUT));
				
				input.ki.dwFlags = KEYEVENTF_KEYUP;
				SendInput(1, &input, sizeof(INPUT));
				Sleep(speed);
			}
			
			else if(text == "{BACKSPACE}") {
				input.ki.dwFlags = 0;
				input.ki.wScan = 0;
				input.ki.wVk = VK_BACK;
				SendInput(1, &input, sizeof(INPUT));
				
				input.ki.dwFlags = KEYEVENTF_KEYUP;
				SendInput(1, &input, sizeof(INPUT));
				Sleep(speed);
			}

			else {
				for(auto chr : text) {
					input.ki.dwFlags = KEYEVENTF_UNICODE;
					input.ki.wScan = chr;
					input.ki.wVk = 0;
					SendInput(1, &input, sizeof(INPUT));
					
					Sleep(speed);
				}
			}
		}
		
		void readLine(string &a) {
			do {
				getline(cin, a);
			} while(!a.length());
		}
};

DefaultFunctions DEFAULT_FUNCTIONS;

class File {
	private:
		bool inputOpen, outputOpen;
	
	public:
		ifstream input;
		ofstream output;
		
		File() {
			this->inputOpen = false;
			this->outputOpen = false;
		}
		
		~File() {
			if(this->inputOpen)
				this->input.close();
			
			if(this->outputOpen)
				this->output.close();
		}
	
		void open(string path, char mode) {
			if(mode == 'r') {
				if(inputOpen)
					this->input.close();

				this->input.open(path);
				if(this->input.is_open())
					this->inputOpen = true;
			}
			
			if(mode == 'w') {
				if(outputOpen)
					this->output.close();
				
				this->output.open(path);
				if(this->output.is_open())
					this->outputOpen = true;
			}
		}
		
		void close(char mode) {
			if(mode == 'r') {
				if(inputOpen) {
					this->input.close();
					this->inputOpen = false;
				}
			}
			
			if(mode == 'w') {
				if(outputOpen) {
					this->output.close();
					this->outputOpen = false;
				}
			}
		}
		
		void readLine(string &a) {
			getline(this->input, a);
		}
		
		bool end() {
			return this->input.eof();
		}
};
""")

		for function in self.functions:
			function.print(indent)

class CPP_Function(Node):
	function_type: Symbol
	name: Symbol
	arguments: list
	scope: list
	env: ChainMap

	def __init__(self, SExpr, env):
		self.function_type, self.name, self.arguments, self.scope = SExpr
		self.env = ChainMap({}, env)

		for c in range(len(self.arguments)):
			self.arguments[c] = CPP_Declaration(self.arguments[c], self.env)
		self.check(env)
		self.scope = CPP_Scope(self.scope, self.env, self.function_type)
		self.scope.check(self.name)

	def check(self, env):
		if(self.function_type not in self.types):
			raise Exception("Function '{}' is of type '{}' which is not a valid type.".format(self.name, self.function_type))

		if(self.name in env):
			raise Exception("Name '{}' is already in use.".format(self.name))

		if(self.name in self.reserved_words):
			raise Exception("Name '{}' is a reserved word.".format(self.name))

		args_tuple = tuple(map(lambda x : x.var_type, self.arguments))
		args_tuple = (args_tuple,)
		env[self.name] = (self.function_type, args_tuple)

	def print(self, indent):
		print('\t' * indent + "{} {}(".format(self.function_type, self.name), end='')
		for argument in self.arguments[:-1]:
			argument.print(0)
			print(", ", end='')

		if(len(self.arguments)):
			self.arguments[-1].print(0)
		print(") {")
		self.scope.print(indent + 1)
		print('\t' * indent + "}")


class CPP_Declaration(Node):
	var_type: Symbol
	name: Symbol
	equal: str
	expression: Union[list, float, int, bool, str, Symbol]

	def __init__(self, SExpr, env):
		_, *SExpr = SExpr

		if(len(SExpr) == 2):
			self.var_type, self.name = SExpr
			self.equal = None
			self.expression = None

		else:
			self.var_type, self.name, self.equal, self.expression = SExpr
			self.expression = CPP_Expression(self.expression, env)

		self.check(env)
		env.maps[0][self.name] = self.var_type

	def check(self, env):
		if(self.equal):
			if(self.var_type not in self.types):
				raise Exception("Variable '{}' is of type '{}' which is not a valid type.".format(self.name, self.var_type))

			if(self.name in env.maps[0]):
				raise Exception("Name '{}' is already in use.".format(self.name))

			if(self.equal != '='):
				raise Exception("'{}' is not a valid assignment operator.".format(self.equal))

			if(self.expression.expression_type not in self.legal_assignments[self.var_type]):
				raise Exception("Invalid expression for the assignment of '{}'.".format(self.name))

		else:
			if(self.var_type not in self.types):
				raise Exception("Variable '{}' is of type '{}' which is not a valid type.".format(self.name, self.var_type))

			if(self.name in env.maps[0]):
				raise Exception("Name '{}' is already in use.".format(self.name))

	def print(self, indent, p_end = ''):
		if(self.equal):
			print('\t' * indent + "{} {} = ".format(self.var_type, self.name), end=p_end)
			self.expression.print(0)

		else:
			print('\t' * indent + "{} {}".format(self.var_type, self.name), end=p_end)

class CPP_Expression(Node):
	expression_type: Symbol
	value: Union[int, float, str, Symbol]
	arguments: tuple
	operator: str

	def __init__(self, SExpr, env):
		self.arguments = None
		self.operator = None

		if(isinstance(SExpr, bool)):
			self.expression_type = Symbol.BOOL
			self.value = SExpr

		elif(isinstance(SExpr, int)):
			self.expression_type = Symbol.INT
			self.value = SExpr

		elif(isinstance(SExpr, float)):
			self.expression_type = Symbol.FLOAT
			self.value = SExpr

		elif(isinstance(SExpr, str)):
			if(SExpr[0] == "'"):
				if(SExpr[1] == '\\'):
					if(len(SExpr) != 4):
						raise Exception("{} is not a valid character.".format(SExpr))
				else:
					if(len(SExpr) != 3):
						raise Exception("{} is not a valid character.".format(SExpr))
				
				self.expression_type = Symbol.CHAR
			
			else:
				self.expression_type = Symbol.STRING
				
			self.value = SExpr

		elif(isinstance(SExpr, Symbol)):
			if(SExpr not in env):
				raise Exception("Variable '{}' does not exist.".format(SExpr))
			self.expression_type = env[SExpr]
			self.value = SExpr

		elif(SExpr[0] in env):
			name, args = SExpr
			_, *args = args
			args_type = []
			for c in range(len(args)):
				args[c] = CPP_Expression(args[c], env)
				args_type.append(args[c].expression_type)

			if(env[name][1] == (...,)):
				if(not len(args_type)):
					raise Exception("No arguments given to print or read function.")
					
				if(args_type[0] == Symbol.FILE):
					args_type = args_type[1:]
					if(not len(args_type)):
						raise Exception("No arguments given to print or read function for a File.")
					
				for arg_type in args_type:
					if(arg_type not in self.PRINT_READ_AUX):
						raise Exception("Arguments '{}' are not printable or readable.".format(args))
							
			else:
				isAccepted = False
				for arg in env[name][1]:
					if(len(args_type) != len(arg)):
						continue
					isAccepted = True
					for c in range(len(arg)):
						if(args_type[c] not in self.legal_assignments[arg[c]]):
									isAccepted = False
									break

				if(not isAccepted):
					if(env[name][1] == (...,)):
						for arg_type in args_type:
							if(arg_type not in self.PRINT_READ_AUX):
								raise Exception("Arguments '{}' are not printable or readable.".format(args))
					else:
						raise Exception("Arguments given to '{}' do not match.".format(name))

			self.expression_type = env[name][0]
			self.arguments = args
			self.value = name

		else:
			operator, operantOne, operantTwo = SExpr
			self.value = ((CPP_Expression(operantOne, env), CPP_Expression(operantTwo, env)))
			self.operator = operator

			type_one = self.type_simplify(self.value[0].expression_type)
			type_two = self.type_simplify(self.value[1].expression_type)
			if((type_one, type_two) in self.legal_operations):
				self.expression_type = self.legal_operations[(type_one, type_two)]

			elif((type_two, type_one) in self.legal_operations):
				self.expression_type = self.legal_operations[(type_two, type_one)]

			else:
				raise Exception("Illegal operation in code.")

	def print(self, indent, p_end = ''):
		print("\t" * indent, end='')
		if(self.value in self.std_cpp):
			arguments = self.arguments
			
			if(self.value == Symbol('print')):
				if(arguments[0].expression_type == Symbol.FILE):
					arguments[0].print(0, '.output')
					arguments = arguments[1:]
					
				else:
					print("cout", end='')
					
				for argument in arguments:
					print(" << ", end='')
					argument.print(0, '')
			else:
				if(arguments[0].expression_type == Symbol.FILE):
					arguments[0].print(0, '.input')
					arguments = arguments[1:]
				else:
					print("cin", end='')
					
				for argument in arguments:
					print(" >> ", end='')
					argument.print(0, '')

		elif(self.value in self.std_auto):
			if(self.value == Symbol('MOUSE_X')):
				print("DEFAULT_FUNCTIONS.getCursorX()", end=p_end)

			elif(self.value == Symbol('MOUSE_Y')):
				print("DEFAULT_FUNCTIONS.getCursorY()", end=p_end)

			elif(self.value == Symbol('SCREEN_W')):
				print("DEFAULT_FUNCTIONS.getScreenW()", end=p_end)

			elif(self.value == Symbol('SCREEN_H')):
				print("DEFAULT_FUNCTIONS.getScreenH()", end=p_end)
				
			elif(self.value in (Symbol('open'), Symbol('close'))):
				arguments = self.arguments
				
				arguments[0].print(0, '')
				print(".{}(".format(self.value), end='')
				
				arguments = arguments[1:]
				for argument in arguments[:-1]:
					argument.print(0, '')
					print(", ", end='')
				arguments[-1].print(0, '')
				print(")", end=p_end)
				
			elif(self.value == Symbol('readLine') and self.arguments[0].expression_type == Symbol.FILE):
				arguments = self.arguments
				
				arguments[0].print(0, '')
				print(".{}(".format(self.value), end='')
				
				arguments = arguments[1:]
				for argument in arguments[:-1]:
					argument.print(0, '')
					print(", ", end='')
				arguments[-1].print(0, '')
				print(")", end=p_end)

			else:
				print("DEFAULT_FUNCTIONS.{}(".format(self.value), end='')
				for argument in self.arguments[:-1]:
					argument.print(0, '')
					print(", ", end='')
				self.arguments[-1].print(0, '')
				print(")", end=p_end)

		elif(isinstance(self.arguments, list)):
			print("{}(".format(self.value), end='')
			for argument in self.arguments:
				argument.print(0, '')
			print(")", end=p_end)

		elif self.operator:
			self.value[0].print(0, ' ')
			print(self.operator, end=' (')
			self.value[1].print(0)
			print(")", end='')

		else:
			print(self.value, end=p_end)
			
class CPP_Scope(Node):
	statements: list
	scope_type: Symbol

	def __init__(self, SExpr, env, scope_type):
		self.statements = []
		self.scope_type = scope_type
		for statement in SExpr:
			self.statements.append(CPP_Statement(statement, env, scope_type))

	def check(self, name):
		noReturn = True
		for statement in self.statements:
			if(isinstance(statement, CPP_Return)):
				noReturn = False
				break
		if(noReturn):
			print("// Warning!: Function '{}' has no return statement.".format(name))

	def print(self, indent):
		for statement in self.statements:
			statement.print(indent)

class CPP_Statement(Node):
	semicolon: bool
	statement_type: str
	statement: Node

	def __init__(self, SExpr, env, scope_type):
		statement_type = SExpr[0]

		if(statement_type == 'declaration'):
			self.statement_type = statement_type
			self.semicolon = True
			self.statement = CPP_Declaration(SExpr, env)

		elif(statement_type == 'assignment'):
			self.statement_type = statement_type
			self.semicolon = True
			self.statement = CPP_Assignment(SExpr, env)

		elif(statement_type == 'return'):
			self.statement_type = statement_type
			self.semicolon = True
			self.statement = CPP_Return(SExpr, env, scope_type)

		elif(statement_type == 'for'):
			self.statement_type = statement_type
			self.semicolon = False
			self.statement = CPP_For(SExpr, env, scope_type)

		elif(statement_type == 'while'):
			self.statement_type = statement_type
			self.semicolon = False
			self.statement = CPP_While(SExpr, env, scope_type)

		elif(statement_type == 'count'):
			self.statement_type = statement_type
			self.semicolon = False
			self.statement = CPP_Count(SExpr, env, scope_type)

		elif(statement_type == 'if'):
			self.statement_type = statement_type
			self.semicolon = False
			self.statement = CPP_If(SExpr, env, scope_type)
			
		# Expression
		else:
			self.statement_type = 'expression'
			self.semicolon = True
			self.statement = CPP_Expression(SExpr, env)

	def check(self, env):
		if(self.statement_type not in ('declaration', 'assignment', 'return', 'for', 'while', 'if', 'else', 'expression')):
			raise Exception("Invalid statement type '{}'".format(self.statement_type))

	def print(self, indent, p_end='\n'):
		self.statement.print(indent)

		if(self.semicolon):
			print(";", end=p_end)

		else:
			print('', end=p_end)

class CPP_Assignment(Node):
	name: Symbol
	operator: str
	expression: Union[list, float, int, bool, str, Symbol, None]
	var_type: Symbol

	def __init__(self, SExpr, env):
		_, *SExpr = SExpr

		if(len(SExpr) == 2):
			self.operator, self.name = SExpr
			self.expression = None

		else:
			self.operator, self.name, self.expression = SExpr
			self.expression = CPP_Expression(self.expression, env)
		
		self.var_type = env[self.name]
		self.check(env)

	def check(self, env):
		if(self.name not in env):
			raise Exception("Variable '{}' does not exist.".format(self.name))

		if(self.expression):
			if(self.expression.expression_type not in self.legal_assignments[self.var_type]):
				raise Exception("Invalid expression for the assignment of '{}'.".format(self.name))

	def print(self, indent, p_end = ''):
		print('\t' * indent, end='')

		if(self.operator == '='):
			print("{} = ".format(self.name), end='')
			self.expression.print(0)

		elif(self.operator[0] == 'r'):
			print("{}{}".format(self.name, self.operator[1:]), end=p_end)

		else:
			print("{}{}".format(self.operator[1:], self.name), end=p_end)

class CPP_Return(Node):
	expression: Node
	scope_type: Symbol
	
	def __init__(self, SExpr, env, scope_type):
		_, self.expression = SExpr
		self.expression = CPP_Expression(self.expression, env)
		self.scope_type = scope_type

		self.check(env)

	def check(self, env):
		if(self.expression.expression_type not in self.legal_assignments[self.scope_type]):
			raise Exception("Function of type '{}' returns a '{}' value.".format(self.current_function_type, self.expression.expression_type))

	def print(self, indent, p_end=''):
		print('\t' * indent + "return ", end=p_end)
		self.expression.print(0, p_end)

class CPP_For(Node):
	env: ChainMap
	initialization: Union[Node, None]
	condition: Node
	iteration: Union[Node, None]
	scope: Node
	scope_type: Symbol

	def __init__(self, SExpr, env, scope_type):
		self.env = ChainMap({}, env)
		self.scope_type = scope_type

		_, self.initialization, self.condition, self.iteration, self.scope = SExpr
		if(self.initialization):
			self.initialization = CPP_Statement(self.initialization, self.env, self.scope_type)
			self.initialization.semicolon = False
		self.condition = CPP_Condition(self.condition, self.env)
		if(self.iteration):
			self.iteration = CPP_Statement(self.iteration, self.env, self.scope_type)
			self.iteration.semicolon = False
		self.scope = CPP_Scope(self.scope, self.env, self.scope_type)

		self.check(self.env)

	def check(self, env):
		if(self.initialization):
			if(self.initialization.statement_type not in ('declaration', 'assignment', 'expression')):
				raise Exception("For loop initialization statement is not a valid statement.")

		if(self.iteration):
			if(self.iteration.statement_type not in ('declaration', 'assignment', 'expression')):
				raise Exception("For loop iteration statement is not a valid statement.")

	def print(self, indent):
		print('\t' * indent, end='')

		print("for(", end='')
		if(self.initialization):
			self.initialization.print(0, '')
		print(";", end=' ')

		self.condition.print(0)

		print(";", end='')
		if(self.iteration):
			print("", end=' ')
			self.iteration.print(0, '')

		print(") {")
		self.scope.print(indent + 1)
		print('\t' * indent + "}")

class CPP_Condition(Node):
	operator: Symbol
	expression_one: Union[Symbol, float, int, bool, str, Node]
	expression_two: Union[Symbol, float, int, bool, str, Node]

	def __init__(self, SExpr, env):
		if(isinstance(SExpr, (Symbol, float, int, bool, str))):
			self.expression_one = CPP_Expression(SExpr, env)
			self.expression_two = None
			self.operator = None
			
		elif(SExpr[0] in self.unary_op):
			self.operator, self.expression_one = SExpr
			
			self.expression_one = CPP_Condition(self.expression_one, env)
			self.expression_two = None

		elif(SExpr[0] not in self.comp_op):
			self.expression_one = CPP_Expression(SExpr, env)
			self.expression_two = None
			self.operator = None

		else:
			self.operator, self.expression_one, self.expression_two = SExpr

			self.expression_one = CPP_Condition(self.expression_one, env)
			self.expression_two = CPP_Condition(self.expression_two, env)

		self.check(env)

	def check(self, env):
		if(isinstance(self.expression_one, Symbol)):
			if(self.expression_one not in env):
				raise Exception("Variable '{}' does not exist.".format(self.expression_one))

		if(self.expression_two):
			if(isinstance(self.expression_two, Symbol)):
				if(self.expression_two not in env):
					raise Exception("Variable '{}' does not exist.".format(self.expression_two))

	def print(self, indent, p_end=''):
		print('\t' * indent, end='')
		
		if(self.operator == Symbol('NOT')):
			print("({}".format(Symbol('NOT')), end=' ')
			if(isinstance(self.expression_one, Node)):
				self.expression_one.print(0)
			else:
				print(self.expression_one, end='')
			print(")", end='')
			
		else:
			if(isinstance(self.expression_one, Node)):
				self.expression_one.print(0)
			else:
				print(self.expression_one, end='')
			
			if(self.operator):
				print(" {} ".format(self.operator), end='')

			if(self.expression_two):
				print("(", end='')
				if(isinstance(self.expression_two, Node)):
					self.expression_two.print(0)
				else:
					print("{}".format(self.expression_two), end='')
				print(")", end='')

class CPP_While(Node):
	env: ChainMap
	condition: Node
	scope: Node
	scope_type: Symbol

	def __init__(self, SExpr, env, scope_type):
		self.env = ChainMap({}, env)
		self.scope_type = scope_type

		_, self.condition, self.scope = SExpr
		self.condition = CPP_Condition(self.condition, self.env)
		self.scope = CPP_Scope(self.scope, self.env, self.scope_type)

	def print(self, indent):
		print('\t' * indent, end='')

		print("while(", end='')
		self.condition.print(0)
		print(") {")
		self.scope.print(indent + 1)
		print('\t' * indent + "}")

class CPP_Count(Node):
	env: ChainMap
	counter: Union[Symbol, Node]
	beginning: Union[int, Node]
	ending: Union[int, Node]
	for_representation: Node
	scope: Node
	counter_name: Symbol

	def __init__(self, SExpr, env, scope_type):
		_, self.counter, self.beginning, self.ending, self.scope = SExpr
		if(not self.counter):
			self.counter_name = Symbol('COUNTER')
			self.counter = ['declaration', Symbol.INT, self.counter_name, '=', self.beginning]
		elif(isinstance(self.counter, Symbol)):
			self.counter_name = self.counter
			self.counter = ['assignment', '=', self.counter_name, self.beginning]
		else:
			try:
				_, counter_type, self.counter_name = self.counter
			except:
				raise Exception("Invalid counter in count loop.".format(self.counter_name))
			self.counter = ['declaration', counter_type, self.counter_name, '=', self.beginning]

		self.for_representation = CPP_For(['for', self.counter, ['<=', self.counter_name, self.ending], ['assignment', 'r++', self.counter_name], self.scope], env, scope_type)
		self.env = self.for_representation.env
		self.check(self.env)

	def check(self, env):
		if(env[self.counter_name] not in self.legal_assignments[Symbol.INT]):
			raise Exception("Counter '{}' is not a valid integer counter.".format(self.counter_name))

	def print(self, indent):
		self.for_representation.print(indent)

class CPP_If(Node):
	env: ChainMap
	condition: Node
	scope: Node
	scope_type: Symbol
	if_else: Union[Node, None]

	def __init__(self, SExpr, env, scope_type):
		self.env = ChainMap({}, env)
		self.scope_type = scope_type
		try:
			_, self.condition, self.scope, self.if_else = SExpr
			self.if_else = CPP_Else(self.if_else, env, self.scope_type)
		except Exception as e:
			_, self.condition, self.scope = SExpr
			self.if_else = None

		self.condition = CPP_Condition(self.condition, self.env)
		self.scope = CPP_Scope(self.scope, self.env, self.scope_type)

	def print(self, indent, p_end=''):
		print('\t' * indent, end='')

		print("if(", end='')
		self.condition.print(0)
		print(") {")
		self.scope.print(indent + 1)
		print('\t' * indent + "}")

		if(self.if_else):
			print("", end='\n')
			self.if_else.print(indent, p_end)

class CPP_Else(Node):
	env: ChainMap
	scope: Node
	scope_type: Symbol
	else_if: Union[Node, None]

	def __init__(self, SExpr, env, scope_type):
		self.env = ChainMap({}, env)
		self.scope_type = scope_type

		if(SExpr[1] == 'if'):
			SExpr.pop(0)
			self.else_if = CPP_If(SExpr, env, scope_type)
		else:
			self.else_if = None
			self.scope = CPP_Scope(SExpr[1], self.env, self.scope_type)

	def print(self, indent, p_end=''):
		print('\t' * indent, end='')
		print("else ", end=p_end)

		if(self.else_if):
			self.else_if.print(indent)

		else:
			print("{")
			self.scope.print(indent + 1)
			print('\t' * indent, end='')
			print("}", end=p_end)