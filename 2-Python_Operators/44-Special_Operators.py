# 44 - Special Operators:Identity & Membership Operators
print('\n')
msg = '44 - Special Operators:Identity & Membership Operators'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\nSpecial Operators:
	1. Identity Operators;
	2. Membership Operators''')

print('''\n1. Identity Operators:
\na. 'is' operator 
r1 is r2 => True if only if both refrences pointing same object
\nb. 'is not' operator
r1 is not r2 => True if only if both r1 and r2 are not pointing to the same object''')

print('''\n#Example: int - object reusability is applicable
a=10
b=10''')
a=10
b=10
print('a is b =>', a is b) # True
print('a is not b =>', a is not b) # False

print('''\n#Example: str - object reusability is applicable
a='durga'
b='durga' ''')
a='durga'
b='durga'
print('id(a) ->',id(a))
print('id(b) ->',id(b))
print('a is b =>', a is b) # True
print('a is not b =>', a is not b) # False

print('''\n#Example: complex - object reusability IS applicable
a=10+20j
b=10+20j ''')
a=10+20j
b=10+20j
print('id(a) ->',id(a))
print('id(b) ->',id(b))
print('a is b =>', a is b) # True
print('a is not b =>', a is not b) # False

print('''\n#Example: list - object reusability NOT is applicable
l1=[10,20,30,40]
l2=[10,20,30,40] ''')
l1=[10,20,30,40]
l2=[10,20,30,40]
print('id(l1) ->',id(l1))
print('id(l2) ->',id(l2))
print('l1 is l2 =>', l1 is l2) # False
print('l1 is not l2 =>', l1 is not l2) # True

print('\n# for content comparison only -> l1 == l2 =>', l1 == l2) # True
print('is operator is for \'refrence comparison\' only - address comparison')
print('if I want content comparison only then we require == operator')

print('''\n\n2. Membership Operators: to check if one object is present of an collection
\na. 'in' operator 
a in sequence => True if only if a is present in that sequence/collection
\nb. 'not in' operator
a not in sequence => True if only if a is NOT present in that sequence/collection''')

print('''\n#Example: str - object is member of string
s='hello learning python is very easy' ''')
s='hello learning python is very easy'
print('\'h\' in s =>', 'h' in s) # True
print('\'d\' in s =>', 'd' in s) # False
print('\'d\' not in s =>', 'd' not in s) # True
print('\'python\' in s =>', 'python' in s) # True
print('\'Python\' in s =>', 'Python' in s, '#because Python is case-sensitive') # False

print('''\n#Example: string - object is member of list
l=['sunny','bunny','chinny','vinny']''')

l=['sunny','bunny','chinny','vinny']
print('\'sunny\' in l ->', 'sunny' in l) # True
print('\'pinny\' in l ->', 'pinny' in l) # False
print('\'pinny\' not in l ->', 'pinny' not in l) # True
