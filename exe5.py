# Napisz program, który dla podanych przez użytkownika liczb całkowitych 𝑎 i 𝑏 znajdzie
# pierwszą taką liczbę całkowitą z przedziału <a; b>, że:
# a) liczba jest podzielna przez 7
# b) liczba jest palindromem

a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))

for i in range(a, b+1):
    if i % 7 == 0 and str(i) == str(i)[::-1]:
        print(f'Szukana liczba to: {i}')
        break


