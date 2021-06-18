import math
from System import *
import time
import numpy as np
import matplotlib.pyplot as plt


def are_coprime(a, b):
    hcf = 1

    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            hcf = i

    return hcf == 1


pos_number = 1000000
coprime_list = []  # lista liczb pierwszych
time_list = np.array([])
base_list = []  # lista baz
counter = 0  # licznik
number_of_bases = 1000  # liczba baz
number = int(math.pow(2, 13))  # liczba od ktorej zaczynamy wyszukiwanie liczb wzglednie pierwszych

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

    if counter >= number_of_bases + 3:
        break

for i in range(number_of_bases):
    buffor_list = coprime_list.copy()
    base_list.append(buffor_list)
    coprime_list.pop(number_of_bases - i - 1)

for i in range(number_of_bases):
    rns = System(base_list[i], pos_number)

    start_time = time.time()

    rns.get_rank_of_number()

    time_of_operation = (time.time() - start_time) * 10 ** 3
    time_list = np.append(time_list, time_of_operation)

base_lengths = np.array([])

for i in range(3, number_of_bases + 3):
    base_lengths = np.append(base_lengths, 1003 - i)

y = time_list
x = base_lengths

plt.plot(x, y)

plt.xlabel("Liczba baz")
plt.ylabel("Czas obliczania [ms]")

plt.show()
