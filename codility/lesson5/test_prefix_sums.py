from prefix_sums import *
import unittest

class PrefixSums(unittest.TestCase):
    @unittest.skip
    def test_prefix_sums(self):
        A = [3, 4, 5, 6]
        print(A[1:2])
        P = prefix_sums(A)
        self.assertTrue(P[1], 3)
        self.assertTrue(P[2], 7)
        self.assertTrue(P[4],18)
    
    @unittest.skip
    def test_count_total(self):
         A = [3, 4, 5, 6]
         P = prefix_sums(A)
         print(P)
         sum = count_total(P,1,2)
         self.assertEqual(sum,  9)
         sum = count_total(P,1,3)
         self.assertEqual(sum,  15)
         sum = count_total(P,0,2)
         self.assertEqual(sum,  12)

    @unittest.skip
    def test_count_div(self):
        self.assertEqual(count_div(6,11,2), 3)
        self.assertEqual(count_div(0,20000,2), 10000)
        self.assertEqual(count_div(12,12,2), 1)
        # self.assertEqual(count_div(0,2_000_000_000,2), 1_000_000_000)

    @unittest.skip
    def test_compute_dna(self):
        P = [2,5, 0]
        Q = [4,5,6]
        dna = "CAGCCTA"
        result = compute_dna(dna,P,Q)
        expected = [2,4, 1 ]
        # self.assertListEqual(result, expected)
        

    def test_compute_dna_effecient(self):
        P = [2,5, 0]
        Q = [4,5,6]
        dna = "CAGCCTA"
        result = compute_dna_effecient(dna,P,Q)
        expected = [2,4, 1 ]
        # self.assertListEqual(result, expected)

        

if __name__ == "__main__":
    unittest.main()
