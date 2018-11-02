# from random import randint

# Zadanie 3
print("\n Zadanie 3 \n")

print("Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach")

min = 1
max = 1000

domyslna = False


def test():
    guess = int((max - min) / 2) + min
    print("Zgaduję: " + str(guess))
    return guess


guess = test()

while not domyslna:

    odp = input("Podaj informację co do trafienia: ")

    if odp == "mniej" and min != max:
        max = guess
        # print(min)
        guess = test()
    elif odp == "więcej" and min != max:
        min = guess
        # print(max)
        guess = test()
    elif odp == "trafiłeś":
        print("Wygrałem!")
        domyslna = True
    else:
        print("nie oszukuj!")
        guess = test()
