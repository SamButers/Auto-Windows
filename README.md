<h1>Auto Windows Documentation</h1>
<div class="line"></div>

<p align="justify">&emsp;&emsp;Auto Windows is a small and on-going project of a language inspired by the C, C++ and Autohotkey languages. It has built-in functions to control inputs on your machine, such as keyboard and mouse.
<br>
&emsp;&emsp;The Auto Windows Compiler, AWC for short, was made using the Python language, turning Auto Windows code into C++ code. All codes produced by this language use the Win32 API, being, by consequence, mainly supported on the Windows platform.</p>

## Native types	
<p align="justify">&emsp;&emsp;Just like any other language, Auto Windows has a set of types that comes with the language. The native types are as follow:</p>

- Integer (int): Represents a signed integer data. In 32 bits systems, it has the size of 2 bytes, ranging from -32,768 to 32,767. In 64 bits systems, it has the size of 4 bytes, ranging from -2,147,483,648 to 2,147,483,647.<br>Its size and range can be modified by the following modifiers:
	- Long Integer (Lint);
	- Unsigned Long Integer (ULint);
	- Short Integer (Sint);
	- Unsigned Short Integer (USint).

- Float (float): Represents a signed floating-point data. It has the size of 4 bytes, ranging from 1.2E-38 to 3.4E+38 with 6 decimal places.<br>Its size and range can be modified by the following modifiers:
	- Long Float (Lfloat).

- Character (char): Represents a character. It has the size of 1 byte, ranging from -128 to 127.

- Boolean (bool): Represents a value of TRUE or FALSE.

- File (File): Represents a file. It is used both for reading and writing operations.

## Native functions
<p align="justify">&emsp;&emsp;Auto Windows has a set of built-in functions, which are as follow:</p>

- read(var1, var2, ...): Reads from stdin and writes value to the variables in order.
- print(value1, value2, ...): Prints each value to stdout. Allowed values are integers, floats, characters, strings and boolean. No line-break character is added at the end.
- moveCursor(x, y, mode, speed): Moves the mouse to the specified x and y position. Both mode and speed arguments are optional. If mode is given and is equal to 1, the cursor is moved relative to its current position, otherwise it moves the cursor relative to the screen. The speed is a value ranging from 0 to 1, the former moving the cursor instantly and the latter moving the cursor at the slowest defined speed.
- click(x, y, mode, speed): Clicks at the specified x and y position. The arguments work the same way as in the moveCursor function.
- type(string, speed): Sends the given string input as keyboard input. The input is sent instantly when speed is equal to 0 or lower.
- sleep(ms): Sleeps the program for the time given in milliseconds.
- open(file, path, mode): Opens the file identified by the path string, for the operation specified at mode, and associates it with the File variable given. For reading operations, mode should be equal to 'r', and for writing operations, mode should be equal to 'w'.
- close(file, mode): Dissociates the File variable given to a previous association with a file for the specified mode. The mode works the same way as the open function.
- sin(x): Returns sin of x.
- cos(x): Returns cos of x.
- tan(x): Returns tan of x.
- acos(x): Returns arc cos of x.
- asin(x): Returns arc sin of x.
- atan(x): Returns arc tan of x.
- sqrt(x): Returns square root of x.
- ln(x): Returns natural logarithm of x.
- log(x): Returns common logarithm of x.

## Global Variables
<p align="justify">&emsp;&emsp;Auto Windows also contains the following global variables:</p>

- MOUSE_X: Current cursor X position.
- MOUSE_Y: Current cursor Y position.
- SCREEN_W: Current screen width.
- SCREEN_H: Current screen height.

## Loop
<p align="justify">&emsp;&emsp;Auto Windows contains three loop structures, those being:</p>
<ul>
	<li>count loop: The count loop follows the following syntax:<br>
	<p align="center" style="font-family: Source Code Pro;">count VAR_NAME from VALUE1 to VALUE2 {<br>
	[...]<br>
	}</p><br>
	The count loop iterates from VALUE1 to VALUE2, including both ends, and stores the value of each iteration in the variable or declaration specified at VAR_NAME, which is optional.</li>
	<li>while loop: The while loop follows the following syntax:<br>
	<p align="center" style="font-family: Source Code Pro;">while CONDITION {<br>
	[...]<br>
	}</p><br>
	The while loop iterates as long as the CONDITION is TRUE. Parentheses around the CONDITION are optional.</li>
	<li>for loop: The for loop follows the following syntax:<br>
	<p align="center" style="font-family: Source Code Pro;">for STARTING_STATEMENT; CONDITION; FINAL_STATEMENT {<br>
	[...]<br>
	}</p><br>
	The for loop iterates as long as the CONDITION is TRUE. At the start of the loop, the for loop executes the statement at STARTING_STATEMENT once. At the end of each iteration, the for loop executes the statement at FINAL_STATEMENT. Statements do not include other loops or conditional structures. Parenthesis are optional.</li>
</ul>

## Conditionals
<p align="justify">&emsp;&emsp;The following conditionals are present in Auto Windows:</p>
<ul>
	<li>if ... : The if condition follows the following syntax:<br>
	<p align="center" style="font-family: Source Code Pro;">if CONDITION {<br>
	[...]<br>
	}<br>
	<br>
	else {<br>
	[...]<br>
	}<br>
	</p><br>
	The count loop iterates from VALUE1 to VALUE2, including both ends, and stores the value of each iteration in the variable or declaration specified at VAR_NAME, which is optional.</li>
</ul>