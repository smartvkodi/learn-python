# 93 - Mathematical, Membership and Comparison Operators for Strings
msg = '93 - Mathematical, Membership and Comparison Operators for Strings'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. Mathematical Operator "+" for str -> for concatenation''')

print(''''durga' + 'soft' => {}'''.format('durga' + 'soft'))

print('''\n### if you want aply + operator for the strings
compulsatory both arguments should be in string type only
''')
print("'durga' + 10 =>", 'TypeError: can only concatenate str (not "int") to str')
print("'durga' + 20.0 =>", 'TypeError: can only concatenate str (not "float") to str')
print("'durga' + True =>", 'TypeError: can only concatenate str (not "bool") to str')

print('''\n2. Mathematical Operators "*" for str -> for multiplication / repetition''')