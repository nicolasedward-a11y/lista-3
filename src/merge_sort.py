from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    merge_sort_rec(array, 0, len(array) - 1)
    return array


def merge_sort_rec(array, inicio, fim):
    if inicio >= fim:
        return

    meio = (inicio + fim) // 2

    merge_sort_rec(array, inicio, meio)

    merge_sort_rec(array, meio + 1, fim)

    merge(array, inicio, meio, fim)


def merge(array, inicio, meio, fim):
    esqu = []
    dire = []

    for i in range(inicio, meio + 1):
        esqu.append(array[i])

    for i in range(meio + 1, fim + 1):
        dire.append(array[i])

    i = 0
    j = 0
    k = inicio

    while i < len(esqu) and j < len(dire):
        if esqu[i] <= dire[j]:
            array[k] = esqu[i]
            i += 1
        else:
            array[k] = dire[j]
            j += 1

        k += 1

    while i < len(esqu):
        array[k] = esqu[i]
        i += 1
        k += 1

    while j < len(dire):
        array[k] = dire[j]
        j += 1
        k += 1
