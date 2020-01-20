# Identificatory in Python 
#
print('\n 1. In Python identificam variabile / clasele / metodele -> dupa numele variabilelor')

a = 10
# a = 10 este numele variabilei si este este identificator de variabilei

#class Test:
	#
	#
# Test este identificatorul clasei


print('\n2. Reguli pentru definirea / crearea identificarilor Python')

# caractere accetabile pentru numele variabilelor:  a-z / A-Z / 0-9 / _
cash = 10
print('cash = ', cash)
#ca$h = 20 # syntax error <- identifier cannot contains $
#my@home = 'acasa' # syntax error <-  identifier cannot contains @
myhome = 'acasa'
print(myhome)

# identificatorii nu pot incepe cu cifre
total123 = 10
#123total = 20

# Python este case-sensitive
print('\n3. Python este case-sensitive')
total = 10
print('total=',total)
Total = 20
print('Total=',Total)
TOTAL = 30
print('TOTAL=',TOTAL)

# Nu exista limita de lungime pentru identificatorii in Python
print('\n4. Nu exista limita de lungime pentru identificatorii in Python')
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx = 10
print('x_foarte_lung=',xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)

# Identificatorii in Python nu pot fi cuvinte rezervate din limbaj
x = 10
# if = 20
print('\n5. Indentificatorii in Python nu pot fi cuvinte rezervate din limbaj')
# if = 20

# Identificatorii in Python cu underscore
x = 10
print('\n6. Identificatorii in Python cu underscore - vezi OOP')
print(' x -> o variabila normala / identificator valid')
print(' _x -> protected variable')
print(' __x -> private variable')
print(' __x__ -> magic variable')
