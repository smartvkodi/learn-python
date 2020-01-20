# 74 -  To print Inverted Right Angle Triangle pattern with * symbols
msg = '74 -  To print Inverted Right Angle Triangle pattern with * symbols'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
#  To print Inverted Right Angle Triangle pattern with * symbols
n=int(input('Enter n value: '))
for i in range(n,0,-1):
	print(('* ')*(i+1))
''')
n=int(input('Enter number of rows: '))
for i in range(n,0,-1):
	print(('* ')*i)

print('\n\n')
for i in range(n,0,-1):
	print((str(n-i) + ' ')*i)

print('\n\n')
for i in range(n):
	print((chr(65+i) + ' ')*(n-i))

