# 79 - Transfer Statements: continue statement
msg = '78 - Transfer Statements: continue statement'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Transfer Statements: continue statement
# continue statement - it is used only inside a loop
to skip current iteration and continue the next iteration

for i in range(10): # 0 to 9
	if i %2 == 0:
		# break # => will go directly out of the loop - no more iterations
		continue # will skip this iteration and go for next iteration
	print(i)	
	...
the output:
''')
for i in range(10): # 0 to 9
	if i %2 == 0:
		# break # => will go directly out of the loop - no more iterations
		continue # will skip this iteration and go for next iteration
	print(i)


print('''\n\nExample 1 - in shopping cart applications 
I add multiple items into cart and then process the shopping cart.
If an item require insurance then skip the item and continue 
for the remaining items

cart = [10,20,30,600,70,900,50,23,80] # each item prices
for item in cart :
	if item>500 :
		print("Insurance must be required, just skipping this item...")
		continue
	print('processing item:', item)
''')
cart = [10,20,30,600,70,900,50,23,80] # each item prices
for item in cart :
	if item>500 :
		print("Insurance must be required, just skipping this item...")
		continue
	print('processing item:', item)


print('''\n\nExample 2 - I want to devide 100 with each element from the list

l = [10,20,0,5,0,30]
for x in l:
	print('100/{}={}'.format(x, 100/x))
	### 100/0 => ZeroDivisonError: division by 0
	### How can we solve this problem?

for x in l:
	if x==0:
		print('Hello Stupid, How we can divide with zero??!!')
		continue
	print('100//{}={}'.format(x, 100//x))
''')
l = [10,20,0,5,0,30]
for x in l:
	if x==0:
		print('Hello Stupid, How we can divide with zero??!!')
		continue
	print('100//{}={}'.format(x, 100//x))


print('''\n\nExample 3 - If you want use continue statement
compulsary you should use it inside loops (same for break)

x=10
if x > 40 :
	print('Hello')
	continue
print('Hi')

SyntaxError: 'continue' not properly in loop
''')
