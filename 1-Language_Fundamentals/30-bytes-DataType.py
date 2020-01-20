# 30 -Python Data Types: Bytes and Bytearray
print('\n')
msg = '30 - Collection Related Data Types: Bytes and Bytearray'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n1. Bytes - to represent a group of byte values as a single entity
when you want to handle binary data like images, video or audio files
 - Bytes data type can represents values only from 0 to 255, 
 - Indexing and slicing concepts are applicable
 - Bytes object is immutable''')

print('\nHow to create a \'bytes\' data type?')
l=[10,20,30,40]
print('l=[10,20,30,40] => ', l)
b = bytes(l)
print('b = bytes(l) => type(b) = ', type(b))
print('''for x in b:
	print(x)''')
for x in b:
	print(x)

print('\nBytes data type can represents values only from 0 to 255')
l=[10,200,256,40]
print('l=[10,200,256,40] => ', l)
# b = bytes(l)
print('b = bytes(l) => ValueError: bytes must be in range(0, 256)')

print('\nBytes data type is immutable')
l=[10,20,30,40]
print('l=[10,20,30,40] => ', l)
b = bytes(l)
print('b[0] = ', b[0])
# b[0] = 77
print('b[0] = 77 => TypeError: \'bytes\' object does not support item assignment')


