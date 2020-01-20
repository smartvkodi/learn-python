# str - String Data Type - 
print('\n\nPython - Tipul de date String str')
print('\n\n1. Orice secventa de caractere reprezinta un string')

s = 'durga'
print("s = 'durga' ", type(s))
# sau 
s = "durga"
print('s = "durga"', type(s))


print('\n\n2. Atentie la ghilimelele simple si duble (caracterele escape)')
s = 'a'
print('s = \'a\' un singur caracter este de tipul', type(s))
s = "a"
print('s = \"a\" un singur caracter este de tipul', type(s))


print('\n\n3. In Python exista  \'\'\' su \"\"\" - triple qoutes')

print('\n3a. Pentru a defini multi-line string literals\n')
s = '''durga
software
solutions'''

### sau 3 x "

s = """durga
software
solutions"""
print('multiline string literal', s)
print(type(s))

print('\n3b. Pentru a include in stringul definit caractere \' si \"')
## cum definim un string s = 'class by 'durga' is very good'
s = "class by 'durga' is very good"
print(s) # sau
s = 'class by "durga" is very good' 
print(s) # sau
s = '''classes by 'durga' for "Python" are very good'''
print(s)

print('\n3c. Documentation string - pentru a defini doc string')
'''
documentation string
'''


