# 28 -Python Data Types: Dict
print('\n')
msg = '28 - Collection Related Data Types: Dict'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n1. Dict - to represent a group of objects key-value pairs as a single entity
where
 - Dict is group of key-value pairs, 
 - the duplicates keys are not allowed but values are allowed
 - the order is not guaranted, objects are ordered based on hashcode of the keys
 - heterogeneous keys and values are allowed
 - Dictionary is mutable
 - Indexing, slicing are not applicable''')

print('\nHow to create a dictionary?')
d = {100:'durga',200:'sunny',300:'chinny'}
print("d={100:'durga',200:'sunny',300:'chinny'} =>",d)
print('type(d) =>', type(d))

print('\nHow to create an empty dictionary?')
d={}
print("d={} =>",d)
print('type(d) =>', type(d))
print('and then add the key-value pairs => d[key]=value')

d[100]='durga'
print("\nd[100]='durga' => ", d)
d[200]='ravi'
print("d[200]='ravi' => ", d)

d[300]='sunny'
print("\nd[300]='sunny' => ", d)
d[300]='shiva'
print("d[300]='shiva' => ", d, '''- the old value of key=300 
'sunny' will replaced with new value 'shiva' ''')


