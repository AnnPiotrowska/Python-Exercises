#Stwórz program w pythonie, który dla podanej liczby naturalnej 𝑛 wypisze szachownicę zbudowaną ze znaków # oraz @, gdzie w lewym górnym rogu zawsze jest #

nam = int(input('Podaj liczbe: '))

znak1 = '#'
znak2 = '@'

for i in range(1,nam+1):
    for j in range(1, nam + 1):
        if (i + j)% 2 == 0:
            print(znak1,end='')
        else:
            print(znak2,end='')
    print()