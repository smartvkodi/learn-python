# str - Slice Operator Applicationin String Data Type - 
print('\n\nSlice Operator Application cu String Data Type str')

s = 'durgasoftsolutions'

print('\n1. Fie s = ',s ,' -> ', type(s))
print('Vreau ca prima litera sa fie convertita in majuscula')
output = s[0].upper() + s[1:]
print(' output = s[0].upper() + s[1:] => ', output)

print('\n2. Fie s = ',s ,' -> ', type(s))
print('Vreau ca ultima litera sa fie convertita in majuscula')
output = s[:len(s)-1] + s[-1].upper()
print(' output = s[:len(s)-1] + s[-1].upper() => ', output)

print('\n3. Fie s = ',s ,' -> ', type(s))
print('Vreau ca prima si ultima litera sa fie convertita in majuscula')
output = s[0].upper() + s[1:len(s)-1] + s[-1].upper()
print(' output = s[0].upper() + s[1:len(s)-1] + s[-1].upper() => ', output)


