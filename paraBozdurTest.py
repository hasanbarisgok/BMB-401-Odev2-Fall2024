'''
Created on Oct 18, 2024
Modified on Nov 7, 2024

@author: Hasan Baris GOK
'''
import unittest
import paraBozdur as pb


class Test(unittest.TestCase):

    def testParaBozdurWithBanknot(self):

        # The tests, which should be work and returns a result.

        result_1 = pb.paraBozdur(3.26)
        print(f"For Value (3.26): {result_1}")
        self.assertListEqual([0, 0, 0, 3, 1, 0, 0, 1], result_1)

        result_2 = pb.paraBozdur(5)
        print(f"For Value (5): {result_2}")
        self.assertListEqual([0, 0, 1, 0, 0, 0, 0, 0], result_2)

        result_3 = pb.paraBozdur(36.41)
        print(f"For Value (36.41): {result_3}")
        self.assertListEqual([1, 1, 1, 1, 1, 1, 1, 1], result_3)

        result_4 = pb.paraBozdur(1.001)
        print(f"For Value (1.001): {result_4}")
        self.assertListEqual([0, 0, 0, 1, 0, 0, 0, 0], result_4)

        # The tests, which should be work, but have to print an empty list result.
        result_5 = pb.paraBozdur(-5)
        print(f"For Value (-5): {result_5}")
        self.assertListEqual([], result_5)  # Inputs which are number, but negative

        result_6 = pb.paraBozdur(150)
        print(f"For Value (150): {result_6}")
        self.assertListEqual([], result_6)  # Inputs which are number, but bigger than 100

        result_7 = pb.paraBozdur("abc")
        print(f"For Value (\"abc\"): {result_7}") 
        self.assertListEqual([], result_7)  #Inputs which are string.

        result_8 = pb.paraBozdur(None)
        print(f"For Value (None): {result_8}")
        self.assertListEqual([], result_8)  # Inputs which are none type.
        
if __name__ == '__main__':
    unittest.main()
