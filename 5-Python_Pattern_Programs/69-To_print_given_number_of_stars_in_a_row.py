# 69 - To print given number of *s in a row
msg = '69 - To print given number of *s in a row'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
# To print given number * in the same row
n=int(input('Enter n value: '))
for i in range(n):
	print('*', end=' ')
''')
n=int(input('Enter n value: '))
for i in range(n):
	print('*', end=' ')
