from lark import Lark, InlineTransformer, Tree, Token
from .symbol import Symbol, var

class SExprTransformer(InlineTransformer):
	INTEGER = int
	FLOAT = float
	VAR_NAME = Symbol
	COMP_OP = ('>', '<', '>=', '<=', '!=', "==")
	
	def start(self, *args):
		return list(args)

	def function(self, type, name, *args):
		args = list(args)
		scope = args.pop()
		return [Symbol(type), Symbol(str(name)), args, scope]

	def argument(self, type, name):
		return ['declaration', Symbol(type), str(name)]

	def scope(self, *args):
		return list(args)

	def assignment(self, var_name, op, expression):
		return ['assignment', str(op), Symbol(str(var_name)), expression]

	def post_increment(self, var_name, op):
		return['assignment', 'r' + str(op), Symbol(str(var_name))]

	def pre_increment(self, op, var_name):
		return['assignment', 'l' + str(op), Symbol(str(var_name))]

	def declaration(self, type, name, *args):
		if(len(args)):
			return ['declaration', Symbol(type), Symbol(name), str(args[0]), args[1]]
		
		return ['declaration', Symbol(type), Symbol(name)]

	def argument(self, type, name):
		return ['declaration', Symbol(type), Symbol(name)]

	def binary_operation(self, left, op, right):
		op = str(op)

		if(isinstance(left, Token)):
			left = str(left)

		if(isinstance(right, Token)):
			right = str(right)

		return [op, left, right]

	def atom(self, atom):
		try:
			return int(atom)
		except:
			try:
				return float(atom)
			except:
				if(isinstance(atom, Token)):
					if(atom.type == 'VAR_NAME'):
						return Symbol(str(atom))
						
					atom = str(atom)

					if(atom == 'TRUE'):
						return True
					
					if(atom == 'FALSE'):
						return False

					else:
						return atom

				return atom

	def call(self, function, *args):
		args = list(args)
		args.insert(0, 'call_args')
		return [Symbol(function), args]

	def count(self, *args):
		args = list(args)
		scope = args.pop()

		if(len(args) == 3):
			if(isinstance(args[0], Token)):
				args[0] = Symbol(str(args[0]))

			return ['count', args[0], args[1], args[2], scope]

		return ['count', None, args[0], args[1], scope]

	def while_loop(self, conditions, scope):
		return ['while', conditions, scope]

	def minimal_for(self, conditions, scope):
		return ['for', None, conditions, None, scope]

	def left_for(self, initialization, conditions, scope):
		return ['for', initialization, conditions, None, scope]

	def right_for(self, conditions, iteration, scope):
		return ['for', None, conditions, iteration, scope]

	def for_loop(self, initialization, conditions, iteration, scope):
		return ['for', initialization, conditions, iteration, scope]

	def if_conditional(self, conditions, *args):
		if(len(args) == 2):
			return ['if', conditions, args[0], args[1]]

		return ['if', conditions, args[0]]

	def else_conditional(self, next):
		if(next[0] == 'if'):
			next.insert(0, 'else')
			return next

		return ['else', next]
		
	def or_condition(self, condition, *conditions):
		for cond in conditions:
			condition = [Symbol('OR'), condition, cond]
			
		return condition
		
	def and_condition(self, condition, *conditions):
		for cond in conditions:
			condition = [Symbol('AND'), condition, cond]
			
		return condition
		
	def not_condition(self, *args):
		if(len(args) == 2):
			return [Symbol('NOT'), args[1]]
			
		return args[0]
		
	def condition(self, expressionOne, op, expressionTwo):
		return [str(op), expressionOne, expressionTwo]
		
	def composite_condition(self, expressionOne, opOne, expressionTwo, opTwo, expressionThree):
		return [Symbol('AND'), [Symbol(str(opOne)), expressionOne, expressionTwo], [Symbol(str(opTwo)), expressionTwo, expressionThree]]

	def return_expression(self, *expression):
		if(len(expression)):
			return ['return', expression[0]]
		return ['return', None]