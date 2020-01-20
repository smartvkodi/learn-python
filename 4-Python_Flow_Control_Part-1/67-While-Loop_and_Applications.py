# 67 - While Loop and Applications
msg = '67 - While Loop and Applications'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Python's While-loop syntax:
while condition:
	body
''')

print('''1. Example-1. 
# I want to print 'Python's while-loop' 10 times
i=1
while i<=10:
	print('Hello, Welcome to Python\'s while-loop')
	i=i+1
''')
i=1
while i<=10:
	print('Hello, Welcome to Python\'s while-loop')
	i=i+1


print('''\n2. Example 2:
# I want to print numbers from 1 to 10

i=1
while i<=10:
	print(i)
	i=i+1
''')
i=1
while i<=10:
	print(i)
	i=i+1

print('''\n3. Example 3: I want to display numbers from 1 to 20
which are divisible by 3 

i=1
while i<=20:
	if i%3==0:
		print(x)
''')
i=1
while i<=20:
	if i%3==0:
		print(i)
	i=i+1

print('''#alternative
i=3
while i<=20:
	print(i)
	i=i+3
''')

print('''\n4. Application 4:
# Write an application to display the sum of first n numbers

n = int(input('Enter a number: '))
sigma = 0
i=1
while i<=n:
	sigma+= i
	i+=1
print('The sum of first {} numbers is: {}'.format(n,sigma)')
''')
n = int(input('Enter a number: '))
sigma = 0
i=1
while i<=n:
	sigma += i
	i+=1
print('The sum of first {} numbers is: {}'.format(n,sigma))


print('''\n5. Application 4:
# while-loop - forcing an answer

name='*'
while name != 'sunny':
	if name!='*':
		print('{} is a wrong answer!!! :)'.format(name))
	name=input('Please, Enter your Favorite actress: ')
print('Thanks for confirmation!!! :)')
''')
name='*'
while name != 'sunny':
	if name!='*':
		print('{} is a wrong answer!!! :)'.format(name))
	name=input('Please, Enter your Favorite actress: ')
print('Thanks for confirmation!!! :)')