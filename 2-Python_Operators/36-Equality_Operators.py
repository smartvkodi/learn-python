# 36 - Equality Operators
print('\n')
msg = '36 - Equality Operators'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''- Equality Operators: == , != ''')

print('''\n1. Equality Operators are applicable for numbers''')
print('''a=10
b=20''')
a=10
b=20
print('a==b #', a==b) # False
print('a!=b #', a!=b) # True
print('10==10.0 #', 10==10.0) # True


print('''\n2. Equality Operators are applicable for strings, too
String comparison will be happend based on alphabethical order,
based on unicode values (ASCII code)''')

s1='durga'
s2='sunny'
print(s1,' == ', s2, '#', s1 == s2) # True
print(s1,' != ', s2, '#', s1 != s2) # True

s1='durga'
s2='durga'
print(s1,' == ', s2, '#', s1 == s2) # True
print(s1,' != ', s2, '#', s1 != s2) # False


print('''\n3. Equality Operators are applicable for boolean, too
Boolean comparison will be happend based on coresponding int values
True -> 1
False -> 0''')

s1=True
s2=False
print(s1,' == ', s2, '#', s1 == s2) # False
print(s1,' != ', s2, '#', s1 != s2) # True
print(s1,' == ', 1, '#', s1 == 1) # True
print(s1,' != ', 0, '#', s1 != 0) # True


print('''\n4. Equality Operators is always applicable
even when the arguments are different in types''')

s1=10
s2='durga'
print(s1,' == ', s2, s1 == s2)
print(s1,' != ', s2, s1 != s2)


print('''\n5. Relational Operators into conditional statement''')
print('''a=10
b=20
if a==b :
	print('a is equal with b')
else:
	print('a is not equal with b')''')
a=10
b=20
if a==b :
	print('resut: a is equal with b')
else:
	print('result: a is not equal with b') # this is the answer wil be printed

print('''\n6. Chaining Equality Operators''')

print('''If all comparisons returns True, then the result is True
If at least one comparison returns False, then the result is False''')
print('10!=20!=30 #', 10!=20!=30)
print('10!=20!=30==40 #', 10!=20!=30==40)


print('''\n6. Difference between '==' and 'is' operator ''')

print('is operator- Reference comparison or Address comparison')
print('== operator- Content comparison\n')

print('''l1=[10,20,30]
l2=[10,20,30]''')
l1=[10,20,30]
l2=[10,20,30]
print('id(l1): ', id(l1))
print('id(l2): ', id(l2))
print('l1 is l2', l1 is l2) # False - addresses are diferent
print('l1 == l2', l1 == l2) # True - the content is the same

l3=l1
print('\nl3 = l1')
print('id(l1): ', id(l1))
print('id(l3): ', id(l3))
print('l1 is l3', l1 is l3) # True - both are pointing to same object

