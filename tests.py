
import unittest
from functions import string_distance




w1 = 'Email'
w2 = 'email'
w3 = 'informação'
w4 = 'informatica'


class MyTest(unittest.TestCase):

    def test_string_distance1(self):
        self.assertEqual(string_distance(w1,w1,'exact'), 100)
    def test_string_distance2(self):
        self.assertEqual(string_distance(w1,w2,'exact'), 100)
    def test_string_distance3(self):
        self.assertEqual(string_distance(w1,w3,'exact'), 0)
    def test_string_distance4(self):
        self.assertEqual(string_distance(w1,w2,'jaccard'), 100)

    def test_string_distance5(self):
        self.assertTrue(string_distance(w1,w3,'jaccard') < 0.3)

    def test_string_distance6(self):
        self.assertTrue(string_distance(w4,w3,'jaccard') > 0.8)


if __name__ == '__main__':
    unittest.main()