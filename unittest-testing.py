import unittest


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


class MySortTest(unittest.TestCase):
    # Нужно отнаследовать класс от данного

    # проверяющие методы должны начинаться с test
    # Перечислим все возможные варианты
    # Фреймворк вызывает лишь методы, начинающиеся с test
    def test_normal(self):
        result = my_sort([3, 4, 2, 8, 6, 1, 4])
        # проверим, что она вернула
        self.assertEqual(result, [1, 2, 3, 4, 4, 6, 8])

    def test_reversed(self):
        result = my_sort([1, 2, 3])
        self.assertEqual(result, [1, 2, 3])

    def test_negative(self):
        result = my_sort([-1, -2, -3])
        self.assertEqual(result, [-3, -2, -1], 'Не работает сортировка с отрицательными числами')

    def test_empty(self):
        result = my_sort([])
        self.assertEqual(result, [], 'Не работает сортировка пустого списка')


if __name__ == "__main__":
    # запускаем автодескавер тестов
    unittest.main()

# Виды тестов:
#   Смоук тесты(Проверяется, запускается ли программа и импортируется ли модуль)
#   Модульные тесты(unit-тесты: тестируются отдельные классы)
#   Функциональные тесты(проверяется, соответствует ли программа техзаданию)
#   Регрессионные тесты((найденные ранее ошибки больше не повторяются)
#   Нагрузочные тесты:проверяется, как ведет себя программа под множеством одновременных запросов