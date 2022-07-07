
import unittest
from functions import string_distance, clean_txt


w1 = 'email'
w2 = 'e-mail'
w3 = 'informação'
w4 = 'informacao'

f1 = ' Essas   frases   são   do   OCR '
f2 = 'rodrigo foi jogar'

class MyTest(unittest.TestCase):

    def test_string_distance1(self):
        self.assertEqual(string_distance(w1,w1,'exact'), 100)
    def test_string_distance2(self):
        self.assertEqual(string_distance(w1,w2,'exact'), 0)
    def test_string_distance3(self):
        self.assertEqual(string_distance(w3,w4,'exact'), 0)

    def test_string_distance4(self):
        self.assertTrue(string_distance(w1,w2,'jaccard') >= 0.7)
    def test_string_distance5(self):
        self.assertTrue(string_distance(w1,w3,'jaccard') < 0.3)
    def test_string_distance6(self):
        self.assertTrue(string_distance(w4,w3,'jaccard') >= 0.7)


    def test_clean_txt(self):
        self.assertEqual(clean_txt(f1), ['essa', 'frase', 'sao', 'do', 'ocr'])

    def test_clean_txt2(self):
        self.assertEqual(clean_txt(f2), ['rodrigo', 'foi', 'jogar'])

if __name__ == '__main__':
    unittest.main()