# 73 - To print Right Angle Triangle pattern with * symbols
msg = '73 - To print Right Angle Triangle pattern with * symbols'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
# To print Right Angle Triangle pattern with * symbols
n=int(input('Enter n value: '))
for i in range(n):
	print(('* ')*(i+1))
''')
n=int(input('Enter n value: '))
for i in range(n):
	print(('* ')*(i+1))

print('\n\n')
for i in range(n):
	for j in range(i+1):
		print('*', end=' ')
	print()
