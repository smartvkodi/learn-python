# 48 - Important Functions and Variables of math Module
import math 
# you can import the module as alias 
# once we define alias name we can not use original name

# if we do not want to use module name
# we can use the functions from module directly
# from math import sqrtr, pi OR import all
from math import *

print('\n')
msg = '48 - Important Functions and Variables of math Module'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Important Functions and Variables of math Module
- sqrt(x)			- pi
- floor(x)			- e
- ceil(x)			- inf
- pow(x,y)			- nan
- gcd(x,y)			.....
- sin(x)
- cos(x)
... ''')

# it is possible create alias only for an function
from math import sqrt as radical

print('radical(16) =', radical(16))

print('''\n#Example: Find circle area for the given radius''')
r = int(input('Enter circle radius:'))
area1 = pi*r**2
area2 = pi*pow(r,2)
print('The circle area: ', area1)
print('The circle area: ', area2)

print('\n',dir(math))

print('\n#Examples:')
print('sqrt(16) = ', math.sqrt(16))
print('pi = ', math.pi)
print('e = ', math.e)



