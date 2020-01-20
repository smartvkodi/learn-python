# 62 - if-elif-else statement and applications
msg = '62 if-elif-else statement and applications'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')


print('''Example-1: simply if statement
name = input('Enter your name:')
if name == 'durga':
	print('Hello Durga, Good Evening')
print('How are you?') # statement out of condition
''')
name = input('Enter your name:')
if name == 'durga':
	print('Hello Durga, Good Evening') # identeted statement under if condition
print('How are you?')


print('''\nExample-2: if-else statement
if condition|:
	Action-1
else:
	Action-2
statement...

name = input('Enter your name:')
if name == 'durga':
	print('Hello Durga, Good Evening')
else:
	print('Hello Guest, Good Evening')
print('How are you?') # statement out of condition
''')
name = input('Enter your name:')
if name == 'durga':
	print('Hello Durga, Good Evening')
else:
	print('Hello Guest, Good Evening')
print('How are you?') # statement out of if-else


print('''\nExample-3: if-elif-else statement
if condition-1|:
	Action-1
elif condition-2:
	Action-2
elif condition-3:
	Action-3
	.
	.
	.
else:
	Default Action
statement...

brand = input('Enter your favorite brand:')
if brand == 'KF':
	print('It is a childrens brand')
elif brand == 'KO':
	print('It is too light')
elif brand == 'RC':
	print('It is not that much kick')
elif brand == 'FO':
	print('Buy one Get one Free')
else:
	print('Other brands are not recommended')
''')
brand = input('Enter your favorite brand:')
if brand == 'KF':
	print('It is a childrens brand')
elif brand == 'KO':
	print('It is too light')
elif brand == 'RC':
	print('It is not that much kick')
elif brand == 'FO':
	print('Buy one Get one Free')
else: # is always optional
	print('Other brands are not recommended')
