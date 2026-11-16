import unittest
from main import pivot


class PivotTests(unittest.TestCase):
    def test_sum_pivot(self):
        rows = [
            {"region":"north","quarter":"q1","sales":"2"},
            {"region":"north","quarter":"q1","sales":"3"},
            {"region":"south","quarter":"q2","sales":"4"},
        ]
        result = pivot(rows, "region", "quarter", "sales", "sum")
        self.assertEqual(result[0], ["", "q1", "q2"])
        self.assertEqual(result[1], ["north", 5.0, ""])
        self.assertEqual(result[2], ["south", 0, 4.0])

    def test_count(self):
        self.assertEqual(pivot([{"a":"x","b":"y"}], "a", "b"), [["", "y"], ["x", 1]])


if __name__ == "__main__":
    unittest.main()
