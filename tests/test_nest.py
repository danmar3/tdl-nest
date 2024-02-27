import unittest
from tdl_nest import nest_iter, nest_map


class TestNest(unittest.TestCase):

    def test_iter(self):
        data = {'a': 1, 'b': (2, 3, 4), 'c': {'d': [{'e': 5}, {'f': [6, 7]}]}}
        test = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(
            list(nest_iter(data)), test,
            'nest_iter did not produce the expected list'
        )

    def test_map(self):
        data = {'a': 1, 'b': (2, 3, 4), 'c': {'d': [{'e': 5}, {'f': [6, 7]}]}}
        test = [vi**2 for vi in range(1, 8)]
        self.assertEqual(
            list(nest_iter(nest_map(data, lambda x: x**2))), test,
            'nest_map failed to produce expected result'
        )


if __name__ == '__main__':
    unittest.main()