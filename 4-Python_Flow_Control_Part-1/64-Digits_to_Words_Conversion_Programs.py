# 64 - Digits to Words Conversion Programs
msg = '64 - Digits to Words Conversion Programs'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print('''Program-1: Write a program to take a single digit number
from the keyboard and print its value in English word

d = int(input('Enter enter any digit from 0 to 9:'))
if d==0:
	print('Zero')
elif d==1:
	print('One')
elif d==2:
	print('Two')
elif d==3:
	print('Three')
elif d==4:
	print('Four')
elif d==5:
	print('Five')
elif d==6:
	print('Six')
elif d==7:
	print('Seven')
elif d==8:
	print('Eight')
elif d==9:
	print('Nine')
else:
	print('Sorry! Please, enter a digit from 0 to 9 only')
''')

d = int(input('Enter enter any digit from 0 to 9:'))
if d==0:
	print('Zero')
elif d==1:
	print('One')
elif d==2:
	print('Two')
elif d==3:
	print('Three')
elif d==4:
	print('Four')
elif d==5:
	print('Five')
elif d==6:
	print('Six')
elif d==7:
	print('Seven')
elif d==8:
	print('Eight')
elif d==9:
	print('Nine')
else:
	print('Sorry! Please, enter a digit from 0 to 9 only')


print('''\nProgram-2: Write a program to take a single digit number
from the keyboard and print its value in English word

list=['Zero, 'One', 'Three, 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
d = int(input('Enter enter any digit from 0 to 9:'))

if d>=0 and d<=0
	print(list[d]
else:
	print('Sorry! Please, enter a digit from 0 to 9 only')
''')

list=['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
d=int(input('Enter enter any digit from 0 to 9:'))
if d>=0 and d<=9:
	print(list[d])
else:
	print('Sorry! Please, enter a digit from 0 to 9 only')


print('''\nProgram-3: Write a program to take a number between 0 and 999
from the keyboard and print its value in English word

words_upto_19=['','ONE','TWO','THREE','FOUR','FIVE','SIX',
'SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']

words_for_tens=['','','TWENTY','THIRTY','FOURTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']

n=int(input('Enter a number from 0 to 99:'))
output=''
if n==0:
	output='ZERO'
elif n<=19:
	output=words_upto_19[n]
elif n<=99:
	output=words_for_tens[n//10]+" "+words_upto_19[n%10]
else:
	output='Please enter a value from 0 to 99 only'
print(output)
''')

words_upto_19=['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE',
'TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']

words_for_tens=['','','TWENTY','THIRTY','FOURTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']

n=int(input('Enter a number from 0 to 999:'))
output=''
if n==0:
	output='ZERO'
elif n<=19:
	output=words_upto_19[n]
elif n<=99:
	output=words_for_tens[n//10]+" "+words_upto_19[n%10]
elif n<=999:
	if n//100==1:
		output="HUNDRED"
	else:
		output=words_upto_19[n//100] + " HUNDREDS"
	n = n%100
	if n<=19:
		output=output + " " + words_upto_19[n]
	else:
		output=output + " " + words_for_tens[n//10]+" "+words_upto_19[n%10]
else:
	output='Please enter a value from 0 to 999 only'
print(output)
