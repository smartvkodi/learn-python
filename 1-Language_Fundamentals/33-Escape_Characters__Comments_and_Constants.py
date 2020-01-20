# 33 - Escape Characters, Comments and Constants
print('\n')
msg = '33 - Escape Characters, Comments and Constants'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('\n1. Escape Characters - the characters which have special functionality')

print('\\n => new line')
print('\\t => horizontal tab')
print('\\r => carriage return - moves cursor at the begining of current line')
print('\\b => back space - the character will be deleted')
print('\\f => form feed')
print('\\\' => single qoute')
print('\\" => double qoute')
print('\\\\ => back slash character')


print('\n2. Comments - commented line won\'t be executed by PVM')

# print(This is a comment won't be executed by PVM)
print('# => single line comment')
print('# line 1')
print('# line 2')
print('# line 3')

print('\n\'\'\' multi lines \'\'\' - this is not multiline comment this is documentation string')


print('\n3. Constants - this concept is not available in Python')
print('''\n- In Python modifiers concept is not applicable, 
There is no way to define constants but there is a convention
If you won't change the value, by convention, you can define 
the variable name in uppercase\n''')

MAX_LENGHT = 10
print('MAX_LENGHT =', MAX_LENGHT, '- by convention that is an constant even we can modify the value')
MAX_LENGHT = 20
print('MAX_LENGHT =', MAX_LENGHT, '- the modified value')