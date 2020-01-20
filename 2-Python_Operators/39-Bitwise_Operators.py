# 39 - Bitwise Operators: &,|,^
print('\n')
msg = '39 - Bitwise Operators: & , | , ^ , ~ , << , >>'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''- Bitwise Operators: 
\t- & -> bitwise and
\t- | -> bitwise or
\t- ^ -> bitwise x-or
\t- ~ -> bitwise complement oprerator
\t- << -> bitwise left-shift operatort
\t- >> -> biwise right-shift operator''')
print('we can can apply bitwise operators only for int an bool data-types')

print('* 10.5 & 20.6 => TypeError: unsupported operand type(s) for &: \'float\' and \'float\'' )
print('* \'durga\' & \'durga\' => TypeError: unsupported operand type(s) for &: \'str\' and \'str\'')
print('* 10 & 20 = ', 10 & 20)
print('* True & False = ', True & False)

print('''\n 4 & 5 ?
\t\t100
\t\t101
\t\t----
\t\t100''')

print('''\n1. x & y - if both bits are 1 then result is 1 otherwise the result is 0''')
print('''\n2. x | y - if at least one bit is 1 then result is 1 otherwise the result is 0''')
print('''\n3. x ^ y - if both bits are different then result is 1 otherwise the result is 0''')

print('4 & 5 #', 4 & 5) # 100 -> 4
print('4 | 5 #', 4 | 5) # 101 -> 5
print('4 ^ 5 #', 4 ^ 5) # 001 -> 1
