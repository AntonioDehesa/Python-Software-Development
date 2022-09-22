import unittest
from compute_stats2 import compute_stats

class TestComputeStats(unittest.TestCase):
    def test_even_list(self):
        values = [1,2,3,4]
        res = compute_stats(values)
        self.assertEqual(res[0],1)#Min 
        self.assertEqual(res[1],4)#Max
        self.assertEqual(res[2],2.5)#Average
        self.assertEqual(res[3],2.5)#Median

    def test_odd_list(self):
        values = [1,2,3,4,5]
        res = compute_stats(values)
        self.assertEqual(res[0],1)#Min 
        self.assertEqual(res[1],5)#Max
        self.assertEqual(res[2],3)#Average
        self.assertEqual(res[3],3)#Median

    def test_empty_list(self):
        values = []
        res = compute_stats(values)
        self.assertIsNone(res)
    
    def test_list_one_element(self):
        values = [1]
        res = compute_stats(values)
        self.assertEqual(res,(1,1,1,1))#Every value should be the same
if __name__ == "__main__":
    unittest.main()