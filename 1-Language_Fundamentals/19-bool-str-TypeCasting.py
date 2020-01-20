# 19 - bool() and str() Type Casting
print('\n')
msg = 'bool() and str() Type Casting or Type Coersion'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)


print('\n1. bool() - to convert from other types to bool type')

print('\n1.a. convert from int to bool type')
print('! Only int 0 => False')
print('bool(0) =>',bool(0))
print('bool(10) =>',bool(10))
print('bool(0XFace) =>',bool(0XFace))

print('\n1.b. convert from float to bool type')
print('! Only float 0.0 => False')
print('bool(0.0) =>',bool(0.0))
print('bool(-1.6) =>',bool(-1.6))
print('bool(2.7E-3) =>',bool(20.7E-3))

print('\n1.c. convert from complex to bool type')
print('! Only complex 0 (0+0j) => False')
print('bool(0+0j) =>',bool(0+0j))
print('bool(0+1j) =>',bool(0+1j))
print('bool(1.7E-1j) =>',bool(1.7E-1j))

print('\n1.d. convert from str to bool type')
print('! Only empty string (\'\') => False')
print('bool(\'\') =>',bool(''))
print('bool(\'False\') =>',bool('False'))
print('bool(\'True\') =>',bool('True'))
print('bool(\'yes\') =>',bool('yes'))
print('bool(\'no\') =>',bool('no'))
print('bool(\'durga\') =>',bool('durga'))


print('\n\n2. str() - to convert from other types to str type')

print('\n2.a. convert from int to str type')
print('str(0) =>',str(0))
print('str(0B1111) =>',str(0B1111))
print('str(10) =>',str(10))
print('str(-100) =>',str(-100))
print('str(0XFace) =>',str(0XFace))

print('\n2.b. convert from float to str type')
print('str(0.0) =>',str(0.0))
print('str(-1.6) =>',str(-1.6))
print('str(2.7E-3) =>',str(20.7E-3))

print('\n2.c. convert from complex to str type')
print('str(10+20j) =>',str(10+20j))
print('str(0+1j) =>',str(0+1j))
print('str(1.7E-1j) =>',str(1.7E-1j))

print('\n2.d. convert from bool to str type')
print('str(False) =>',str(False))
print('str(True) =>',str(True))
