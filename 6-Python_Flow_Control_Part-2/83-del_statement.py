# 83 - del statement
msg = '83 - del statement'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

print("Python specific syntax - 'del' statement")

print('''\nWhen the Python's "del" statement is useful?
- "del" statement: delete a reference variable in respect of memory usage;
- if you "del" an reference variable it doesn't mean that the object become 
eligible for garbage collection(GC), it is possible that other refrence variables 
pointing that object;
- we can delete reference variables which pointing to immutable objects
- we cannot delete elements present inside immutable objects (string, tuple,..)''')

print('''\n1. I want to delete x variable then the coresponding object
will be the eligible to be destroyed by garbage collector(GC)
for improving the memory usage.

x=10
print(x)

## x variable is not longer required so
del x
## after deleting x variable it is possible accessing the x variable?
print(x) => will get NameError: name 'x' is not defined
''')

print('''\nExample:
s1='durga'
s2=s1
s3=s2

## single object 'durga' refered by 3 references: s1, s2 and s3
## if I del s1 => only s1 reference will be deleted but not the object
del s1

print('s2 =', s2)
print('s3 =', s3)

## it is possible to delete multiple reference variables
del s2, s3

## output:''')
s1='durga'
s2=s1
s3=s2
del s1
print('s2 =', s2)
print('s3 =', s3)
del s2,s3

print('''\n\n2. "del" versus immutable objects
# immutable object => once we create an object we cannot perform any changes to that object

s='durga' - it is an immutable object

Is possible to delete the s reference variable which is pointing to the immutable objects?
Yes. You can delete the reference variable because it will no change the object.

del s[0] .. will get error because we are trying to modify the immutable object
TypeError: 'str' object doesn't support item deletion
''')

print('''\n\n3. "del" versus None

x=10
# we have 2 approches to make this 10 object eligible to garbage collection:

- del x -> x refrence variable deleted and then you cannot access x variable
  trying to print(x) => will get NameError: name 'x' is not defined

- x=None -> we reasign to x reference variable the None object, the x variable 
  remains accessible print(x) => will get None''')

x=10
#del x print(x) => will get NameError: name 'x' is not defined
x=None
print(x)




