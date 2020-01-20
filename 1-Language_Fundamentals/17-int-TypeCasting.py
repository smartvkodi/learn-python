# 17 - int() Type Casting
print('\n')
msg = 'int() Type Casting or Type Coersion'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)


print('\n1. int() - to convert from other types to int type')

print('\n1.a. convert from float to int type')
f = 10.989
i = int(f)
print('int(',f,') =>',i)
f = -127.89
i = int(f)
print('int(',f,') =>',i)

print('\n1.b. convert from complex to int type')
c = 10 + 20j
# i = int(c)
print('int(',c,') =>  TypeError: can\'t convert complex to int')


print('\n1.c. convert from bool to int type')
b = True
i = int(b)
print('int(',b,') =>',i)
b = False
i = int(b)
print('int(',b,') =>',i)


print('\n1.d. convert from str to int type')
print('''String internaly should contains only
integral value in base-10\n''')
s = '10'
i = int(s)
print('int(',s,') =>',i)

print('\n\tValueError')
s = '0B101011'
# i = int(s)
print('\t- int(',s,') => ValueError: invalid literal for int() with base 10: ',s)

s = '10.5'
# i = int(s)
print('\t- int(',s,') => ValueError: invalid literal for int() with base 10: ',s)

s = '0xFace'
# i = int(s)
print('\t- int(',s,') => ValueError: invalid literal for int() with base 10: ',s)



