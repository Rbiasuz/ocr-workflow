import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(   sum([2, 2]) , 4,  "should be 4"    )

    def test_sum2(self):
        self.assertNotEqual (   sum([1, 1]) , 3,  "should not be 3"    )

    def test_sum3(self):
        self.assertEqual(   sum([3, 3]) , 6,  "should be 6"   )

    def test_sum4(self):
        self.assertEqual(   sum([15, 15]) , 30,  "should be 30"   )


if __name__ == '__main__':
    unittest.main()
