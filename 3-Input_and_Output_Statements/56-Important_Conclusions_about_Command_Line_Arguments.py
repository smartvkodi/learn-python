# 56 - Important Conclusions about Command Line Arguments
msg = '56 - Important Conclusions about Command Line Arguments'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''# 1st Conclusion 
- Space is the separator between cmd line arguments
- If the argument contains spaces, we should enclose
it between the double quotes "argument with spaces"

# program.py file
from sys import argv
print(argv[1])

# py program.py Sunny Leone
the result: Sunny

# but I want to print "Sunny Leone"
py program.py "Sunny Leone"
the result: Sunny Leone
''')

print('''\n# 2nd Conclusion 
- all command line arguments are available in str form only

# program.py file
from sys import argv
print(argv[1] + argv[2])

py program.py 10 20 - args are available in str form, then
the result: 1020

# but I want the result to be 30
# program.py file
from sys import argv
print(int(argv[1]) + int(argv[2]))

py program.py 10 20 - args are available in str form,
but we perform the int type casting, so
the result: 30
''')


print('''\n# 3rd Conclusion 
- if we are trying access command line arguments with
out of range index, we ar going to get IndexError

# program.py file
from sys import argv
print(argv[100])

py program.py 10 20 - we ask to print argv[100],
the result: IndexError: list index out of range''')