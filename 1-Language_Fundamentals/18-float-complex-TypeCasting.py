# 18 - float() and complex() Type Casting
print('\n')
msg = 'float() and complex() Type Casting or Type Coersion'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)


print('\n1. float() - to convert from other types to float type')

print('\n1.a. convert from int to float type')
print('float(10) =>',float(10))
print('float(0B1111) =>',float(0B1111))
print('float(0XFace) =>',float(0XFace))


print('\n1.b. convert from complex to float type')
c = 10 + 20j
# f = float(c)
print('float(10 + 20j) =>  TypeError: can\'t convert complex to float')


print('\n1.c. convert from bool to float type')
b = True
f = float(b)
print('int(True) =>',float(True))
b = False
f = float(b)
print('int(False) =>',float(False))


print('\n1.d. convert from str to float')
print('''String internaly should contains either
integral value in base-10 or float value\n''')

f = float('10')
print('float(\'10\') =>',f)

f = float('20.7')
print('float(\'20.7\') =>',f)

f = float('2.867E3')
print('float(\'20.7E3\') =>',f)

print('\nErrors:')
#f = float('0XBeef')
print('- float(\'0XBeef\') => ValueError: could not convert string to float: \'0XBeef\'')
#f = float('durga')
print('- float(\'durga\') => ValueError: could not convert string to float: \'durga\'')



print('\n\n\n2. complex() - to convert from other types to complex type')

print('\nForm 1 - complex(x)')
print('complex(10) =>',complex(10))
print('complex(0B1111) =>',complex(0B1111))
print('complex(10.7) =>',complex(10.7))
print('complex(True) =>',complex(True))
print('complex(False) =>',complex(False))

print('\n! convert from str to complex')
print('''String internaly should contains either
integral value in base-10 or float value''')
print(' - complex(\'10\') =>',complex('10'))
print(' - complex(\'10.5\') =>',complex('2.5'))
print(' - complex(\'1.333777e3\') => ', complex('1.333777e3'))
print(' - complex(\'0B1111\') => ValueError: complex() arg is a malformed string')



print('\nForm 2 - complex(x,y)')
print('complex(10,20) =>',complex(10,20))
print('complex(0B1111, 0xF) =>',complex(0B1111,0xF))
print('complex(10.7, 20.6) =>',complex(10.7,20.6) )
print(' - complex(\'10\', \'20\') => TypeError: complex() can\'t take second arg if first is a string')
print(' - complex(\'10\', 20) => TypeError: complex() can\'t take second arg if first is a string')
print(' - complex(10.5, \'2\') => TypeError: complex() second arg can\'t be a string')
print('complex(False, False) =>',complex(False, False))
print('complex(False, True) =>',complex(False, True))
print('complex(True, False) =>',complex(True, False))
print('complex(True, True) =>',complex(True, True))