# 70 - To print square pattern with * symbols
msg = '70 - To print square pattern with * symbols'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
# To print square pattern with * symbols
n=int(input('Enter n value: '))
for i in range(n):
	if i != 0:
		print()
	for j in range(n):
		print('*')
''')
n=int(input('Enter n value: '))
for i in range(n):
	print('* '*n)

print('\n\n')

for i in range(n):
	if i==0 or i==(n-1) :
		print('* '*n)
	else:
		print('*' + ' '*(2*n-3) + '*')
