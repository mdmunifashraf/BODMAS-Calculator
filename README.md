# BODMAS-Calculator

String Arithmetic Calculator

This repository contains Calculator.py, a Python script that evaluates arithmetic expressions directly from string input. It parses numbers and mathematical operators manually and calculates the result following basic order of operations, without relying on Python's built-in eval() function. 

Features:
  Custom Parsing Algorithm: Reads the input string character by character to sequentially separate integers from operators (+, -, *, /).
  Order of Operations: Processes division (/) and multiplication (*) first, followed by addition (+) and subtraction (-).   
  No External Dependencies: Built entirely using standard Python logic, loops, and list manipulations.   

How It Works: 
1. The user is prompted to enter an arithmetic expression. 
2. The script appends a ! character to act as an end-of-string marker for the parsing loop. 
3. It extracts all the numbers and operators into two separate lists, combining adjacent digits into multi-digit numbers.
4. The script iterates through the operators to perform all / and * operations first, updating the numbers list and dynamically adjusting the list
   indices.
5. It then removes the processed / and * operators from the operator list.   A final loop processes the remaining + and - operations using the updated
   number values. 
6. The final calculated value, which remains at the first index of the numbers list, is printed to the console. 

Usage: Run the script from your terminal or command prompt: Bashpython Calculator.py

Example: 
Enter the expression: 10+5*2-4/2
18.0
