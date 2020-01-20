## Python Data Types
print('\n\nPython Data Types Concept - Tipul datelor')

print('\n1. In Python nu este necesara declararea tipul datelor in mod explicit')
# 10 -> int
a=10
print('\na=10')
print('type(a) -> ', type(a))
# int b = 20 - genereaza erroare
print('\n>>> int b = 20')
print('  File "<stdin>", line 1')
print('    int b = 20')
print('        ^')
print('SyntaxError: invalid syntax')

# 10.5 -> float
# True -> boolean

b=True
print('\nb=',b)
print('type(b) -> ', type(b))

c=10.5
print('\nc=',c)
print('type(c) -> ', type(c))

print('''\n2. In Python tipul datelor este determinat pe baza valoarii atribuite. - Python este Dynamicaly Typed Programming Language''')

print('\n3. Python - 14 in-build Data Types')
print('In Python: int, float, complex, bool, str == IMMUTABLE')
print('In Python: list, tuple, set, frozenset, dict')
print('In Python: byte, bytearray, range, None')

print('\n4. Everyting in Python is an object')
# 10 -> int
a=10
print('\na=',a)

print('\n5. Python in-build functions')
print('tipul obiectului este dat de functia type(a) -> ', type(a))
print('adresa din memorie a obiectului este data de functia id(a) -> ', id(a))
print('print(a) -> ', a)
