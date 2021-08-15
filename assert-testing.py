# Напишем функцию для сортировка


def my_sort(slist):
    """Сортировка массива"""
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist) - 1):
            if slist[i] > slist[i + 1]:
                slist[i], slist[i+1] = slist[i+1], slist[i]
                was_swap = True
    return slist


mas1 = [5, 2, 4, 3, 1, 6, 7, 0]
mas2 = [4, 3, 5]
mas3 = [-7, 9, 8, 1]
print(my_sort(mas1))
print(my_sort(mas2))
print(my_sort(mas3))

# Каждый раз запускать код - долго
# Автоматизируем

if my_sort(mas1) != [0, 1, 2, 3, 4, 5, 6, 7]:
    print("Ошибка!")
if my_sort(mas2) != [3, 4, 5]:
    print("Ошибка!")
if my_sort(mas3) != [-7, 1, 8, 9]:
    print("Ошибка!")

# Еще лучше - использовать оператор assert
assert my_sort(mas1) == [0, 1, 2, 3, 4, 5, 6, 7], "Не работает сортировка целых положительных"


