# doc-тесты - тесты, хранящиеся в документации к функциям
def my_sort(slist):
    """
    Функция сортировки списков
    >>> my_sort([2, 1, 3])
    [1, 2, 3]
    """
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist) - 1):
            if slist[i] > slist[i + 1]:
                slist[i], slist[i+1] = slist[i+1], slist[i]
                was_swap = True
    return slist


if __name__ == "__main__":
    import doctest

    doctest.testmod()  # проходит по всем функциям в нейм-спейсе и запускает

# Лучше использовать только в простейших случаях
