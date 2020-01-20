# 87 - Program to generate first n prime numbers
msg = '87 - Program to generate first n prime numbers'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Write a Python program to generate first n prime numbers.

n=int(input('Enter n value: '))
k=0
lchk=1
while k<n:
	lchk=lchk+1
	is_prime=True
	for i in range(2,lchk//2+1):
		if lchk%i==0:
			is_prime=False
			break
	if is_prime:
		print(lchk)
		k=k+1
''')

n=int(input('Enter n value: '))
k=0
lchk=1
while k<n:
	lchk=lchk+1
	is_prime=True
	for i in range(2,lchk//2+1):
		if lchk%i==0:
			is_prime=False
			break;
	if is_prime:
		print(lchk)
		k=k+1




		
	

