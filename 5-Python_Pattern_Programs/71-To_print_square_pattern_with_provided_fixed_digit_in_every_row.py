# 71 - To print square pattern with provided fixed digit in every row
msg = '71 - To print square pattern with provided fixed digit in every row'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
# To print square pattern with provided fixed digit in every row
n=int(input('Enter n value: '))
if n>0 and n<10 :
	for i in range(1,n+1):
		print((str(i)+' ')*n)
else:
	print('Sorry, the number is greather than 9')
''')
n=int(input('Enter n value: '))
if n>0 and n<10 :
	for i in range(1,n+1):
		print((str(i)+' ')*n)
else:
	print('Sorry, the number is greather than 9')

print('\n\n')

if n>0 and n<10 :
	for i in range(1,n+1):
		if i==1 or i==n :
			print((str(i)+' ')*n)
		else:
			print(str(i) + ' '*(2*n-3) + str(i))
else:
	print('Sorry, the number is greather than 9')