# 53-eval()_function
msg = '53-eval()_function'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('## eval(x) is an alternative of data-type casting')

print('''\n## x = input('Enter something') 
print(x, type(x))\n''')
x = input('Enter something: ') 
print(x, type(x))


print('''\n## but x = eval(input('Enter something'))
print(x, type(x))\n''')
x = eval(input('Enter something: '))
print(x, type(x))

print('''\n## the important speciality of eval is to evaluate
the expersions eval(expression))
x = eval('10+20+30') => x = 60 ''')
x = eval('10+20+30')
print('x=',x, type(x))


