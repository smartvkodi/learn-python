# str - Slice Operator in String Data Type - 
print('\n\nSlice Operator in String Data Type str')
print('- In Python exista un operator special pentru string-uri')

print('\n1. Vreau sa extrag doar o parte dintr-un string')
print('s[begin:end]')
print ('=> un substring de la indexul "begin" la indexul "end-1"')
s = 'abcdefghijklmnopqrstuvwxyz'
print('\nFie s = ',s ,' -> ', type(s))
print('Vreau sa extrag de la indexul 3 la 8 -> "defghi"')
print(' - s[3:9] = ', s[3:9])

print('\n\n2. Vreau sa extrag de la inceput pana la indexul "end-1"')
print('- s[:end] pentru ca default begin index = 0  ')
print ('=> un substring de la indexul "0" pana la indexul "end-1"')

s = 'abcdefghijklmnopqrstuvwxyz'
print('\n3. Fie s = ',s ,' -> ', type(s))
print('Vreau sa extrag de la inceput pana la al 8 index "abcdefghi"')
print(' - s[:9] = ', s[:9])

print('\n4., Fie s = ',s ,' -> ', type(s))
print('Vreau sa extrag de la index 3 la sfarsitul string-ului"')
print(' - s[3: ] = ', s[3:])

print('\n5. Fie s = ',s ,' -> ', type(s))
print('Nu specificam niciun index -> retureaza stringul original"')
print(' - s[:] = ', s[:])

print('\n6. Fie s = ',s ,' -> ', type(s))
print('Specificam index in afara range-ului')
print(' - s[3:1000] = ', s[3:1000])
print('Operatorul Slice nu ridica niciodata Index Error: string index out of range')

print('\n7. Fie s = ',s ,' -> ', type(s))
print(' - s[5:1] = ', s[5:1])
print('''daca de la pozitia "begin" mergand spre dreapta
nu intalnim indexul "end-1" 
atunci nu este nimic de returnat 
deci nu se returneza nimic -> sau empty string \'\' ''')
