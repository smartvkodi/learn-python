# 37 -  Logical Operators For Boolean Types
print('\n')
msg = '37 -  Logical Operators For Boolean Types'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''- Logical Operators For Boolean Types: and, or, not ''')

print('''\n1. and - operator returns True if only if both arguments are True''')

print('True and True #', True and True) # True
print('True and False #', True and False) # False
print('False and True #', False and True) # False
print('False and False #', False and False) # False

print('''\n2. or - operator returns True if only if at least one argument is True''')

print('True or True #', True or True) # True
print('True or False #', True or False) # True
print('False or True #', False or True) # True
print('False or False #', False or False) # False


print('''\n3. not - operator reverse operator''')

print('not True #', not True) # False
print('not False #', not False) # True



print('''\n4. I want to develop an small authentication application
I will read username and password from keyboard
- use input() function to read keyboard input''')

username=input('Enter username:')
password=input('Enter password:')

if username == 'durga' and password=='sunny':
	print('Result: valid user')
else:
	print('Result: invalid user')
