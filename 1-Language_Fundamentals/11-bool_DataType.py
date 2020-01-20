# bool Data Type - 
print('\n\nPython - Tipul de date bool')
print('\n\n1. In Python valorile booleane sunt True si False')

b = True
print(b, ' -> ', type(b))
b = False
print(b, ' -> ', type(b))

print('\n\n2. Variabilelor le pot fi atribuite si valorile expresiilor logice')
a=10
print('a =',a)
b=20
print('b =',b)
c=a>b
print('c = a>b => c = ', c, ' type(c) -> ', type(c))

print('\n\n3. Operatii aritmetice cu valori boolene:')
print('Intern valorile boolene sunt reprezentate ca intregi')
print('True -> 1 si False -> 0')
print('\nCat face print(True + True) = ? \t rezultat: ', True + True)
print('Cat face print(True - False) = ? \t rezultat: ', True - False)
print('Cat face print(True * False) = ? \t rezultat: ', True * False)
# Atentie la impartirea cu 0
print('Cat face print(True / False) = ? \t rezultat: ', True / False)
