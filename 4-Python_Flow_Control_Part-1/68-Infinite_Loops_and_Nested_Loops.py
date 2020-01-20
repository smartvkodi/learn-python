# 68 - Infinite Loops and Nested Loops
msg = '68 - Infinite Loops and Nested Loops'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Example-1. 
# Infinite loop
i=1
while True:
	print('Hello, infinite loop: ', i)
	i=i+1

How can we solve this problem?
while True:
	print('Hello, infinite loop: ', i)
	i=i+1
	if our required condition satisfied
	break
''')


print('''\n2. Example 2:
# Nested lopps - loop inside another loop

for i in range(3): # 0,1,2
	for j in range(2): # 0,1
		print("Hello")
''')
for i in range(3):
	for j in range(2):
		print("Hello")

print('''\n3. Example 3:
# Nested lopps - loop inside another loop

for i in range(3): # 0,1,2
	for j in range(2): # 0,1
		print('i={}, j={}'.format(i,j))
''')
for i in range(3): # 0,1,2
	for j in range(2): # 0,1
		print('i={}, j={}'.format(i,j))
