# 26 -Python Data Types: Set data type
print('\n')
msg = '26 - Collection Related Data Types: Set data type'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n1. Set - to represent group of individual objects as a single entity
where 
 - the duplicates are not allowed
 - the order is not applicable
 - heterogeneous objects are allowed
 - set is growable & mutable''')

s = {10,20,20,30,40}
print('\ns = {10,20,20,30,40} =>',s)
print('type(s) -> ', type(s), ' ! note the order is not applicable, duplicates are not allowed')

s = {10,10,100.5,10+30j,True,'durga'}
print("\ns = {10,10,100.5,10+30j,10,True,'durga'} =>",s)
print('type(s) -> ', type(s), ' ! note the order is not applicable, duplicates are not allowed')

s = {10,'durga',20,10,30}
print("\ns = {10,'durga',20,10,30} =>",s)
print('s[0] -> TypeError: \'set\' object is not subscriptable')
print('s[1:4] -> TypeError: \'set\' object is not subscriptable')

print('\n\n!!! - set is mutable, so we can not perform any modification')
s = {20,30}
print("\ns = (20,30) =>",s,' - we created an set')

s.add(50)
print('s.add(50) =>',s,'we can \'add\' other objects to \'set\'')

s.remove(20)
print("s.remove(20) =>",s,'we can \'remove\' objects from \'set\'')

print('\nI want to create a empty set')
s = {}
print('s = {} =>',s,' - we did not create a set!')
print('type(s) =',type(s), 'is a dictionary')

print('\nHow I can create a empty set?')
s = set()
print('s = set() =>',s,' - we did create an empty set!')
print('type(s) =',type(s))
