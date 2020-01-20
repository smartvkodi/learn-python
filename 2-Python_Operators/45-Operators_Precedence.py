# 45 - Operators Precedence
print('\n')
msg = '45 - Operators Precedence'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')


print('10 + 2 * 3 =', 10 + 2 * 3) # 16
print('(10 + 2) * 3 =', (10 + 2) * 3) # 36

print('''\n#Example:
a=30
b=20
c=10
d=5''')
a=30
b=20
c=10
d=5
print('(a+b)*c/d = ',(a+b)*c/d ) # 100.0
print('(a+b)*(c/d) = ',(a+b)*(c/d) ) # 100.0
print('a+(b*c)/d = ', a+(b*c)/d ) # 70.0

print('''\n#Example:
3/2*4+3+(10/5)**3-2 =''', 3/2*4+3+(10/5)**3-2) # 15.0

