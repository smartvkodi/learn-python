# 61 - Introduction and Indentation
msg = '61 - Introduction and Indentation'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')


print('''In Python there are 3 categories of flow-control statements:
	1. Selection statements:
		# if
		# if-else
		# if-elif-elese
		# if-elif
	2. Iterative statements:
		# for
		# while
	3. Transfer statements:
		# break
		# continue
		# pass
# pass & del statements ''')

print('''\n#In Python some flow-control statements are not available
	# switch
	# do-while
	# go-to''')

print('''\n#In Python there is the indentention concept
# in Java using the {} we can define the statements blocks
	if(c)
	{
		body/action
	}
	statement

# in Python the statements block are defined by ':' and identention
if condition: # (condition) the paranthesis are optional
	statement-1		\ 
	statement-2		 --  same identition (are under if condition)
	statement-3		/
statement4 - has different indetention (it is out of if condition) 

IdententionError !! If we not maintain the right identention we will get the error.''')
