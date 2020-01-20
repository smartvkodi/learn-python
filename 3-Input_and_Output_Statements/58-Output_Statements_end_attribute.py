# 58 - Output Statements : end attribute
msg = '58 - Output Statements : end attribute'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')


print('''1. Output Statements: print with 'end' attribute''')
print('''print('hello') => \\n automaticaly is added
print('durga') => \\n automaticaly is added
print('soft') => \\n automaticaly is added
# output''')
print('hello')
print('durga')
print('soft')

print('''\n# But if I want to print into a single line
as: hellodurgasoft  I should use the 'end' attribute
print('hello', end='')
print('durga', end='')
print('soft', end='')
# output''')
print('hello', end='')
print('durga', end='')
print('soft', end='')

print('''\n\n# But I can define the 'end' attribute as I wish
to get: hello::durga$$$soft
print('hello', end='::')
print('durga', end='***')
print('soft')
# output''')
print('hello', end='::')
print('durga', end='$$$')
print('soft')

print('''\n\n# I can define the 'sep' and 'end' attribute as I wish
print(10,20,30,sep=':', end='***')
print(40,50,60,sep=':')
print(70,80,sep='**', end='$$')
print(90,100)
# output''')
print(10,20,30,sep=':', end='***')
print(40,50,60,sep=':')
print(70,80,sep='**', end='$$')
print(90,100)


print('''\n\n# Difference between
print('durga' + 'software') # string concatenation
print('durga', 'software') # 2 arguments with default separator ' ' space
# output''')
print('durga' + 'software') # durgasoftware
print('durga', 'software') # durga software



