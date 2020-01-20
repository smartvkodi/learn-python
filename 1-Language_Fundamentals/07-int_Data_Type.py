## int Data_Type - Integral Values (Whole Numbers)
print('\n\nPython - Tipul de date intreg - int')

a=10
print('\na=10')
print('type(a) -> ', type(a))

print('\n\nPython - pentru numere intregi foarte mari -> long doar in python 2.x')
print('In Python 3.x - long nu este disponibil - pt numerele foarte mari se foloseste tipul int')

print('\nTipul de date intregi (int) in diferite formate')
print('\n - format zecimal 0-9 - baza 10 == Default Format')
a=1111
print('a=',a)

print('\n - format binar 0-1 - baza 2 - prefixat cu 0b / 0B')
a=0b1111
print('a=0b1111 ->',a)
c=0B1011
print('c=0B1011 ->',c)

print('\n - format octal - 0-7 - baza 8 - prefixat cu 0o / 0O')
a=0o123
print('a=0o123 ->',a)
c=0O11
print('c=0O11 ->',c)

print('\n - format hexa-decimal - 0-9 + A,B,C,D,E,F - baza 16 prefixat cu 0x / 0X')
a=0x1f
print('a=0x1f ->',a)
c=0X2A
print('c=0X2A ->',c)
face=0XFace
print('face=0XFace ->',face)
beef=0xBEEF
print('beef=0xBEEF ->',beef)
