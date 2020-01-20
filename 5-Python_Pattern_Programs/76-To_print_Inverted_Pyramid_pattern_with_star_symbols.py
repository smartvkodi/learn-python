# 76 -  To print Inverted Pyramid pattern with * symbols
msg = '76 - To print Inverted Pyramid pattern with * symbols'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
#  To print Inverted Pyramid pattern with * symbols
n=int(input('Enter n value: '))
for i in range(n): # 0,1,2,3...n-1
	print((' ')*i + ('* ')*(n-i))
''')

n=int(input('Enter n value: '))
for i in range(n):
	print((' ')*i + ('* ')*(n-i))


