# 60 - Output Statements : print() with formatted string
msg = '60 - Output Statements : print() with formatted string'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')


print('''Output Statements print() with formatted string: 
# %i --> signed decimal value
# %d --> signed decimal value
# %f --> floating point value
# %s --> string, any other objects like list, set, etc...''')

print('\n#Example-1')
print('''a=10
print('a value: %i' %a)
print('formatted_string' %(variable_list))
# output''')
a=10
print('a value: %i' %a)

print('\n#Example-2')
print('''a=10
b=20
c=30
print('a=%d, b=%f, c=%d' %(a,b,c))
# output''')
a=10
b=20
c=30
print('a=%d, b=%f, c=%d' %(a,b,c))

print('\n#Example-3')
print('''name='Durga'
marks=[10,20,30,40]
name is str, marks is list then the specified format required is %s
print('Hello %s, your marks list: %s' %(name, marks))
# output''')
name='Durga'
marks=[10,20,30,40]
print('Hello %s, your marks list: %s' %(name, marks))


print('\n#Formatted string is more powerfull than replacement operator {}')
print('''price = 70.56789
print('Price value={}'.format(price))
print('Price value=%f' %price)
# output''')
price = 70.56789
print('Price value={}'.format(price)) # with replacement operator
print('Price value=%f' %price) # with formated string

print('''\n#the biggest advantage using formatted string is when 
I do not want displaying all decimals but only 2 decimals
print('Price value=%.2f' %price)''')
print('Price value=%.2f' %price)



