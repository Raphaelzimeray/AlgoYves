def yes_no(arr):
    array_sorted = []
    while arr:
        array_sorted.append(arr[0])
        arr.pop(0)
        if arr:
            arr.append(arr[0])
            arr.pop(0)
    return array_sorted


def beggars(values, n):
    beggars_results = []
    for i in range(n):
        beggar_count = 0
        for i in range(i, len(values), n):
            if i >= len(values) :
                beggar_count = 0
            else:
                beggar_count += values[i]
        beggars_results.append(beggar_count)
    print(beggars_results)
    return beggars_results


# Amélioré par Yves (faire attention à différencier les itérateurs)


def beggars(values, n):
    beggars_results = []
    for i in range(n):
        beggar_count = 0
        for j in range(i, len(values), n):
            beggar_count += values[j]
        beggars_results.append(beggar_count)
    print(beggars_results)
    return beggars_results
