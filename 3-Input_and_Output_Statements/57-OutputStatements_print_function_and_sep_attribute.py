# 57 - Output Statements : print() function and sep attribute
msg = '57 - Output Statements : print() function and sep attribute'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Output Statements: new line '\\n'
print('durga')
print()
print('soft') 
- statement without any argument will print an blank line''')
print('durga')
print()
print('soft')

print('''\n2. Output Statements: str argument with escape characters
- print(String) and combinations of str operators''')
print('durga')
print('durga\nsoftware')
print('durga\tsoftware')
print('durga' + 'software')
print(5*'durga' +'\t' + 'software')


print('''\n3. Output Statements: variable number of str argument''')
print('''a,b,c = 10,20,30
print('Values are:',a,b,c,d) # the spaces will automatical inserted ''')
a,b,c=10,20,30
print('Values are:',a,b,c)

print('''\n4. Output Statements: with sep attribute => separator character''')
print('''a,b,c,d = 10,20,30,40
print(a,b,c) # the default separator 'space' will automatical inserted ''')
a,b,c,d = 10,20,30,40
print(a,b,c,d)

print('''\n# I want the separator to be ':' as the result: 10:20:30:40
we should use print(a,b,c,d,sep=':')''')
print(a,b,c,d,sep=':')

print('''\n# I want the separator to be '--' as the result: 10--20--30--40
we should use print(a,b,c,d,sep='--')''')
print(a,b,c,d,sep='--')
