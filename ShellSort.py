def shell_sort(arr):
    """
    Сортировка Шелла с последовательностью n/2, n/4, ..., 1
    """
    n = len(arr)
    gap = n // 2  # Начальный шаг
    
    while gap > 0:
        # Выполняем сортировку вставками для этого шага
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Сдвигаем элементы, пока не найдем правильную позицию
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Уменьшаем шаг
    return arr
