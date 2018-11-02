from random import randint

# Zadanie 2
print("\n Zadanie 2 \n")

liczby = []

for i in range(1, 7):
    domyslna = False

    while not domyslna:

        liczba = input("Podaj " + str(i) + " typowaną liczbę: ")

        try:

            liczba_int = int(liczba)

            if (liczba in liczby):
                print("\n Już tą liczbę podałeś! Podaj inną... \n")
            elif (liczba_int < 1) or (liczba_int > 49):
                print("\n Liczba spoza zakresu! Podaj inną... \n")
            else:
                liczby.append(liczba_int)
                domyslna = True

        except ValueError:
            print("\n To nie jest liczba! \n")

liczby.sort()
print("\n Podałeś następujące liczby: " + str(liczby))

wylosowane = []
i = 1
while i <= 6:
    rand = randint(1, 49)
    wylosowane.append(rand)
    i += 1

print("\n Zostały wylosowane następujące liczby: " + str(wylosowane) + "\n")

licznik = []

for l in liczby:
    if l in wylosowane:
        licznik.append(l)

# if len(licznik) == 3:
#     print("\n Trafiłeś trójkę: " + licznik + "\n")
# elif len(licznik) == 4:
#     print("\n Trafiłeś czwórkę: " + licznik + "\n")
# elif len(licznik) == 5:
#     print("\n Trafiłeś piątkę: " + licznik + "\n")
# elif len(licznik) == 6:
#     print("\n Trafiłeś szóstkę: " + licznik + "\n")
# else:
#     print("\n Niestety nie udało się nic trafić :( \n")

if len(licznik) >= 3:
    print("\n Trafiłeś przynajmniej trójkę: " + licznik + "\n")
else:
    print("\n Niestety nie udało się nic trafić :( \n")

# if len([l for l in liczby if l in wylosowane]) >= 3:
#     print("\n Trafiłeś przynajmniej trójkę: " + licznik + "\n")
# else:
#     print("\n Nie tym razem... \n")
