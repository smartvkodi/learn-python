# 85 - Program to check whether the given number is prime number or not
msg = '85 - Program to check whether the given number is prime number or not'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Write a Python program Program to check whether 
the given number is prime number or not

n=int(input(Enter Any Number:'))
if n<=1:
	print('It si not prime number')
else:
	is_prime=True
	for i in range(2,n//2+1)"
		if n%i == 0:
			is_prime=False
			break
	if is_prime==True:
		print('It is prime number')
	else:
		print('It is not prime number')
''')

n=int(input('Enter Any Number: '))
if n<=1:
	print('It is not prime number')
else:
	is_prime=True
	for i in range(2, n//2+1):
		if n%i == 0:
			is_prime=False
			break
	if is_prime==True:
		print('It is prime number')
	else:
		print('It is not prime number')

