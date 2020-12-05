import unittest

from Operations.operations import Operations


class TestOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Operations.addition("3243124", "2342434", 5), "11141113")
        self.assertEqual(Operations.addition("34ACD56EF3", "A34DC56EF", 16), "3EE1B1C5E2")
        self.assertEqual(Operations.addition("A34562B3", "345BA21A", 12), "117A54511")
        self.assertEqual(Operations.addition("10010111010100100111", "10100111010101000101", 2),
                         "100111110101001101100")

    def test_subtraction(self):
        self.assertEqual(Operations.subtraction("45462353", "23532532", 7), "21626521")
        self.assertEqual(Operations.subtraction("DA735FC29", "B95A352F3", 16), "21192A936")
        self.assertEqual(Operations.subtraction("A5429C4B", "9B6C3016", 14), "7B46C35")
        self.assertEqual(Operations.subtraction("2121012011200110", "1200100201010211", 3), "220211110112122")

    def test_multiplication(self):
        self.assertEqual(Operations.multiplication("3535025205321", "4", 6), "23432153234124")
        self.assertEqual(Operations.multiplication("B79AD34EF12", "D", 16), "952DCBB023EA")
        self.assertEqual(Operations.multiplication("756542710273", "6", 8), "5630121262142")
        self.assertEqual(Operations.multiplication("AC4539B45", "A", 13), "85650B794B")

    def test_division(self):
        self.assertEqual(Operations.division_op("313232123321", "2", 4), ("123313031330", "1"))
        self.assertEqual(Operations.division_op("CE8347EF34AB", "A", 16), ("14A6BA64B877", "5"))
        self.assertEqual(Operations.division_op("A9803948B34", "8", 12), ("1426058114B", "0"))
        self.assertEqual(Operations.division_op("736523752113", "5", 8), ("137567142017", "0"))