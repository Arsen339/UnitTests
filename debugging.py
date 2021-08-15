def prime_numbers_generator(n):
    """Генератор поиска простых чисел"""
    prime_numbers = []
    for number in range(2, n+1):

        for prime in prime_numbers:
            if number % prime == 0:

                break

        else:

            prime_numbers.append(number)
            yield number


for prime in prime_numbers_generator(100):
    print(f"Простое из генератора: {prime}")
# Плюсы дебаггинга: возможность следить за ходом выполнения алгоритма
# Недостатки: сложно поймать необходимое состояние программы