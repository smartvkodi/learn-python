# 47 - Various Possible Ways to Import a Module
from math1 import *
from math2 import *

'''using an Python module'''

print('\n')
msg = '47 - Various Possible Ways to Import a Module'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('\nMathematical Functions from math module')

print('''Asume that we import same function from 2 modules!
What will happen that  will use sqrt(4)?''')

sqrt(4)

print('''Will never get the error, 
will be use the most recent member (version) function, class''')

