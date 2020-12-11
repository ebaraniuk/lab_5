import unittest
from progression import Progression


class TestProgression(unittest.TestCase):
    test = Progression(1, 3, 10)
    test2 = Progression(0, 2, 40)

    def test_i_element(self):
        self.assertEqual(self.test.i_element(8), 22)
        self.assertEqual(self.test.i_element(10), 28)
        self.assertEqual(self.test.i_element(1), 1)
        self.assertEqual(self.test2.i_element(1), 0)
        self.assertEqual(self.test2.i_element(10), 18)

    def test_summa(self):
        self.assertRaises(ValueError,self.test.summa,-1)
        self.assertEqual(self.test.summa(10), 145)
        self.assertTrue(self.test.summa(3), isinstance(self.test.summa(3), int))
        self.assertEqual(self.test2.summa(10), 90)


    def test_range(self):
        self.assertEqual(self.test.range_(3, 9), [7, 10, 13, 16, 19, 22, 25, 28])
        self.assertTrue(self.test.range_(3, 6), isinstance(self.test.range_(3, 6), list))
        self.assertTrue(self.test.range_(1, 10), isinstance(self.test.range_(1, 10), list))
        self.assertTrue(self.test2.range_(6,9), isinstance(self.test.range_(1, 10), list))

    def test_check_element(self):
        self.assertEqual(self.test.check_element(4), True)
        self.assertEqual(self.test.check_element(5), False)
        self.assertTrue(self.test.check_element(10), isinstance(self.test.check_element(10), bool))
        self.assertEqual(self.test2.check_element(6), True)
        self.assertEqual(self.test2.check_element(5), False)

if __name__ == '__main__':
    unittest.main()
