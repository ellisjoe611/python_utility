import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertNotEqual('var'.upper(), 'BAr')
        self.assertListEqual([2, 4, 6, 8], [_ for _ in range(1, 10) if _ % 2 == 0])


if __name__ == '__main__':
    unittest.main()
