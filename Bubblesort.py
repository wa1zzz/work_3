def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Флаг проверки обменов
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Обмен элементов
                swapped = True
        if not swapped:  # Если обменов не было - выходим
            break
    return arr
