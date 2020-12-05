import unittest

from Conversions.conversions import Conversions


class TestConversions(unittest.TestCase):
    def test_rapid_conversions(self):
        self.assertEqual(Conversions.rapid_conversions("ABDEC345ACD", 16, 8), "253675415055315")
        self.assertEqual(Conversions.rapid_conversions("ABDEC34", 16, 4), "22233132300310")
        self.assertEqual(Conversions.rapid_conversions("BA34DF", 16, 2), "101110100011010011011111")
        self.assertEqual(Conversions.rapid_conversions("725472346", 8, 2), "111010101100111010011100110")
        self.assertEqual(Conversions.rapid_conversions("5456527", 8, 4), "11211311113")
        self.assertEqual(Conversions.rapid_conversions("732642357654", 8, 16), "ED689DFAC")

    def test_substitution_method(self):
        self.assertEqual(Conversions.substitution_method("423432412", 5, 8), "6625205")
        self.assertEqual(Conversions.substitution_method("525427350031", 9, 12), "2820974AB31")
        self.assertEqual(Conversions.substitution_method("AB34C568", 13, 16), "28A3FBDF")

    def test_successive_divisions(self):
        self.assertEqual(Conversions.successive_divisions("A345B12A3", 12, 7), "214356406512")
        self.assertEqual(Conversions.successive_divisions("1242352", 7, 2), "100111011111001001")
        self.assertEqual(Conversions.successive_divisions("EFA79BC", 16, 9), "574764506")

    def test_base_10_as_intermediate(self):
        self.assertEqual(Conversions.base_10_as_intermediate("A345B12A3", 12, 7), "214356406512")
        self.assertEqual(Conversions.base_10_as_intermediate("1242352", 7, 2), "100111011111001001")
        self.assertEqual(Conversions.base_10_as_intermediate("EFA79BC", 16, 9), "574764506")
        self.assertEqual(Conversions.substitution_method("423432412", 5, 8), "6625205")
        self.assertEqual(Conversions.substitution_method("525427350031", 9, 12), "2820974AB31")
        self.assertEqual(Conversions.substitution_method("AB34C568", 13, 16), "28A3FBDF")
