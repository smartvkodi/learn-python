# str - Plus & Star Operator in String Data Type - str
print('\n','*'*3,'Plus & Star Operator in String Data Type str','*'*3)
print('*'*3,'Operatii matematice: + si * cu string-uri')


print('\n1. Operatorul + pe str (Adunare / Concatenare String-uri)')
print(' \'druga\' + \'soft\' => ', 'druga' + 'soft')

print('\ndar daca vreau sa concatenez un string cu un intreg')
# s = 'druga' + 10
print('''s = \'druga\' + 10 => in Python da eroare!
TypeError: can only concatenate str (not "int") to str' 
- + functioneaza doar daca ambele argumente sunt str''')
print('! In Java operatia este valida: "druga" + 10 = "durga10"')


print('\n2. Operatorul * pe str (Multiplicare / Repetare String-uri)')
print(' - s = \'druga\' * 3 => s = \'', 'druga'*3, '\'')
print(' - 4 * \'druga|\' => s=\'', 4 * 'druga|', '\'')

print(''' - s = 'druga' * 'soft' => da eroare!
! TypeError: can't multiply sequence by non-int of type 'str'
- * functioneaza doar daca multiplicam str cu int''')

print('\n')
msg = 'PCHUPS SOFT SOLUTIONS'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('\n3. Concluzii Importante')
print('\n3.1. Tipuri de date fundamentale in Python')
print('''- int => numere intregi
- float => numere reale in virgula mobila
- complex => numere complexe z = 10 + 20j
- bool => True sau False
- str => siruri de caractere''')
print('''\n3.2. Tipul de date long pentru numere reale 
- este disponibil doar in Python 2.x
- in Python 3.x long este inclus in tipul de date int''')
print('''\n3.3. Tipul de date char nu exista in Python 
- tipul char -> un singur caracter poate fi reprezentat
folosind tipul de date 'str' ''')







