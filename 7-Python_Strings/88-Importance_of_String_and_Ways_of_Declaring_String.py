# 87 - Importance of String and Ways of Declaring String
msg = '87 - Importance of String and Ways of Declaring String'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. String Data Type - is most commonly used data type
## more than 90% of objects in any application are strings
## the most common used objects in any applications is string
''')
print('''Example: String Data Type
## Remember the Voter Registration Application
there are more than 90% of objects are string
''')

print('''I want to read data from keyboard
### the "input" in-build function I have to use
### "input" function returns string data-type
n=input('Enter n value: ')
print(type(n)) => str 

Why the Python people given very much importance for string?
Because the string is the most common data-type used!
''')

print('''Commom Line Arguments are stored into "argv variable" in str format
- for accessing the cmd line arguments we require access 
the "argv variable" which is present into "sys" module

py test.py 10 20 -> argv internaly is a list
argv[1] + argv[2] => '1020' BUT NOT 30!!!
''')

print('''\n2. What is string?
string is a sequence of carachters in single or double quotes

ch='a' - C, C++, Java - there is char data type

but in Python char data type is not available
ch='a' is treated as string
''')

print('''When we can use "triple-quotes"? 
- when we want to define the multi-lines strings letterals
- when we want to include into string sigle-quotes or double-qoutes
- when we want to define the doc strings
''')

print('''Defining a string variable we easy can get the error when we have  to
include into our string single-quotes, double-quotes
## !!! to avoid the SyntaxError: invalid syntax !!
- using combinations of single-quotes, double-quotes
- using escape characters: \\' \\"
- or beter using the \'\'\' - triple-quotes

Example: s=\'\'\'This is ' sing-quotes symbol and this is " double-quotes symbol\'\'\'
''')
	
	

