from unittest.mock import Mock

fake_1 = Mock()
print(fake_1(1, 2, 3, test=42))
print(fake_1.called)  # используется ли объект
fake_1.assert_called_with(1, 2, 3, test=42)  # если объект не вызывался с параметром, выскочит исключение

# заставим возвращать объект
fake_2 = Mock(return_value=30)
print(fake_2())

# присвоим объекту любой атрибут
fake_3 = Mock()
fake_3.any_attr = 27
print(fake_3.any_attr)
