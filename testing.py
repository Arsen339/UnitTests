from my_sort import  my_sort
# выделим тестировку в отдельный файл

import unittest

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
