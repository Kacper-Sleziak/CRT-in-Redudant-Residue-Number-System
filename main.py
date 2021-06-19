from System import *
from rns_to_pos_converter import *


def main_menu():
    while True:
        print("Wcisnij: ")
        print("1 aby dokonac operacji w systemie resztowym")
        print("2 aby zamienic liczbe z systemu resztowego na pozycyjny")
        print("3 aby wyjsc z programu")

        print("")
        x = input("Wpisz numer: ")
        print("")

        if x == '1':
            rns_operations_menu()

        if x == '2':
            rns_number = []
            base = []

            print("Podaj dlugosc bazy oraz liczby w systemie resztowym: ")
            length = int(input("Podaj dlugosc: "))

            print("")

            for i in range(length):
                x = int(input(f"Podaj liczbe w bazie na pozycji {i}: "))
                base.append(x)

            print("")

            for i in range(length):
                x = int(input(f"Podaj liczbe w systemie resztowym na pozycji {i}: "))
                rns_number.append(x)

            print(converter(rns_number, base))

            print("")

        if x == '3':
            break


def rns_operations_menu():
    print("CRT MENU")
    base_len = int(input("Podaj wielkosc bazy: "))
    base = []

    for i in range(base_len):
        z = int(input(f"Podaj numer bazy na pozycji numer {i + 1}: "))
        base.append(z)

    print("")

    pos_number = int(input("Podaj liczbe w systemie pozycyjnym: "))
    print("")

    RNS = System(base, pos_number)

    while True:
        print("Wcisnij: ")
        print("0 aby zmienic baze i liczbe")
        print("1 aby otrzymac liczbe w systmie resztowym")
        print("2 aby dodac dwie liczby w systemie resztowym")
        print("3 aby pomnozyc dwie liczby w systemie resztowym")
        print("4 aby podzielic dwie liczby w systemie resztowym")
        print("5 aby obliczyć rangę liczby")
        print("6 aby obliczyć rangę liczby nadmiarowo")
        print("7 aby obliczyc liczbe w systemie pozycyjnym przy pomocy rangi")
        print("8 aby wyjsc z menu operacji w systemie resztowym")

        print("")
        x = input("Wpisz numer: ")
        print("")

        if x == '0':
            base_len = int(input("Podaj wielkosc nowej bazy: "))
            base = []

            for i in range(base_len):
                z = int(input(f"Podaj numer bazy na pozycji numer {i + 1}: "))
                base.append(z)

            pos_number = int(input("Podaj nowa liczbe w systemie pozycyjnym: "))
            print("")

            RNS = System(base, pos_number)

        elif x == '1':
            print(f"liczba w systmie resztowym: {RNS.get_rns()}")
            print("")

        elif x == '2':
            pos_number_b = int(input("Podaj druga liczbe w systmie pozycyjnym: "))
            RNS_b = System(base, pos_number_b)
            print(f"Wynik dodawania {RNS.addition(RNS_b)}")
            print("")

        elif x == '3':
            pos_number_b = int(input("Podaj druga liczbe w systmie pozycyjnym: "))
            RNS_b = System(base, pos_number_b)
            print(f"Wynik mnozenia: {RNS.multiplication(RNS_b)}")
            print("")

        elif x == '4':
            pos_number_b = int(input("Podaj druga liczbe w systmie pozycyjnym: "))
            RNS_b = System(base, pos_number_b)
            print(f"Wynik dzielenia: {RNS.division(RNS_b)}")
            print("")

        elif x == '5':
            print(f"Ranga liczby: {RNS.get_rank_of_number()}")
            print("")

        elif x == '6':
            print(f"Ranga liczby: {RNS.get_rank_of_number_redundant()}")
            print("")

        elif x == '7':
            print(f"Liczba w systemie pozycyjnym: {RNS.convert_to_pos_by_rank()}")
            print("")

        elif x == '8':
            break

        else:
            print("Wprowadziles/as zly znak!")

main_menu()
