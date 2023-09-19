def quicksort(listtest):
    if len(listtest) <= 1:
        return listtest

    pivot = listtest[len(listtest) // 2]
    left = [x for x in listtest if x < pivot]
    middle = [x for x in listtest if x == pivot]
    right = [x for x in listtest if x > pivot]

    return quicksort(left) + middle + quicksort(right)
