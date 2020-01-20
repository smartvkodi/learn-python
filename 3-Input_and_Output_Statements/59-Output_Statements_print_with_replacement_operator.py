# 59 - Output Statements : print(object) and with replacement operator
msg = '59 - Output Statements : print(object) and with replacement operator'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')


print('''1. Output Statements:
print(Object) => we can pass any type of object as argument''')

print('''\nprint(Object) => we can pass a list object
l=[10,20,30,40]
print(l)
# output''')
l=[10,20,30,40]
print(l)

print('''\nprint(Object) => we can pass a tuple object
t=(10,20,30,40)
print(t)
# output''')
t=(10,20,30,40)
print(t)


print('''\n\n2. Output Statements: print with {} replacement operator
# my requirement is to print
Hello Durga, your salary is 10000 and your girlfriend Sunny is waiting.
- there are 3 variables: name, salary and gf''')
print('''
name='Durga'
salary=10000
gf='Sunny'
print( 'Hello {}, Your salary is {} and your girlfriend {} is waiting.'.format(name, salary, gf) )
''')

name='Durga'
salary=10000
gf='Sunny'
print('Hello {}, Your salary is {} and your girlfriend {} is waiting.'.format(name, salary, gf))

print('''\n# we can specify the indexes into placeholders, too - there are 3 variables: name, salary and gf''')
print("print( 'Hello {0}, Your salary is {1} and your girlfriend {2} is waiting.'.format(name, salary, gf) )")
print('Hello {0}, Your salary is {1} and your girlfriend {2} is waiting.'.format(name, salary, gf))

print('''\n# If by mistake we change the order into format, then print will not function as we expected''')
print("print( 'Hello {1}, Your salary is {2} and your girlfriend {0} is waiting.'.format(name, salary, gf) )")
print( 'Hello {1}, Your salary is {2} and your girlfriend {0} is waiting.'.format(name, salary, gf) )

print('''\n# Why should I remember the order, indexes? 
We can define keywords arguments, then the order is not important!''')
print("print( 'Hello {n}, Your salary is {s} and your girlfriend {f} is waiting.'.format(n=name, s=salary, f=gf) )")
print( 'Hello {n}, Your salary is {s} and your girlfriend {f} is waiting.'.format(s=salary, f=gf, n=name) )

print('''\n#Another example:
a,b,c,d=10,20,30,40
I want to print
a=10, b=20, c=30, d=40

print( 'a={}, b={}, c={}, d={}'.format(a,b,c,d) )''')
a,b,c,d=10,20,30,40
print( 'a={}, b={}, c={}, d={}'.format(a,b,c,d) )
