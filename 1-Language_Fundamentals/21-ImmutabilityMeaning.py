# 21-Immutability Meaning
print('\n')
msg = '21 - Fundamental Data Types vs Immutability Meaning'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\nMutable -> Changeable
Immutable -> Non Changeable''')

print('''\nAll fundamental data types in Python are Immutable
- int / float / complex / bool / str 
Once we create an object we can not perform any changes in that object.
If we are trying to perform any changes, 
a new object with those changes will be created. ''')

x=10
print('x = ', 10)
print('       ---- ')
print('x --> | 10 | addres of object id(x)=', id(x))
print('       ---- ')
x=x+1
print('we try to modify x=x+1 => new object with id(x)=', id(x))
print(''' - a new object will be created (11) and 
 - the refrence variable x will point to new object (11)
- the old 10 object having no refrence variable will 
  become eligible for garbage collection (GC from PVM)''')

print('\n - Other example')
print('x=10')
print('y=x')
x=10
y=x
print('id(x)=', id(x))
print('id(y)=', id(y))
print(' - and then increment y => y=y+1')
y=y+1
print('x=',x,' with id(x)=', id(x))
print('y=',y,' with id(y)=', id(y))

 