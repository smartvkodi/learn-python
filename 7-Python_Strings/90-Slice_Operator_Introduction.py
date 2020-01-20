# 90 - Slice Operator Introduction
msg = '90 - Slice Operator Introduction'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. How to access characters of String?
## by using Slice
''')
print('''By Using Slice
## to get substrings from a givent string
- slice operator contains 3 arguments: s[begin : end : step]

# 'step' is optional
s[begin : end] -> return an substring from 'begin' index to 'end-1' index'

# 'begin' index is optional & default value is 0
# 'end' index is optional & default value len(s) - last character

Examples:
	s='abcdefghijk'
	s[2:7] = 'cdefg'		s[2:] = 'cdefghijk'
	s[:7] = 'abcdefg'		s[:] => total string
''')
s='abcdefghijk'
print('s[2:7] = {}\t\t s[2:] = {}'.format(s[2:7], s[2:] ))
print('s[:7] = {}\t\t s[:] = {}'.format(s[:7], s[:]))

print('''\n\nBy Using Slice
## to get substrings from a givent string
- slice operator contains 3 arguments: s[begin : end : step]
- default value for 'step' is 1
			- if step = 0 => ValueError

Examples:
	s='abcdefghijk'
	s[2:7:1] = 'cdefg'		s[2::3] = 'cfi'
	s[2:7:2] = 'ceg'		s[::4] ='aei'
''')
s='abcdefghijk'
print('s[2:7:1] = {}\t s[2::3] = {}'.format(s[2:7:1], s[2::3] ))
print('s[2:7:2] = {}\t\t s[::4] = {}'.format(s[2:7:2], s[::4]))
