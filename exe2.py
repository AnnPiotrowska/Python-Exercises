#zadanie 8

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

suma = 0
iloczyn = 1

if a <= b:
    for i in range(a,b+1):
        suma += i
        iloczyn *= i
    print(f'Suma twoich liczb wynosi: {suma}')
    print(f'Iloczyn twoich liczb wynosi: {iloczyn}')
else:
    print('Początek przedziału musi być mniejszy bądź równy niż jego koniec!')



