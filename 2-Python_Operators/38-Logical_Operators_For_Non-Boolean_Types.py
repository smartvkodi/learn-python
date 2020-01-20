# 38 - Logical Operators For Non-Boolean Types
print('\n')
msg = '38 - Logical Operators For Non-Boolean Types'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''- Logical Operators For Non-Boolean Types: and, or, not ''')

print('''\n- 0 means False / non-zero means True
- empty string, list, tuple, set, dict  means False''')

print('''\n1. x and y - result is x | y !but not boolean type
- if x evaluats to False, than result is x
- if x evaluats to True, then result is y''')

print('10 and 20 #', 10 and 20) # 20
print('0 and 20 #', 0 and 20) # 0
print('\'durga\' and \'soft\' #', 'durga' and 'soft') # 'soft'
print('\'\' and \'soft\' #', '' and 'soft') # ''

print('''\n2. x or y - result is x | y !but not boolean
- if x evaluats to True, than result is x
- if x evaluats to False, then result is y''')

print('10 or 20 #', 10 or 20) # 10
print('0 or 20 #', 0 or 20) # 20
print('[] or \'durga\' #', [] or 'durga') # 'durga'
print('\'durga\' or \'soft\' #', 'durga' or 'soft') # 'durga'
print('\'\' and \'soft\' #', '' or 'soft') # 'soft'


print('''\n3. not - For Non-Boolean Types => result is boolean''')

print('not \'durga\' #', not 'druga') # False
print('not \'\' #', not '') # True
print('not 0 #', not 0) # True
print('not 10 #', not 10) # False 

