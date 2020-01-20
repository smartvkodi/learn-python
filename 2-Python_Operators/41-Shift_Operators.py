# 41 - Shift Operators:<< and >>
print('\n')
msg = '41 - Shift Operators:<< and >>'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n- Shift Operators: 
\t- << -> bitwise left-shift operator
\t- >> -> biwise right-shift operator''')

print('''\n- Left Shift Operator:  x<<2''')
print('10<<2 -> ', 10<<2)
print('''10 ->
0b0000...01010 - lefting shift with 2 positions
  0b00...0101000 -> 40''')

print('''\n- Right Shift Operator:  x>>2''')
print('10>>2 -> ', 10>>2)
print('''10 -> positive number -> sign bit is 0
  0000...01010 - right shift with 2 positions
  000000...010 -> 2''')

print('\nTrue<<2 =>',True<<2)
print('True>>2 =>',True>>2)