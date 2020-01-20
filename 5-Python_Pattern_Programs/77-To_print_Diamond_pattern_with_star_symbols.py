# 77 -  To print Diamond pattern with * symbols
msg = '77 - To print Diamond pattern with * symbols'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
#  To print Diamond pattern with * symbols
n=int(input('Enter number of rows: '))
for i in range(n): # 0,1,2,3...n-1
	print((' ')*(n-i-1) + ('* ')*(i+1))
''')
n=int(input('Enter number of rows: '))
for i in range(2*n): # 0,1,2,3...2n-1
	if i<n :
		print((' ')*(n-(i+1)) + ('* ')*(i+1))
	else:
		print((' ')*((i+1)-n) + ('* ')*(2*n-(i+1)))
		#print((' ')*i + ('* ')*(n-i))



