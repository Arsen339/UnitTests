import unittest
from Mock_objects import ExternalResourceGetter
import Mock_objects

# FakeResult нужен для устранения зависимости от внешних объектов

_test_data = """
123456789
12345
1234
123
12

"""

class FakeResult:
    def __init__(self):
        self.text = _test_data

def fake_get_result(url):
    return FakeResult()


class ExternalResourceGetterTest(unittest.TestCase):

    def test_normal(self):
        getter = ExternalResourceGetter(url='https://www.python.org/')
        # переопределим функцию get
        Mock_objects.requests.get = fake_get_result
        result = getter.run()
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()