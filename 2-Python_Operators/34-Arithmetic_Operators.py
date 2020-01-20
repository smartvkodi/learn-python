# 34 - Arithmetic Operators
print('\n')
msg = '34 - Arithmetic Operators'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)

print('''- General arithmetic operators: + , - , * , / , %
- Python special operators:
	- // => floor division operator
	- ** => exponential / power operator''')

print('\n1. General arithmetic operators')
print('''a=10
b=2''')
a=10
b=2
print('a+b =', a+b) # 12
print('a-b =', a-b) # 8
print('a*b =', a*b) # 20
print('a%b =', a%b) # 0

print('''\na=10
b=3''')
a=10
b=3
print('a+b =', a+b) # 13
print('a-b =', a-b) # 7
print('a*b =', a*b) # 30
print('a%b =', a%b) # 1

print('\n2. Division')
print('10/2 =', 10/2) # 5.0
print('10/3 =', 10/3) # 3.3333333333333335
print('In Python 3.x - division operator always provide floating point result')
print('10/3.0 =', 10/3.0)
print('10/0 => ZeroDivisionError: division by zero')
print('10.0//0 => ZeroDivisionError: division by zero')
print('10%0 => ZeroDivisionError: division by zero')


print('\n3. Floor Division')
print('''In Python 3.x - floor division operator is meant for
- integral arithmetic -  if both arguments are int type - result is int
- floating point arithmetic if at least argument is float - result is float''')
print('10//2 =', 10//2) # 5
print('10//3 =', 10//3) # 3
print('10.0//2 =', 10.0//2) # 5.0
print('10//3.0 =', 10//3.0) # 3.0
print('11.66//3.0 =', 11.66//3.0) # 3.0

print('\n3. Power or Exponential Operator')
print('10**2 =', 10**2) # 100 - int
print('10**3 =', 10**3) # 1000 - int
print('10.0**2 =', 10.0**2) # 100.0 - float
print('10**3.0 =', 10**3.0) # 1000.0 - float
print('16**-0.5 =', 16**-0.5) # 0.25 - float

print('\nNote: We can use +,* operators for str type also.')
print('\n4. String Concatenation Operator')

print('''\n- If we want to use + operator for str type then compulsory 
both arguments should be str type only otherwise we will get error.''')

# s = 'durga' + 10
print('\n \'durga\' + 10 => TypeError: can only concatenate str (not "int") to str')
print('\'durga\' + \'10\' => ', 'durga' + '10')
print('\'durga\' + str(10) => ', 'durga' + str(10))
s = 'durga' + 'soft'
print('\'durga\' + \'soft\' =', s)


print('\n5. String Multiplication Operator')
print('''If we use * operator for str type then compulsory one argument 
should be int and other argument should be str type.\n''')

print('3*"durga" = ', 3*"durga")
print('"durga"*3 =', "durga"*3)
print('\'durga\'*True =', 'durga'*True)
print('\'durga\'*False =', 'durga'*False)
print('"durga"*int(\'3\') =', "durga"*int('3'))
print('"durga"*"durga" => TypeError: can\'t multiply sequence by non-int of type \'str\'')
print('2.5*"durga" => TypeError: can\'t multiply sequence by non-int of type \'float\'')

