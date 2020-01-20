# 82 - pass statement
msg = '82 - pass statement'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print("Python specific syntax - 'pass' statement")

print('''\nWhen the Python's 'pass' statement is useful?
pass statement: acts as placeholder for future implementention 
pass statement: acts empty block
''')

def f1():
	pass

print('''\nI want to write an function 
def f1(): ### but we do not know implementention for this function
	pass  ### empty block - pass acts as placeholder for future implementention

## syntacticaly I defined function f1 with empty body
## otherwise we will get SyntaxError: unexpected EOF while parsing''')


print('''\nI want to write multiple classes but I don'k know how this classes are: 
	class A:		class B:	class C:   
		pass			pass		pass

	### but we do not know implementention for these classes
	pass  ### empty block - pass acts as placeholder for future implementention''')

print('''\nx=100
if x>10:
	print('Success')
else:
	pass
''')
x=int(input('Enter Marks:'))
if x>=35:
	print('Success')
else:
	pass
	## print('Fail') -- this will be the future implementetion
print("the next statements...")


print('''\n\n### In OOP there is the concept of "abstract method"
# abstract method in abstract classes: a method without body
# the child classes are responsable to provide implementation of abstract methods

Example: loan bank application

Loan -> multiple types of loans are available:
	- HomeLoan => interest rate = 8%
	- VehicleLoan => interest rate = 12%
	- PersonalLoan => interest rate = 22%

#### for every type of loan, there is an specific  "interest rate" 
but we don't know it at Loan level.. but we know at every child type loan

How to implement this scenario:

from abc import *

class Loan(ABC):
	@abstractmethod
	def getInterestRate(self):
		pass

class HomeLoan(Loan):
	def getInterestRate(self):
		return 8

class VehicleLoan(Loan):
	def getInterestRate(self):
		return 12

class PersonalLoan(Loan):
	def getInterestRate(self):
		return 22

# instantiate the child classes and then display the intrerest rate

homeLoan = HomeLoan()
print('homeLoan.getInterestRate() =>', homeLoan.getInterestRate())

vehicleLoan = VehicleLoan()
print('vehicleLoan.getInterestRate() =>', vehicleLoan.getInterestRate())

personalLoan = PersonalLoan()
print('personalLoan.getInterestRate() =>', personalLoan.getInterestRate())
''')

from abc import *

class Loan(ABC):
	@abstractmethod
	def getInterestRate(self):
		pass

class HomeLoan(Loan):
	def getInterestRate(self):
		return 8

class VehicleLoan(Loan):
	def getInterestRate(self):
		return 12

class PersonalLoan(Loan):
	def getInterestRate(self):
		return 22

homeLoan = HomeLoan()
print('homeLoan.getInterestRate() =>', homeLoan.getInterestRate())

vehicleLoan = VehicleLoan()
print('vehicleLoan.getInterestRate() =>', vehicleLoan.getInterestRate())

personalLoan = PersonalLoan()
print('personalLoan.getInterestRate() =>', personalLoan.getInterestRate())


print('''\n\n### pass to define minimal classes and minimal functions

- to define minimal class
class A:
	pass

- to define minimal function
def f1():
	pass