# 27 -Python Data Types: FrozenSet
print('\n')
msg = '27 - Collection Related Data Types: FrozenSet'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n1. FrozenSet - to represent group of individual objects as a single entity
where 
 - the duplicates are not allowed
 - the order is not applicable
 - heterogeneous objects are allowed
 - FrozenSet is like Set but it is immutable''')

s = {10,20,20,30,40}
print('\ns = {10,20,20,30,40} =>',s, 'create a set')
fs = frozenset(s)
print('fs = frozenset(s) =>',fs, 'create a FrozenSet')
print('type(fs) -> ', type(fs), ''' ! note the order is not applicable, 
duplicates are not allowed''')

s = {10,10,100.5,10+30j,True,'durga'}
print("\ns = {10,10,100.5,10+30j,10,True,'durga'} =>",s, 'create a set')
fs = frozenset(s)
print('fs = frozenset(s) =>',fs, 'create a FrozenSet')
print('type(fs) -> ', type(fs), ''' ! note the order is not applicable, 
duplicates are not allowed''')

# print(fs[1])
print('fs[1] -> TypeError: \'frozenset\' object is not subscriptable')

print('\n!!! - FrozenSet is immutable, so we can not perform any modification')
# fs.add(50)
print('fs.add(50) -> AttributeError: \'frozenset\' object has no attribute \'add\'')

# fs.remove(100.5)
print('fs.remove(100.5) -> AttributeError: \'frozenset\' object has no attribute \'remove\'')

