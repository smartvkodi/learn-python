# 40 - Bitwise Complement Operator(~)
print('\n')
msg = '0 - Bitwise Complement Operator(~)'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('~4 = ', ~4)

print('''\n ~4 ?
\t * the most segnificant bit (MSB) acts as sign bit
\t    0 -> +ve number
\t    1 -> -ve number
\t * +ve numbers will be represented directly in the memory
\t * -ve numbers will be represented in 2's complement form
\t * 1's complement - flipping the bits: 0 <-> 1
\t * 2's complement - 1's complement + 1

\t  4 ->		00000...0100
\t ~4       	11111...1011
\t 1's compl	 0000...0100 + 1
\t 2's compl	 0000...0101 => -5''')

print('\n~-23 = ', ~-23)
print('''-23	1+ the rest in 2's complemet form
23	 000...10111
1compl	 111...01000 +1
2compl	 111...01001
-23	1111...01001
~-23	0000...10110''')
print('\t0b10110 ->', 0b10110)


print('\n~-357 =', ~-357)	
print('''-357	1+ the rest in 2's complemet form
357	 000...101100101
1compl	 111...010011010 + 1
2compl	 111...010011011
-357	1111...010011011
~-357	0000...101100100''')
print('\t0b101100100 ->', 0b101100100)


print('\n~1971 =', ~1971)	
print('''1971	0000...11110110011
~1971	1111...00001001100
1compl	 000...11110110011 +1
2compl	 000...11110110100''')
print('\t0b11110110100 ->', 0b11110110100)






