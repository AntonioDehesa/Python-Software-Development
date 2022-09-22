import unittest

class TestMax(unittest.TestCase):
    def test_one_element(self):
        with self.assertRaises(TypeError):
            max(5)

    def test_no_elements(self):
        with self.assertRaises(TypeError):
            max()

    def test_two_elements_equal(self):
        self.assertEqual(max(5,5),5)

    def test_two_elements_first_greater(self):
        self.assertEqual(max(6,5),6)

    def test_two_elements_second_greater(self):
        self.assertEqual(max(5,6),6)

    def test_three_elements_first_greater(self):
        self.assertEqual(max(3,2,1),3)

    def test_three_elements_second_greater(self):
        self.assertEqual(max(1,3,2),3)

    def test_three_elements_equal(self):
        self.assertEqual(max(3,3,3),3)

    def test_three_elements_third_greater(self):
        self.assertEqual(max(1,2,3),3)

    def test_multiple_elements_equal(self):
        self.assertEqual(max(1,1,1,1,1,1,1,1),1)

    def test_multiple_elements(self):
        self.assertEqual(max(1,2,3,4,5,6,7,8,9,10),10)

    def test_list_empty(self):
        with self.assertRaises(ValueError):
            max([])

    def test_list_equal(self):
        self.assertEqual(max([1,1,1,1]),1)

    def test_list(self):
        self.assertEqual(max([1,2,3,4]),4)

    def test_string(self):
        self.assertEqual(max("s","d"),"s")
    
    def test_different_types(self):
        with self.assertRaises(TypeError):
            max("s",3)


if __name__ == "__main__":
    unittest.main()