# Pending Implementations
<div class="line"></div>
<p align="justify">&emsp;&emsp;Some functionalities for Auto Windows were planned but are yet to be implemented for various reasons. In this page, information about those functionalities can be found.</p>

## Arrays
<p align="justify">&emsp;&emsp;Auto Windows is planned to have three types of arrays, those being as follow:</p>

<ul>
	<li>Auto-resizing typed array: An auto-resizing typed array is an array that resizes itself as elements are inserted and can be done using any of the types available in Auto Windows with the following syntax:<br>
	<p align="center" style="font-family: Source Code Pro;">{TYPE} {VAR_NAME}[];<br>
	Lint myLongIntArray[];</p></li>
	<li>Fixed size typed array: A fixed typed array is an array with a fixed size, defined during declaration, and can be done using any of the types available in Auto Windows with the following syntax:<br>
	<p align="center" style="font-family: Source Code Pro;">{TYPE} {VAR_NAME}[{SIZE}];<br>
	Lfloat mySmallLongFloatArray[5];</p></li>
	<li>Auto-resizing heterogeneous array: An auto-resizing heterogeneous array is an array that resizes itself as element are inserted and accept any variable available in Auto Windows. Different from the other arrays, this array is declared using a special type called Array.</li>
</ul>

<p align="justify">&emsp;&emsp;All those functionalities are planned to be implemented, with exception of the auto-resizing heterogeneous array, which is still debatable, for its existence implicates in multiple problems during the C++ parsing process.</p>

## Switch conditional
<p align="justify">&emsp;&emsp;Auto Windows is planned to have another conditional, that being the switch conditional, which follows the following syntax:</p>
<p align="center" style="font-family: Source Code Pro;">switch(EXPRESSION) {<br>
case VALUE1:<br>
case VALUE2:<br>
[...]<br>
default:<br>
}<br>
</p>
<p align="justify">&emsp;&emsp;The switch case conditional executes the matching case for the given expression, otherwise matching the default case. Parenthesis for the EXPRESSION are optional.<br>
</p>

## Break and Continue
<p align="justify">&emsp;&emsp;In addition to the switch conditional, the statements break and continue are also planned to be added. The break statement can be used inside loops to end them prematurely, while the continue statement can be used to skip to the next iteration of a loop.</p>

## Structs
<p align="justify">&emsp;&emsp;The creation of structures, which is a special variable capable of carrying multiple other variables inside it. The struct follows the following syntax:</p>
<p align="center" style="font-family: Source Code Pro;">struct STRUCT_NAME {<br>
	TYPE1 VAR1;<br>
	TYPE2 VAR2;<br>
[...]<br>
}<br>
<br>
STRUCT_NAME myStructure;</p>

## Operators
<p align="justify">&emsp;&emsp;Four operators are planned to be implemented in Auto Windows, those being the following:</p>

- cast operator: The cast operator is an unary operator capable of converting a variable from one type to another, as long as they are compatible.
- pow operator: The pow operator is a binary operator which has the function of compute the power of a number.
- module operator: The module operator is a binary operator which returns the rest of a integer division.
- assignment by reference: The assignment by reference operator has the function of assigning the reference of a variable to another.

## Uint
<p align="justify">&emsp;&emsp;The unsigned int (Uint) type is yet to be implemented completely, being forgotten during the development process by mistake.</p>

## More getKeyState keys
<p align="justify">&emsp;&emsp;Currently, the only key the getKeyState function accepts is the Escape key. More keys are yet to be implemented, possibly all the keyboard keys or at least most of them.</p>

## -gpp flag
<p align="justify">&emsp;&emsp;A -gpp flag is yet to be added. Its function is to automatically compile the C++ code to an executable if the g++ compiler is available.</p>