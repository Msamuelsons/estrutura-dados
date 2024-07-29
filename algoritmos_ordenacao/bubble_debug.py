def bubble_sort(lista=[]):
    for v in range(0, len(lista) + 1):
        for i in range(0, len(lista) - 1, 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux


lista = [1, 4, 7, 3, 0, 20]
bubble_sort(lista)
print(lista)