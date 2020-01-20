# 43 - Ternary Operator
print('\n')
msg = '43 - Ternary Operator'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''\n ~a --> unary operator
 a+b --> binary operator
 3 args --> Ternary Operator(conditional operator)''')

print('''\n- Ternary Operator:
	a = 10
	b = 20
	c = 30 if a > b else 40''')
a = 10
b = 20
c = 30 if a > b else 40
print('c = ', c)


print('''\n- Ternary Operator Syntax:
	c = first_value if condition else second_value''')

print('''\n#Example: Write a short Python program which read
2 int values from the keyboard and print the minimum value''')

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
min = a if a<b else b
print('The minimun value: ', min)

print('''\n# Insight the Ternary Operator we can use Ternary Operator
Nesting of ternary operator''')

print('''\n#Example: Write a short Python program which read
3 int values from the keyboard and print the minimum value''')

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
min = a if a<b and a<c else b if b<c else c
print('The minimun value: ', min)


print('''\n#Example: Write a short Python program which read
3 int values from the keyboard and print the maximum value''')

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
c = int(input('Enter third number:'))
max = a if a>b and a>c else b if b>c else c
print('The maximum value: ', max)


print('''\n#Example: Write a short Python program which read
2 int values from the keyboard and print:
	1. The numbers are equal;
	2. First number is smaller than second number;
	3. First number is greather than second number''')

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))

m1='The numbers are equal'
m2='First number is smaller than second number'
m3='First number is greather than second number'

m = m1 if a==b else m2 if a<b else m3
print(m)