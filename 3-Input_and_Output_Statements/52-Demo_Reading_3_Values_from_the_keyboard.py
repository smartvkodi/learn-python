# 52 - Demo Reading 3 Values from the keyboard
msg = '52 - Demo Reading 3 Values from the keyboard'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('## str split() function')
print('## List Comprehension Concept')
print('## float type casting')
print('## List Unpacking Concept')

print('''\n## Write a program to read 3 float values from 
the keyboard separated by ',' and then print the sum\n''')

a,b,c = [ float(x) for x in input('Enter 3 Float Numbers separated by \',\': ').split(',') ]
print('The Sum:', a+b+c)


