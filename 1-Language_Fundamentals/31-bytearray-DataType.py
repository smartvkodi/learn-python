# 31 -Python Data Types: Bytearray
print('\n')
msg = '31 - Collection Related Data Types: Bytearray'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n1. Bytearray - to represent a group of byte values as a single entity
when you want to handle binary data like images, video or audio files
 - Bytearray data type can represents values only from 0 to 255, 
 - Indexing and slicing concepts are applicable
 - Bytearray object is mutable''')

print('\nHow to create a \'bytearray\' data type?')
l=[10,20,30,40]
print('l=[10,20,30,40] => ', l)
ba = bytearray(l)
print('ba = bytearray(l) => type(ba) = ', type(ba))
print('ba[0] = ', ba[0])
print('ba[-1] = ', ba[-1])
print('''for x in ba:
	print(x)''')
for x in ba:
	print(x)

print('\nBytearray data type can represents values only from 0 to 255')
l=[10,200,256,40]
print('l=[10,200,256,40] => ', l)
# ba = bytearray(l)
print('ba = bytearray(l) => ValueError: bytes must be in range(0, 256)')

print('\nBytearray data type is mutable')
l=[10,20,30,40]
print('l=[10,20,30,40] => ', l)
ba = bytearray(l)
print('ba[0] = ', ba[0])
ba[0] = 77
print('ba[0] = ', ba[0])
for x in ba:
	print(x)


