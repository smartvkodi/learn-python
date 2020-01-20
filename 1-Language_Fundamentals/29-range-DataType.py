# 29 -Python Data Types: Range
print('\n')
msg = '29 - Collection Related Data Types: Range'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n1. Range - to represent a sequence of values as a single entity
where
 - Range is a sequence of values, 
 - order is important
 - Indexing and slicing concepts are applicable
 - Range object is immutable''')

print('\nHow to create a range data type?')
print('\nForm-1 - range(n) => a sequence of numbers from 0 to n-1')
r = range(5)
print("r = range(5) =>",r, 'to represent the integers from 0 to 4')
print('type(r) =>', type(r))
print('''for x in r:
	print(x)''')
for x in r:
	print(x)

r = range(100)
print("\nr = range(100) =>",r, 'to represent the integers from 0 to 99')


print('\nForm-2 - range(begin, end) => a sequence of numbers from \'begin\' to \'end-1\'')
r = range(5,10)
print("r = range(5,10) =>",r, 'to represent the integers from 5 to 9')
print('type(r) =>', type(r))
for x in r:
	print(x)


print('''\nForm-3 - range(begin, end, increment/decrement) 
=> a sequence of numbers from \'begin\' to \'end-1\' ''')
r = range(5,12,2)
print("r = range(5,12,2) =>",r, 'to represent the integers from 5 to 12')
print('type(r) =>', type(r))
for x in r:
	print(x)

r = range(100,57,-10)
print("r = range(100,57,-10) =>",r, 'to represent the integers from 100 to 57')
print('type(r) =>', type(r))
for x in r:
	print(x)


print('\nRange - Indexing, slicing are applicable')
r = range(10,21)
print("r = range(10,21) =>",r, 'to represent the integers from 10 to 20')
print('r[0] = ', r[0])
print('r[-1] = ', r[-1])
print('r[1:5] = ', r[1:4])
r1 = r[1:4]
for x in r1:
	print(x)

# r[1] = 7777
print('\n r[1] = 7777 => TypeError: \'range'' object does not support item assignment')

