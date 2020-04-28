slownik = {}


print("Witam w Twoim prywatnym słowniku")

print('\n')

print("Poniżej znajduję się menu, które oprowadzi Cię po programie")

print('Wpisz 1 aby dodać nowe słowo do słownika')

print('Wpisz 2 aby znaleźć słowo')

print('Wpisz 3 aby usunąć słowo ze słownika')

print("Wpisz 4 aby zakończyć program")

while(True):

    wybor = input("Wpisz cyfrę, odpowiednią dla zadania, które chcesz wykonać: ")

    if wybor == '1':
        klucz = input('Podaj słowo, które chcesz zdefiniować: ')
        definicja = input('Podaj definicę: ')
        slownik[klucz] = definicja

    elif wybor == '2':
        klucz = input('Podaj słowo, którego szukasz: ')
        if klucz in slownik:
            print(slownik[klucz])
        else:
            print('Podane słowo nie zostało zdefiniowane')

    elif wybor == '3':
        klucz = input('Podaj słowo, które chcesz usunąć: ')
        if klucz in slownik:
            del slownik[klucz]
        else:
            print('Podane słowo nie istnieje w słowniku')

    elif wybor == '4':
        break

    else:
        print('Proszę wybrać podaną w menu cyfrę')

    
