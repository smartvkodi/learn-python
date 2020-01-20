# 91 - Slice Operator Rules
msg = '91 - Slice Operator Rules'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Slice Operator Rules
## to get substrings from a givent string
- slice operator contains 3 arguments: s[begin : end : step]

# 'step' is optional
s[begin : end] -> return an substring from 'begin' index to 'end-1' index'

# 'begin' index is optional & default value is 0
# 'end' index is optional & default value len(s) - last character
''')

print('''\nBy Slice Operator Rules - the indexes may be either positive or negative
# slice operator contains 3 arguments: s[begin : end : step]

# step either positive or negative:
	- step is positive -> Left to Right [Forward direction] from 'begin' to 'end-1'
	- step is negative => Right to Left [Backword direction] from 'begin' to 'end+1'
	- if step = 0 => ValueError

# NOTES:
	*** in 'Forward direction' if 'end' = 0 -> result is always empty
	*** in 'Backward direction' if 'end' = -1 -> result is always empty

*** default values in 'Forward direction' 
	- 'begin' = 0 and 'end' = len(s)

*** default values in 'Backward direction' 
	- 'begin' = -1 and 'end' = -(len(s)+1)
''')
