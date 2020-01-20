# 25-Python Data Types: Tuple data type
print('\n')
msg = '25 - Collection Related Data Types: Tuple data type'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n1. tuple - to represent group of individual objects as a single entity
where 
 - the duplicates are allowed
 - the order is important, indexing concept is applicable
 - heterogeneous objects are allowed
 - tuple is immutable''')

print('\nTuple - represent an Read-Only version of List')

t = (10,20,20,30)
print('\nt = (10,20,20,30) =>',t)
print('type(t) -> ', type(t), ' ! note the order is preserved, duplicates are allowed')

t = (10,10,100.5,10+30j,True,'durga')
print("\nt = (10,10,100.5,10+30j,10,True,'durga') =>",t)
print('type(t) -> ', type(t), ' ! note the order is preserved, duplicates are allowed')

t = (10,'durga',20,10,30)
print("\nt = (10,'durga',20,10,30) =>",t)
print('t[0] -> ', t[0], ' - ! note the tuple is 0 indexed')
print('t[-1] -> ', t[-1], ' - ! the last element in the list')
print('t[1:4] -> ', t[1:4], ''' # slicing concept applicable => returns a tuple 
of elements from 1 index to (4-1) index''')

print('\n\n!!! - tuple is immutable, so we can not perform any modification')
t = (20,30)
print("\nt = (20,30) =>",t,' - we created an tuple')

# t.append('durga')
print("t.append('durga') =>",t,'AttributeError: \'tuple\' object has no attribute \'append\'')

# t.remove(20)
print("t.remove(20) =>",t,'AttributeError: \'tuple\' object has no attribute \'remove\'')

# t[0]=7777
print("t[0]=7777) =>",t,'TypeError: \'tuple\' object does not support item assignment')

t = (20)
print("\nt = (20) =>",t,' - we did not create an tuple!')
print('type(t) =',type(t), 'is int')

t = (20,)
print("\nt = (20,) =>",t,' - is a tuple!')
print('type(t) =',type(t), 'is a tuple')