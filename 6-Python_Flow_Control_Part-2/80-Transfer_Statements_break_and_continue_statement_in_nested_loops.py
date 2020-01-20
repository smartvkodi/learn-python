# 80 - Transfer Statements: break and continue in nested loops
msg = '80 - Transfer Statements: break and continue in nested loops'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. break in nested loops
\t# break - stops executions only in its inner loop
for i in range(3): # 0,1,2
	for j in range(3): # 0,1,2
		if i == j:
			break # the control is coming outside the current loop
		print(i,j)	
	...
the output:
''')
for i in range(3): # 0,1,2
	for j in range(3): # 0,1,2
		if i == j:
			break # the control is coming outside the current loop
		print(i,j)


print('''\n\n2. continue in nested loops
\t# continue - skips to next iteration only in its inner loop
for i in range(3): # 0,1,2
	for j in range(3): # 0,1,2
		if i == j:
			continue # skips to next iteration into current loop
		print(i,j)	
	...
the output:
''')
for i in range(3): # 0,1,2
	for j in range(3): # 0,1,2
		if i == j:
			continue # skips to next iteration into current loop
		print(i,j)	
