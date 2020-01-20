# 92 - Slice Operator Case Study
msg = '92 - Slice Operator Case Study'
tn = ' '*5
text = '#'+ tn + msg + tn + '#'
i = len(text)
print('#'*i)
print(text)
print('#'*i)
print('\n')

s='abcdefghij'

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("1. s='abcdefghij' #  => bcdef => bdf")
print('s[1:6:2] = ', s[1:6:2], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("2. s='abcdefghij' #  => abcdefghij")
print('s[::1] = ', s[::1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("3. s='abcdefghij' #  => jihgfedcba")
print('s[::-1] = ', s[::-1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print('''4. s='abcdefghij' #  => backward from begin to end+1 
=> backward from 3 to 8 => from 3 backward I never gonna get 8
=> empty string (8 is not available into backward direction)''' )
print('s[3:7:-1] = ', s[3:7:-1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("5. s='abcdefghij' #  => fgh => hgf")
print('s[7:4:-1] = ', s[7:4:-1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print('''6. s='abcdefghij' #  => from 0 to 99999 => abcdefghij
slice operator will never rise IndexError ''')
print('s[0:10000:1] = ', s[0:10000:1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("7. s='abcdefghij' # from -4 to 2 => gfedc")
print('s[-4:1:-1] = ', s[-4:1:-1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("8. s='abcdefghij' #  => from -4 to 2 => gec")
print('s[-4:1:-2] = ', s[-4:1:-2], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("9. s='abcdefghij' #  => empty string")
print('s[5:0:1] = ', s[5:0:1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("10. s='abcdefghij' #  => ValueError: slice step cannot be zero")
#print('s[9:0:0] = ', s[9:0:0], '\n')
print('s[9:0:0] = => ValueError: slice step cannot be zero, \n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("11. s='abcdefghij' #  => from 0 to -9 backward => empty string")
print('s[0:-10:-1] = ', s[0:-10:-1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("12. s='abcdefghij' #  from 0 to -10 backward => 'a'")
print('s[0:-11:-1] = ', s[0:-11:-1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("13. s='abcdefghij' # from 0 to -1 forward  => empty string")
print('s[0:0:1] = ', s[0:0:1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("14. s='abcdefghij' # from 0 to -8 backward => empty string")
print('s[0:-9:-2] = ', s[0:-9:-2], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("15. s='abcdefghij' # from -5 to -8 backward => 'fd'")
print('s[-5:-9:-2] = ', s[-5:-9:-2], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("16. s='abcdefghij' # from 10 to 0 backward => empty string")
print('s[10:-1:-1] = ', s[10:-1:-1], '\n')

print('''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  a  b  c  d  e  f  g  h  i  j
  0  1  2  3  4  5  6  7  8  9''')
print("17. s='abcdefghij' # from 10000 to 3 backward => 'jihgfed'")
print('s[10000:2:-1] = ', s[10000:2:-1], '\n')
