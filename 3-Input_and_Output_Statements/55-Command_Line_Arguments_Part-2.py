# 54 - Command Line Arguments Part-2
msg = '54 - Command Line Arguments Part-2'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''## Write a program to print the sum 
of given numbers provided as cmd line arguments''')
from sys import argv
sum=0
for x in argv[1:]:
	sum = sum + eval(x)
print('The sum:', sum)

print('''\n\n## Develop a File Merger Application

# this is hard-coded approach
f1 = open('file1.txt')
f2 = open('file2.txt')
f3 = open('output.txt, w)

for  x in f1:
	f3.write(x)
for x in f2:
	f3.write(x)

# this is correct approach
f1 = open(argv[1])
f2 = open(argv[2])
f3 = open(argv[3], w)

for  x in f1:
	f3.write(x)
for x in f2:
	f3.write(x)


the use of program in cmd line:
py program.py a.txt b.txt c.txt
py program.py jjfj.txt yyrekk.txt jeddr.txt

''')









