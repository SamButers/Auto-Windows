from src import *
import argparse
import io
from contextlib import redirect_stdout

def main():
	args_parser = argparse.ArgumentParser(description='Auto Windows Compiler')
	args_parser.add_argument("-i", "--input", required=True, type=str, help="input file containing the Auto Windows code")
	args_parser.add_argument("-o", "--output", default="output.cpp", type=str, help="output file containing the C++ code")
	args_parser.add_argument("-t", "--terminal", action="store_true", help="print to terminal flag")
	args_parser.add_argument("-d", "--debug", action="store_true", help="print SExpr flag")
	
	args = args_parser.parse_args()
	
	with open(args.input, 'r') as aw_file:
		awc_code = aw_file.read()
	
	awc_code = grammar.parse(awc_code)
	awc_code = SExprTransformer().transform(awc_code)
	
	if(args.debug):
		print(awc_code)
	
	f = io.StringIO()
	with redirect_stdout(f):
		cpp_output = CPP_Code(awc_code)
		cpp_output.print()
		
	output = f.getvalue()
	
	if(args.terminal):
		print(output)
		
	else:
		cpp_file = open(args.output, "w")
		cpp_file.write(output)
		cpp_file.close()
	
	
if __name__ == '__main__':
    main()