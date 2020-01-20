# 50 - Demo Program-1 to Read input data from the keyboard
msg = '50 - Demo Program to Read input data from the keyboard'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''\n1. Write a short program to read 2 int values from keyboard and then print the sum
# compulsory we require performing data-type casting because input() returns str''')

print("\nx = int(input('Enter First Number:'))")
x = int(input('Enter First Number:'))

print("\ny = int(input('Enter Second Number:'))")
y = int(input('Enter Second Number:'))

print('\nThe sum:', x, '+', y, '=', x+y)

print('''\n# not recomanded 
print('The sum:', int(input('Enter First Number:') + int(input('Enter Second Number:'))''')



print('''\n\n2. Write a short program to read the employee data 
from keyboard and then print that data\n''')

print("\n eno = int(input('Enter Employee Number:'))")
eno = int(input('Enter Employee Number:'))

# data-type casting is not required
print("\n ename = input('Enter Employee Name:')")
ename = input('Enter Employee Name:')

print("\n esal = float(input('Enter Employee Salary:'))")
esal = float(input('Enter Employee Salary:'))

# data-type casting is not required
print("\n eaddr = input('Enter Employee Address:')")
eaddr = input('Enter Employee Address:')

print('''\n!! married = bool(input('Is Employee Married? [True|False]:'))
it is always true because only bool('') returns False
if bool('not empty') returns True
married = bool('False')''')
married = bool('False')
print('married:', married)

print("\n married = eval(input('Is Employee Married? [True|False]:'))")
married = eval(input('Is Employee Married? [True|False]:'))

print('\nPlease, confirm your provided information')
print('Emplyee Number:', eno)
print('Employee Name:', ename)
print('Employee Salary:', esal)
print('Employee Address:', eaddr)
print('Employee Married:', married)
