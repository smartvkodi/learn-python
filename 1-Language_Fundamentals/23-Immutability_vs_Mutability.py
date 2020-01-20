# 23-Immutability vs Mutability
print('\n')
msg = '23 - Immutability vs Mutability'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\nAll fundamental data types in Python are Immutable
- int / float / complex / bool / str 
but object reusability is applicable only for
- int / float / bool / str  
so, reusability is not available for compex data type (be careful..)''')

print('\n- Check Reusability of int')
a=10
b=10
print('a=', a)
print('b=', b)
print('a is b -> ', a is b)

print('\n- Check Reusability of float')
a=10.5
b=10.5
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

print('\n- Check Reusability of complex')
a=10+20j
b=10+20j
print('''Durga said that Object Reusability 
is NOT AVAILABE FOR complex!!!
Then why for me:''', )
print('a=', a, 'type(',a,') = ',type(a))
print('b=', b, 'type(',b,') = ',type(b))
print('a is b -> ', a is b)

print('\n- Immutability Example:')
x=10
print('x=', x, 'id(x)=', id(x))
print(' - we try to modify x=x+1')
x=x=1
print('x=', x, 'id(x)=', id(x))


print('\n- Mutability Example:')
l=[10,20,30]
print('l=',l)
print('id(l)=', id(l))

print('- now, modify l[0]=7777')
l[0]=7777
print('l=',l)
print('id(l)=', id(l), 'the id of list did not modify')
print(' so, the list is mutable')

print('\n other example to demonstrate that the list is mutable')
l1=[10,20,30,40]
l2=l1
print('l1=',l1)
print('l2=',l2)
print('l1 is l2 ->', l1 is l2)
print('id(l1)=', id(l1))
print('id(l2)=', id(l2))

print('''- now, modify l1[0]=7777 and will be reflected in l2, too
because l1 and l2 are references to the same object''')
l1[0]=7777
print('l1=',l1)
print('l2=',l2)

print('''- now, modify l2[1]=8888 and will be reflected in l1, too
because l1 and l2 are references to the same object''')
l2[1]=8888
print('l1=',l1)
print('l2=',l2)
