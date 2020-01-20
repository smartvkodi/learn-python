# 75 -  To print Pyramid pattern with * symbols
msg = '75 - To print Pyramid pattern with * symbols'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
#  To print Pyramid pattern with * symbols
n=int(input('Enter number of rows: '))
for i in range(n): # 0,1,2,3...n-1
	print((' ')*(n-i-1) + ('* ')*(i+1))
''')
n=int(input('Enter number of rows: '))
for i in range(n):
	print((' ')*(n-i-1) + ('* ')*(i+1))


print('''\n2. Example-2. 
#  To print Inverted Pyramid pattern with * symbols
n=int(input('Enter n value: '))
for i in range(n): # 0,1,2,3...n-1
	print((' ')*i + ('* ')*(n-i))
''')
for i in range(n):
	print((' ')*i + ('* ')*(n-i))


