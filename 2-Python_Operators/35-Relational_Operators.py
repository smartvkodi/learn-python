# 35 - Relational Operators
print('\n')
msg = '35 - Relational Operators'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''- Relational Operators: > , >= , < , <= ''')

print('''\n1. Relational Operators are applicable for numbers''')
print('''a=10
b=20''')
a=10
b=20
print('a<b #', a<b) # True
print('a<=b #', a<=b) # True
print('a>b #', a>b) # False
print('a>=b #', a>=b) # False


print('''\n2. Relational Operators are applicable for strings, too
String comparison will be happend based on alphabethical order,
based on unicode values (ASCII code)''')

print('''\nWhich is the UNICODE of a charachter? 
- use build-in function") ord and chr build-in functions''')
print("\n# unicode 'a' = ord('a') = ",  ord('a'))
print("the character with unicode 97? chr(97) =", chr(97))

print("\n# unicode 'b' = ord('b') = ", ord('b'))
print("the character with unicode 98? chr(98) =", chr(98))

print("\nWhich is the UNICODE of a charachter? use build-in function")
print("\# unicode 'A' = ord('A') = ",  ord('A'))
print("# unicode 'B' = ord('B') = ", ord('B'))


print("\String comparison examples:")

s1='durga'
s2='sunny'
print(s1,' < ', s2, '#', s1 < s2) # True
print(s1,' <= ', s2, '#', s1 <= s2) # True
print(s1,' > ', s2, '#', s1 > s2) # False
print(s1,' >= ', s2, '#', s1 >= s2) # False

s1='durga'
s2='durga'
print(s1,' < ', s2, '#', s1 < s2) # False
print(s1,' <= ', s2, '#', s1 <= s2) # True
print(s1,' > ', s2, '#', s1 > s2) # False
print(s1,' >= ', s2, '#', s1 >= s2) # True

s1='durga'
s2='Durga'
print(s1,' < ', s2, '#', s1 < s2) # False
print(s1,' <= ',s2, '#', s2, s1 <= s2) # False
print(s1,' > ',s2, '#', s2, s1 > s2) # True
print(s1,' >= ',s2, '#', s2, s1 >= s2) # True

print('''\n3. Relational Operators are applicable for boolean
Boolean comparison will be happend based on coresponding int values
True -> 1
False -> 0''')

s1=True
s2=False
print(s1,' > ', s2, '#', s1 > s2) # True
print(s1,' >= ', s2, '#', s1 <= s2) # True
print(s1,' < ', s2, '#', s1 > s2) # False
print(s1,' <= ', s2, '#', s1 >= s2) # False

print('''\n4. Sometimes comparability is not applicable
when the arguments are different in types''')

s1=10
s2='durga'
print(s1,' < ', s2, '#', "TypeError: '<' not supported between instances of 'int' and 'str'")
print(s1,' <= ', s2, '#', "TypeError: '<=' not supported between instances of 'int' and 'str'")
print(s1,' > ', s2, '#', "TypeError: '>' not supported between instances of 'int' and 'str'")
print(s1,' >= ', s2, '#', "TypeError: '>=' not supported between instances of 'int' and 'str'")

print('''\n5. Relational Operators into conditional statement''')
print('''a=10
b=20
if a>b :
	print('a is greater than b')
else:
	print('a is not greater than b')''')
a=10
b=20
if a>b :
	print('\na is greater than b')
else:
	print('\na is not greater than b') # this is the answer wil be printed

print('''\n6. Chaining Relational Operators ''')
print('''10 <20 # True
10<20<30 # True
10<20<30<40 # True
10<20<30<40>50 # False

If all comparisons returns True htan the result is True
If at least one comparison returns Fals than the result is False''')
print('10<20<30 #', 10<20<30)
print('10<20<30<40 #',10<20<30<40)
print('10<20<30<40>50 #', 10<20<30<40>50)

