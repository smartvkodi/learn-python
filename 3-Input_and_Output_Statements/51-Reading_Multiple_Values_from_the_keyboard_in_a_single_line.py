# 51 - Reading Multiple Values from the keyboard in a single line
msg = '51 - Reading Multiple Values from the keyboard in a single line'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''1. How to read multiple values from the keyboard in a single line:''')

print('''#List Comprehension Concept: [int(x) for x in input('Enter 2 Numbers:').split())]''')
print('''#List Unpacking Concept: a,b = [int(x) for x in input('Enter 2 Numbers:').split()]''')
print('')
a,b = [ int(x) for x in input('Enter 2 Numbers:').split() ]
print('The Sum:', a+b)

print('\nExplaining...')
print("#s = input('Enter 2 Numbers:')")
s = input('Enter 2 Numbers:')
print('s =', s, type(s))
print('\nl = s.split() => split() returns a list')
l = s.split()
print('l=', l)

print('\n## List Comprehension Concept')
print('l1 = [int(x) for x in l] ## for each x in list l perform type cast into int type')
l1 = [int(x) for x in l] ## for each x in list l perform type cast into int type
print('l1=',l1)

print('\n## List Unpacking Concept')
print('a,b = l1')
a,b = l1
print('a=', a, 'b=',b)
print('The sum:', a+b)
