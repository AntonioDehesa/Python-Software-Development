from typing import Iterable
import unittest
from autompg2 import *
from os import path
from collections.abc import Iterable
from argparse import ArgumentError, ArgumentTypeError

class TestComputeStats(unittest.TestCase):
    # Tests for AutoMPG
    def test_create_AutoMPG(self):
        temp_AutoMPG = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertIsInstance(temp_AutoMPG, AutoMPG)

    def test_AutoMPG_features(self):
        temp_AutoMPG = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertEqual(temp_AutoMPG.make, "chevrolet")
        self.assertEqual(temp_AutoMPG.model, "chevelle malibu")
        self.assertEqual(temp_AutoMPG.year, 1970)
        self.assertEqual(temp_AutoMPG.mpg, 18.0)
    
    def test_AutoMPG_repr(self):
        temp_AutoMPG = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertEqual("AutoMPG(make= \"chevrolet\", model= \"chevelle malibu\", year= 1970, mpg= 18.0)", repr(temp_AutoMPG))
    
    def test_AutoMPG_str(self):
        temp_AutoMPG = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertEqual("make= \"chevrolet\", model= \"chevelle malibu\", year= 1970, mpg= 18.0", str(temp_AutoMPG))

    def test_AutoMPG_eq_true(self):
        temp_AutoMPG = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        temp_AutoMPG2 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertEqual(temp_AutoMPG, temp_AutoMPG2)

    def test_AutoMPG_eq_false(self):
        temp_AutoMPG = AutoMPG("chevrolet", "chevelle malibu", 1969, 18.0)
        temp_AutoMPG2 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertNotEqual(temp_AutoMPG, temp_AutoMPG2)
    
    def test_AutoMPG_lt_actually_equal(self):
        temp_AutoMPG = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        temp_AutoMPG2 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertFalse(temp_AutoMPG < temp_AutoMPG2)

    def test_AutoMPG_lt_1(self):
        temp_AutoMPG = AutoMPG("a", "chevelle malibu", 1970, 18.0)
        temp_AutoMPG2 = AutoMPG("b", "chevelle malibu", 1970, 18.0)
        self.assertTrue(temp_AutoMPG < temp_AutoMPG2)
    def test_AutoMPG_lt_2(self):
        temp_AutoMPG = AutoMPG("a", "a", 1970, 18.0)
        temp_AutoMPG2 = AutoMPG("a", "b", 1970, 18.0)
        self.assertTrue(temp_AutoMPG < temp_AutoMPG2)

    def test_AutoMPG_lt_3(self):
        temp_AutoMPG = AutoMPG("a", "a", 1969, 18.0)
        temp_AutoMPG2 = AutoMPG("a", "a", 1970, 18.0)
        self.assertTrue(temp_AutoMPG < temp_AutoMPG2)
    
    def test_AutoMPG_lt_4(self):
        temp_AutoMPG = AutoMPG("a", "a", 1970, 17.0)
        temp_AutoMPG2 = AutoMPG("a", "a", 1970, 18.0)
        self.assertTrue(temp_AutoMPG < temp_AutoMPG2)
    
    def test_AutoMPG_hash_true(self):
        temp_AutoMPG = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        temp_AutoMPG2 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertEqual(hash(temp_AutoMPG), hash(temp_AutoMPG2))

    def test_AutoMPG_hash_false(self):
        temp_AutoMPG = AutoMPG("chevroletv", "chevelle malibu", 1970, 18.0)
        temp_AutoMPG2 = AutoMPG("chevrolet", "chevelle malibu", 1970, 18.0)
        self.assertNotEqual(hash(temp_AutoMPG), hash(temp_AutoMPG2))
    # Tests for AutoMPGData
    def test_AutoMPGData_load_data_and_clean_data(self):
        a = AutoMPGData()
        self.assertIsInstance(a, AutoMPGData)
        self.assertTrue(path.exists("auto-mpg.clean.txt"))
    
    def test_AutoMPGData_iter(self):
        self.assertTrue(isinstance(iter(AutoMPGData()), Iterable))
    
    def test_sort_by_default(self):
        temp_AutoMPGData = AutoMPGData()
        temp_AutoMPGData.sort_by_default()
        for x in range(len(temp_AutoMPGData.data)-1):# Checks that each element is greater than the previous element
            self.assertGreaterEqual(temp_AutoMPGData.data[x+1], temp_AutoMPGData.data[x])

    def test_sort_by_year(self):
        temp_AutoMPGData = AutoMPGData()
        temp_AutoMPGData.sort_by_year()
        for x in range(len(temp_AutoMPGData.data)-1):# Checks that each element is greater than the previous element, by year
            self.assertGreaterEqual(temp_AutoMPGData.data[x+1].year, temp_AutoMPGData.data[x].year)
    
    def test_sort_by_mpg(self):
        temp_AutoMPGData = AutoMPGData()
        temp_AutoMPGData.sort_by_mpg()
        for x in range(len(temp_AutoMPGData.data)-1):# Checks that each element is greater than the previous element, by year
            self.assertGreaterEqual(temp_AutoMPGData.data[x+1].mpg, temp_AutoMPGData.data[x].mpg)
    @unittest.skip # We skip this test for now, as to not make too many requests to the servers
    def test_download_data(self):
        from os import remove # We import this method here, as it would be dangerous to allow it to be available anywhere else
        remove("auto-mpg.clean.txt")
        del remove
        self.assertFalse(path.exists("auto-mpg.clean.txt"))
        temp_autompgData = AutoMPGData()
        self.assertTrue(path.exists("auto-mpg.clean.txt"))
            
    def test_argparse_print(self):
        args = ["print"]
        res = parser(args)
        self.assertTrue(res.print == "print")

    def test_argparse_sort_year(self):
        args = ["-s", "year", "print"]
        res = parser(args)
        self.assertTrue(res.sortOrder == "year")

    def test_argparse_sort_mpg(self):
        args = ["-s", "mpg", "print"]
        res = parser(args)
        self.assertTrue(res.sortOrder == "mpg")

    def test_argparse_sort_default(self):
        args = ["-s", "default", "print"]
        res = parser(args)
        self.assertTrue(res.sortOrder == "default")
    
    def test_argparse_sort_incorrect(self):
        args = ["-s", "gg", "print"]
        with self.assertRaises((ArgumentError, ArgumentTypeError, SystemExit)):
            res = parser(args)
    
    def test_argparse_empty(self):
        args = []
        with self.assertRaises((ArgumentError, ArgumentTypeError, SystemExit)):
            res = parser(args)
if __name__ == "__main__":
    unittest.main()