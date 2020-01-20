# 86 - Program to generate prime numbers which are less than or equal the given number
msg = '86 - Program to  generate prime numbers which are less than or equal the given number'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Write a Python program to generate prime numbers which are less than or equal
the given number.

n=int(input('Enter Any Number:'))
n1=2
while n1<=n:
	is_prime=True
	for i in range(2,n1//2+1):
		if n1%i == 0:
			is_prime=False
			break
	if is_prime==True:
		print(n1)
''')

n=int(input('Enter Any Number:'))
n1=2
while n1<=n:
	is_prime=True
	for i in range(2,n1//2+1):
		if n1%i == 0:
			is_prime=False
			break
	if is_prime==True:
		print(n1)
	n1=n1+1

