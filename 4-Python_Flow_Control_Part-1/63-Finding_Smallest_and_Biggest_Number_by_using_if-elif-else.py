# 63 - Finding Smallest and Biggest Number by using if-elif-else Statement
msg = '63 Finding Smallest and Biggest Number by using if-elif-else Statement'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Program-1: Find the biggest Number of 2 given numbers
no1 = int(input('Enter first number:'))
no2 = int(input('Enter second number:'))
max = no1
if no1 < no2:
	max = no2
print('The biggest number is:', max)
''')

no1 = int(input('Enter first number:'))
no2 = int(input('Enter second number:'))
max = no1
if no1 < no2:
	max = no2
print('The biggest number is:', max)

print('''\nProgram-2: Find the smallest Number of 2 given numbers
no1 = int(input('Enter first number:'))
no2 = int(input('Enter second number:'))
min = no1
if no1 > no2:
	min = no2
print('The smallest number is:', min)
''')

no1 = int(input('Enter first number:'))
no2 = int(input('Enter second number:'))
min = no1
if no1 > no2:
	min = no2
print('The smallest number is:', min)


print('''\nProgram-3: Find the biggest Number of 3 given numbers
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
if a>b and a>c:
	max = a
elif b>c:
	max = b
else:
	max = c
print('The biggest number is:', max)
''')

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
if a>b and a>c:
	max = a
elif b>c:
	max = b
else:
	max = c
print('The biggest number is:', max)


print('''\nProgram-4: Find the smallest Number of 3 given numbers
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
if a<b and a<c:
	min = a
elif b<c:
	min = b
else:
	min = c
print('The smallest number is:', min)
''')

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
if a<b and a<c:
	min = a
elif b<c:
	min = b
else:
	min = c
print('The smallest number is:', min)

print('''\nProgram-5: Check if the given number is between 1 and 100
a = int(input('Enter any number:'))
if a>1 and a<100:
	print('The entered number is between 1 and 100)
else:
	print('The entered number is not between 1 and 100)

''')

a = int(input('Enter any number:'))
if a>=1 and a<=100:
	print('The entered number {} is in between 1 and 100'.format(a))
else:
	print('The entered number {} is not in between 1 and 100'.format(a))
