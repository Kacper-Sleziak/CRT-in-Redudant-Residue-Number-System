import math
from System import *
import time
import numpy as np
import matplotlib.pyplot as plt


# funkcja sprawdzająca czy dwie liczby są wzglednie pierwsze

def are_coprime(a, b):
    hcf = 1

    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            hcf = i

    return hcf == 1


pos_number = 1000000                                        # liczba, ktorej range bedziemy obliczac
number = int(math.pow(2, 13))                               # liczba od ktorej zaczynamy wyszukiwanie liczb wzglednie pierwszych

coprime_list = []                                           # lista liczb pierwszych i rownoczesnia najwieksza baza
time_list_redudant = np.array([])                           # tablica usrednionych pomiarow z nadmiarem
time_list_non_redudant = np.array([])                       # tablica usrednionych pomiarow bez nadmiarow
base_list = []                                              # lista baz
base_lengths = np.array([])                                 # tablica wielkosci baz

number_of_tests = 1000                                      # liczba testow do przeprowadzenia
largest_base = 1000                                         # wielkosc najwiekszej bazy
number_of_bases = 20                                        # liczba baz dla, ktorej chcemy dokonac pomiarow
density_of_diagram = largest_base // number_of_bases        # liczba punktow na wykresie

counter = 0

# Obliczanie najdluzszej bazy
for i in range(3, number):

    if i == 3:
        coprime_list.append(i)
        counter += 1

    else:
        coprime = True

        for k in range(counter):
            if not are_coprime(coprime_list[k], i):
                coprime = False
                break

        if coprime:
            counter += 1
            coprime_list.append(i)

    if counter >= largest_base:
        break

# tworzenie mniejszych baz za pomoca zmienijszania najwiekszej
for i in range(number_of_bases):

    if i != 0:
        for k in range(density_of_diagram):
            coprime_list.pop()

    buffor_list = coprime_list.copy()
    base_list.append(buffor_list)

# Wielkosci baz
for i in range(number_of_bases):
    base_lengths = np.append(base_lengths, largest_base - i * density_of_diagram)

# wlasciwe pomiary czasu
for i in range(number_of_bases):
    time_of_operation_redudant = 0
    time_of_operation_non_redudant = 0

    for k in range(number_of_tests):
        rns = System(base_list[i], pos_number)

        start_time_redudant = time.time()
        rns.get_rank_of_number_redundant()
        time_of_operation_redudant = time_of_operation_redudant + (time.time() - start_time_redudant) * 10 ** 3

        start_timne_non_redudant = time.time()
        rns.get_rank_of_number()
        time_of_operation_non_redudant = time_of_operation_non_redudant + (time.time() - start_time_redudant) * 10 ** 3

    average_time_of_operation_redudant = time_of_operation_redudant / number_of_tests
    average_time_of_operation_non_redudant = time_of_operation_non_redudant / number_of_tests

    time_list_redudant = np.append(time_list_redudant, average_time_of_operation_redudant)
    time_list_non_redudant = np.append(time_list_non_redudant, abs(average_time_of_operation_non_redudant))

y_1 = time_list_redudant
x = base_lengths
y_2 = time_list_non_redudant

plt.xlabel("Liczba modulow w bazie")
plt.ylabel("Czas obliczania rangi [ms]")

plt.plot(x, y_1, label = "Ranga z nadmiarem")
plt.plot(x, y_2, label = "Ranga bez nadmiaru")

plt.legend()

plt.show()
