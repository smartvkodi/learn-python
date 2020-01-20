# 89 - How to access characters of String and application
msg = '89 - How to access characters of String and application'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. How to access characters of String?
## by ising Index
## by using Slice
''')
print('''By Using Index
## Python support both positive and negative index
- positive index from 0 to n -> forward direction : left to right
- negative index from -1 to -n -> backward direction : right to left

s = 'durga': s[0] -> 'd' and s[-1] -> 'a'
but s[100] -> IndexError: string index out of range
''')

print('''\nApplication: Write a program to display characters of given
string index wise (both positive and negative)

s = 'durga'
# output should be like this:
The character present at +ve index: 0 and at -ve index: -5 is: d
The character present at +ve index: 1 and at -ve index: -4 is: u
The character present at +ve index: 2 and at -ve index: -3 is: r
The character present at +ve index: 3 and at -ve index: -2 is: g
The character present at +ve index: 4 and at -ve index: -1 is: a

s = input('Enter some string: ')
i=0
for x in s:
	print('The character present at +ve index: {} and at -ve index: {} is: {}'.format(i, i-len(s), x))
	i+=1
''')

s = input('Enter some string: ')
i=0
for x in s:
	print('The character present at +ve index: {} and at -ve index: {} is: {}'.format(i, i-len(s), x))
	i+=1

