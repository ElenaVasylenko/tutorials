"""
1. Create your inputs
2. Execute the code being tested, capturing the output
3. Compare the output with an expected result

.assertEqual(a, b)	a == b
.assertTrue(x)	bool(x) is True
.assertFalse(x)	bool(x) is False
.assertIs(a, b)	a is b
.assertIsNone(x)	x is None
.assertIn(a, b)	a in b
.assertIsInstance(a, b)
.assertRaises(TypeError)
"""

import unittest
from parameterized import parameterized
from function_for_test import sum


class TestSum(unittest.TestCase):
    @parameterized.expand([
        [[1, 2, 3], 6 ],
        [[1, 2, 3, 7], 13],
        [[1, 2, 3, 2], 8],
    ])
    def test_sum(self, data, expected_result):
        result = sum(data)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()