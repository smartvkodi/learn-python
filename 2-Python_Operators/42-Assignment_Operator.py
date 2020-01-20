# 42 - Assignment Operators
print('\n')
msg = '42 - Assignment Operators'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('\n- Assignment Operator: x = 10')

print('''\n- Compound Assignment Operator:
	x = 10
	x += 20 <=> x = x + 20
	x = 30''')

print('''\n- Compound Assignment Operators:
\t- += -> plus-equal
\t- -= -> minus-equal
\t- *= -> multiply-equal
\t- /= -> division-equal
\t- %= -> modulo-equal
\t- //= -> fool-division-equal
\t- **= -> exponential-power-equal
\t- &= -> bitwise-and-equal
\t- |= -> bitwise-or-equal
\t- ^= -> bitwise-xor-equal
\t- >>= -> bitwise-left-shift-equal
\t- <<= -> bitwise-right-shift-equal
''')
print('\nExamples:')
print('''\nx = 10
x &= 5 => ?''')
x =10
x&=5
print('x &= 5 =>', x)
print('''
10	-> 000...01010
5	-> 000...00101
10&5	-> 000...00000 => 0''')

x =10
x**=2
print('''\nx = 10
x **= 2 <=> x = x ** 2 <=> x= ''', x)

print('''\nx=10
x++  => SyntaxError: invalid syntax''')
print('''\nx=10
x--  => SyntaxError: invalid syntax''')

x=10
print('''\nx=10
++x  => ''',  ++x)
print('''\nx=10
--x=''', --x,
'''---x=''', ---x,
'''----x=''', ----x)

