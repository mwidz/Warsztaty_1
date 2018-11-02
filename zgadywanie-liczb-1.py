from random import randint

# Zadanie 1
print("\n Zadanie 1 \n")


domyslna = False
wylosowana = randint(1, 100)

while not domyslna:
    zgaduj = input("Zgadnij liczbę: ")
    try:
        liczba = int(zgaduj)
        if liczba < wylosowana:
            print("Za mało!")
        elif liczba > wylosowana:
            print("Za dużo!")
        else:
            print("Zgadłeś!")
            domyslna = True
    except ValueError:
        print("To nie jest liczba")
