# 24-Python Data Types: List data type
print('\n')
msg = '24 - Collection Related Data Types: List data type'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\nIf you want to represent a group of individual things as a single entity
then we require a Collection Related Data Types ''')
print('''\nlist \t tuple \t set \t frozenset
dict \t range \t bytes \t bytearray''')

print('''\n1. list - to represent a group of individual objects as a single entity
where 
 - the duplicates are allowed
 - the order is important, indexing concept is applicable
 - heterogeneous objects are allowed
 - growable in nature
 - list is mutable''')

l = [10,20,20,30]
print('\nl = [10,20,20,30] =>',l)
print('type(l) -> ', type(l), ' ! note the order is preserved, duplicates are allowed')

l = [10,10,100.5,10+30j,True,'durga']
print("\nl = [10,10,100.5,10+30j,10,True,'durga'] =>",l)
print('type(l) -> ', type(l), ' ! note the order is preserved, duplicates are allowed')

l = [10,'durga',20,10,30]
print("\nl = [10,'durga',20,10,30] =>",l)
print('l[0] -> ', l[0], ' - ! note the list is 0 indexed')
print('l[-1] -> ', l[-1], ' - ! the last element in the list')
print('l[1:4] -> ', l[1:4], ''' # slicing concept applicable => returns a list of elemets 
from 1 index to (4-1) index''')

l = []
print("\nl = [] =>",l,' - we created an empty list')
l.append('durga')
print("l.append('durga') =>",l,' - adding an element to the list')
l.append(20)
print("l.append(20) =>",l,' - adding another element to the list')
l.append(30)
print("l.append(30) =>",l,' - adding another element to the list')
l.append(20)
print("l.append(20) =>",l,' - adding another element to the list')
l.remove(20)
print("l.remove(20) =>",l,' - remove an element from the list')
l[0]=7777
print("l[0]=7777) =>",l,' - replace an element in the list')