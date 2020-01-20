# 22-Immutability Need
print('\n')
msg = '22 - Immutability Need'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\nWhy the Immutable is required?\n''')

x=10
y=10
z=10
print('x = ', x)
print('y = ', y)
print('z = ', z)
print('        ---')
print('x -->  /   \  addres of object id(x)=', id(x), 'x is y == ', (x is y))
print('y --> | 10  | addres of object id(y)=', id(y), 'x is z == ', (x is z))
print('z -->  \   /  addres of object id(z)=', id(z), 'y is z == ', (y is z))
print('        --- ')
x=x+1
print('Modify x=x+1')
print('x = ', x)
print('y = ', y)
print('z = ', z)
print('        ---')
print('       /   \ ')
print('x --> | 11  | addres of object id(x)=', id(x) )
print('       \   /  x is y ', (x is y), ' and  x is z ', (x is z) )
print('        ---')
print('       /   \  but y is z ', (y is z) )
print('y --> | 10  | addres of object id(y)=', id(y))
print('z -->  \   /  addres of object id(z)=', id(z))
print('        --- ')

print('\nAdvantages of Immutality -> reusability of created objects')
print('- Memory Utilization will be improoved')
print('- Performace will be improoved')
print('''\nExample: - Voter Registration Application
to prevent the program to behave abnormaly - for that
the immutability is required.''')

print('\nDisadvantages of reusability of created objects')
print('''- In the lack of immutability there is the possibility
the program to behave abnormaly''')

print('''\nReusability of created objects is available 
for int / float / bool / str''')
print('\n- Check Reusability of float')
a=1000.234
b=1000.234
print('a=', a)
print('b=', b)
print('a is b -> ', a is b)

print('\n- Check Reusability of bool')
a=True
b=True
print('a=', a)
print('b=', b)
print('a is b -> ', a is b)

print('\n- Check Reusability of str')
a='durgasoft'
b='durgasoft'
print('a=', a)
print('b=', b)
print('a is b -> ', a is b)


print('''\nIn Python, if an object is require create, PVM won\'t create 
the object immediatly! First it will check/search if any object 
with required content is already available or not. 
If the required object is aready available then that object 
will be reused.''')

print('''\nIf before creation of an object, PVM perform an search
operation, that is nor an performance issue? Yes! This is an 
performance issue but the search operation will take  less time 
than create operation so, aver all performace will be improoved''')
