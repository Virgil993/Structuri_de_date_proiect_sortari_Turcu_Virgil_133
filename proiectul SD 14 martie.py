import random
import time
import decimal

def test_sort(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True



def interclasre(lista1,lista2):
    i = j = 0
    sol = []
    while i != len(lista1) and j!= len(lista2):
        if lista1[i] < lista2[j]:
            sol.append(lista1[i])
            i+=1
        else:
            sol.append(lista2[j])
            j+=1
    while i != len(lista1):
        sol.append(lista1[i])
        i+=1
    while j != len(lista2):
        sol.append(lista2[j])
        j+=1
    return sol

def Timsort(lista):
    if len(lista) <= 64:
        for i in range(1,len(lista)):
            ok = 1
            j = i
            while ok != 0:
                if j == 0:
                    ok = 0
                else:
                    if lista[j] < lista[j-1]:
                        lista[j],lista[j-1] = lista[j-1],lista[j]
                        j -= 1
                    else:
                        ok = 0
        return lista
    else:
        return interclasre(Timsort(lista[:len(lista)//2]),Timsort(lista[len(lista)//2:]))

def merge_sort(lista):
    if len(lista) == 1:
        return lista
    else:
        return interclasre(merge_sort(lista[:len(lista)//2]),merge_sort(lista[len(lista)//2:]))


def count_sort(lista):
    if max(lista) < 100000000:
        count = [0 for i in range(max(lista) + 1)]

        for i in range(len(lista)):
            count[lista[i]] += 1

        j = 0
        sol = []
        while j <= max(lista):
            while count[j] != 0:
                sol.append(j)
                count[j] -= 1
            j += 1
        return sol
    else:
        return False

def bubble_sort(lista):
    inceput = time.time()
    if len(lista) >= 100000:
        return False
    while 1:
        nr = 0
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
                nr = nr +1
        if nr == 0:
            break
    return lista

T = int(input("numarul de teste ="))
for i in range(T):
    N = int(input(f"numarul de elemente din testul {i+1} = "))
    M = int(input(f"valoare maxima posibila din testul {i+1} = "))
    L = [random.randrange(0,M+1) for i in range(N)]  #lista cu elemente ce va fi sortata
    lista_copie = L
    start = time.time()
    lista_copie = bubble_sort(lista_copie)
    final = time.time()
    d = decimal.Decimal(final - start)
    if lista_copie:
        if test_sort(lista_copie):
            print("lista a fost sortata de bubble sort")
            print(f"timpul de executare = {d}")
        else:
            print("lista nu a fost sortata de bubble sort")
            print(f"timpul de executare = {d}")
    else:
        print("lista nu poate fi sortata de bubble sort deoarece numarul elementelor este prea mare")
    lista_copie = L
    start = time.time()
    lista_copie = count_sort(lista_copie)
    final = time.time()
    d = decimal.Decimal(final - start)
    if lista_copie:
        if test_sort(lista_copie):
            print("lista a fost sortata de count sort")
            print(f"timpul de executare = {d}")
        else:
            print("lista nu a fost sortata de count sort")
            print(f"timpul de executare = {d}")
    else:
        print("lista nu a putut fi sortata de count sort din cauza faptului ca ocupa prea multa memorie")
    lista_copie = L
    start = time.time()
    lista_copie = merge_sort(lista_copie)
    final = time.time()
    d = decimal.Decimal(final - start)
    if test_sort(lista_copie):
        print("lista a fost sortata de merge sort")
        print(f"timpul de executare = {d}")
    else:
        print("lista nu a fost sortata de merge sort")
        print(f"timpul de executare = {d}")
    lista_copie = L
    start = time.time()
    lista_copie = Timsort(lista_copie)
    final = time.time()
    d = decimal.Decimal(final - start)
    if test_sort(lista_copie):
        print("lista a fost sortata de  Timsort")
        print(f"timpul de executare = {d}")
    else:
        print("lista nu a fost sortata de Timsort")
        print(f"timpul de executare = {d}")
    lista_copie = L
    start = time.time()
    lista_copie.sort()
    final = time.time()
    d = decimal.Decimal(final - start)
    if test_sort(lista_copie):
        print("lista a fost sortata de sortarea naturala a limbajului de programare")
        print(f"timpul de executare = {d}")
    else:
        print("lista nu a fost sortata de sortarea naturala a limbajului de programare")
        print(f"timpul de executare = {d}")

