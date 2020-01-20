# 81 - Loops with else block
msg = '81 - Loops with else block'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Other Python specific syntax 
# else - can be used in this situations too 
- for-else-loop
- while-else-loop
- try - except - else - finally <= exception handling
''')

print('''\nWhen the Python's else-loops are useful?
If the loop has been executed successfuly without break and you 
want to do any 'activity' immediatly after the loop finished
execution, you have to define that 'activity' inside 'else' part
''')

print('''\nExample 1:
cart = [10,20,30,40,50] # each item prices
for item in cart :
	if item>500 :
		print("Insurance must be required, we can not place this order")
		break
		## continue is not meaningful for else
	print('processing item:', item)
else:
	print("Congratulations, all items processed successfuly')

print('that is it!')

## the output''')
cart = [10,20,30,600,40,50] # each item prices
for item in cart :
	if item>500 :
		print("Insurance must be required, we can not place this order")
		break
		# but continue is not meaningful for else
	print('processing item:', item)
else: ## the for loop has been executed without break
	print('Congratulations, all items processed successfuly')

print('That is all!')