# 78 - Transfer Statements: break statement
msg = '78 - Transfer Statements: break statement'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Transfer Statements: 
	1. break statement
	2. continue statement
# 1. break statement - it is used inside a loop when based
on some condition, you want to stop the loop execution

for i in range(10):
	...
	if i==7:
		break ## => the control is coming outside the loop
	...
''')

print('''\nExample 1
for i in range(10): ## 0 to 9
	if i==7:
		print('processing is enough, please break loop execution'
		break
	print(i)
print('outside of loop')
''')
for i in range(10):
	if i==7:
		print('processing is enough, please break loop execution')
		break
	print(i)
print('outside of loop')


print('''\nExample 2 - in shop cart applications I add multiple
items into cart and then process the shopping cart

cart = [10,20,30,600,70,80] # each item prices
for item in cart :
	if item>500 :
		print("To place this order, insurance must required, we can't proceed further")
		break
	print('processing item:', item)
''')
cart = [10,20,30,600,70,80] # each item prices
for item in cart :
	if item>500 :
		print("To place this order, insurance must required, we can't proceed further")
		break
	print('processing item:', item)

print('''\nExample 3 - If you want use break statement
compulsary you should use it inside loops (same for continue)

x=10
if x > 40 :
	print('We are stopping program execution')
	break
print('Hello')

SyntaxError: 'break' outside loop
''')
