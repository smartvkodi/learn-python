# 32 -Python Data Types: None
print('\n')
msg = '32 - Data Types: None'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n1. None - to represent nothing - No value associated
- useful for handle the situations 
when the variable's value is not available ''')

x=10
print('\nx = ', 10)
print('       ---- ')
print('x --> | 10 | addres of object id(x)=', id(x))
print('       ---- ')
x=None
print('\nx=None')
print('type(x) =', type(x), 'None - is also an object')
print(' ----')
print('|None| - in Python there is only one None object throughout our application')
print(' ---- ')
print('/      ---- ')
print('x      | 10 | <- this object is eligible for garbage collection')
print('       ---- ')
print('id(x) =\t\t' , id(None))
print('id(None) =\t' , id(None))

print('\n\n- define a function f1 which returns 10 value')
print('''def f1():
	return 10
x = f1()''')
def f1():
	return 10
x = f1()
print('print(x) -> ', x) # f1 returns 10

print('\n- define a function f2 which do something but returns nothing')
print('''def f2():
	pass
x = f2()''')
def f2():
	pass
x = f2()
print('print(x) ->', x) # prints None