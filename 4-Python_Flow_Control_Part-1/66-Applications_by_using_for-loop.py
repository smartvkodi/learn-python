# 66 -  Applications by using for loop
msg = '66 -  Applications by using for loop'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Application 1:
# I want to print 'Hello welcome to Python for-loop' 10 times

range(n) => 0 to n-1
range(m,n) => m to n-1
range(m,n, increment_decrement) => m to n-1

for x in range(10):
	print('Hello welcome to Python for-loop')
''')
for x in range(10):
	print('Hello welcome to Python for-loop')

print('''\n2. Application 2:
# I want to print numbers from 1 to 10

for x in range(1,11):
	print(x)
''')
for x in range(1,11):
	print(x)

print('''\n3. Application 3:
# I want to display odd numbers from 1 to 20

for x in range(21):
	if x%2==1:
		print(x)
''')
for x in range(21):
	if x%2 != 0:
		print(x)

### alternate way to generate odd numbers
for x in range(1,21,2):
	print(x)


print('''\n4. Application 4:
# I want to display numbers from 10 to 1

for x in range(10,0,-1):
	print(x)
''')
for x in range(10,0,-1):
	print(x)


print('''\n5. Application 5:
# I want to print the sum of numbers in the given list
# I do not want to hard-code the list, you have to read
the list from keyboard

list=eval(input('Enter list of numbers: l='))
sigma=0
for x in list:
	sigma = sigma + x
print('The sum:', sigma)

### alternative way
print('sum(list) =', sum(list))
''')
list=eval(input('Enter list of numbers: '))
sigma=0
for x in list:
	sigma = sigma + x
print('The sum:', sigma)

### alternative way using in-built function sum(list)
print('sum(list) =', sum(list))

