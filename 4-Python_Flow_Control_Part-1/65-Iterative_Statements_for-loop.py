# 65 - Iterative Statements: for loop
msg = '65 - Iterative Statements: for loop'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Iterative Statements:
	1. for-loop
	2. while-loop''')

print('''1. for-loop
applicabile for collections and string
python syntax:
for x in sequence:
	Activity-1

s='Sunny Leone' # I want to print every character present in this string
for x in s:
	print(x)
''')
s='Sunny Leone' # I want to print every character present in this string
for x in s:
	print(x)

print('''\n## I want to print the character present at specified index
s='Sunny Leone'
i=0
for x in s:
	print('The character present at {} index: {}'.format(i, x))
	i=i+1 ## or i+=1
''')
s='Sunny Leone'
i=0
for x in s:
	print('The character present at {} index: {}'.format(i, x))
	i=i+1 ## or i+=1

print('''\n## I want to get the string dynamically from keyboard 
and then to print the character present at specified index

s=input('Enter any string:')
i=0
for x in s:
	print('The character present at {} index: {}'.format(i, x))
	i=i+1 ## or i+=1
''')
s=input('Enter any string:')
i=0
for x in s:
	print('The character present at {} index: {}'.format(i, x))
	i=i+1 ## or i+=1
