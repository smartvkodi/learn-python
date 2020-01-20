# 72 - To print square pattern with alphabet symbols
msg = '72 - To print square pattern with alphabet symbols'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
# To print square pattern with alphabet symbols
n=int(input('Enter n value: '))
for i in range(n):
	print((chr(65+i)+' ')*n)
''')
n=int(input('Enter n value: '))
for i in range(n):
	print((chr(65+i)+' ')*n)


print('\n\n')

for i in range(n):
	if i==0 or i==n-1 :
		print((chr(65+i)+' ')*n)
	else:
		print(chr(65+i) + ' '*(2*n-3) + chr(65+i))