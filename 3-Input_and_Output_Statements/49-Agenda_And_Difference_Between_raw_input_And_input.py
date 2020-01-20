# 49 - Agenda & Difference between raw_input() and input() functions
msg = '49 - Agenda & Difference between raw_input() and input() functions'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('Input and Output Statements\n')

print('\n1. raw-input() vs input() applicable only in Python 2.x')

print('''\n# raw-input() this functions can be used to read end-user provided data
The problem with this function is that it always return the result in string 
form only and compulsory always we have to perform  type casting''')

print('''Example: 
	x = raw_input('Enter some value:') <- 10
	y = int(x)
	print(type(x)) -> str''')

print('''\n# input() this functions can be used to read end-user provided data
and provide the result based on the value data-type - we are not require
to perform any type casting.
- if end-user provide int input data directly, input() function will provide int type
- if end-user provide str input data directly, input() function will provide str type''')

print('''Example: 
	x = input('Enter some value:') 
	print(type(x))
	10	--> int
	10.5	--> float
	'durga'	--> str''')

print('\n\n2. input() function - Python 3.x')
print('''\n# In Python 3.x - input() function can be used to read end-user provided data
but it always return the result in string form only and compulsory always 
we have to perform type casting''')
print('''Example: 
	x = input('Enter some value:') 
	print(type(x)) --> str''')

x = input('Enter some value:') 
print(x, '--> ', type(x))


print('\n3. How to read multiple values from keyboard in a single line')
print('4. Command Line Arguments')

print('5. Output Statement: print() function')
print('6. sep attribute')
print('7. end attribute')
print('8. printing formatted String')
print('9. Replacement operator: {}')





