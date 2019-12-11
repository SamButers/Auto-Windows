<h1>Auto Windows Documentation</h1>
<div class="line"></div>

<p align="justify">&emsp;&emsp;Auto Windows is a small and on-going project of a language inspired by the C, C++ and Autohotkey languages.
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