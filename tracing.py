
def prime_numbers_generator(n):
    """Генератор поиска простых чисел"""
    prime_numbers = []
    for number in range(2, n+1):
        print(f"number {number}")
        for prime in prime_numbers:
            if number % prime == 0:
                print(f" делится на {prime}")
                break

        else:
            print(f"Найдено простое число {number}")
            prime_numbers.append(number)
            yield number


for prime in prime_numbers_generator(100):
    print(f"Простое из генератора: {prime}")

# Трассировка(пошаговое выполнение команды) позволяет увидеть весь процесс выполнения
# Позволяет выявить места изменения значений
# применима в сложных условиях
# Недостатки: необходимость писать много кода в print, замедляет выполнение программы
# Сложно переключать режимы отладка vs продакшн

# другой способ отладки - дебаггинг с помощью отладчика