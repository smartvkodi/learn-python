# 54 - Command Line Arguments Part-1
msg = '54 - Command Line Arguments Part-1'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('## How can we pass the command line arguments to our python programs\n')

print('''- At execution time #python program.py 10 20 30') 
these arguments 10, 20, 30 are the command line arguments''')

print('''\n- How can we these command line arguments?
# sys	- is predefined module in Python which contains a variable 'argv'
# argv	- is a list type(order is important, duplicate are allowed) 
	which helps to get the command line arguments''')

print('''\nfrom sys import argv
print('type(argv) =>', type(argv))''')
from sys import argv
print('type(argv) => ', type(argv))

print('''\n#python program.py 10 20 30
print('argv[0] =>', argv[0]?? => no returns 10!!
argv = [program.py, 10, 20, 30]
argv[0] = 'program.py' ''')
print('\n* argv =',argv)

print('\n## Program to print command line arguments information:')

from sys import argv
print('\nThe number of cmd line argumenst: ', len(argv))
print('\nThe list of cmd line arguments: ', argv)
print('\nThe cmd line arguments one by one:')
for x in argv:
	print(x)








