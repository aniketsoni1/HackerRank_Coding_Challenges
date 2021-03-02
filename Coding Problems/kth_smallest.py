import unittest


def kth_smallest(a, k=2):
    # print(a)
    a.sort()
    # b.sort()
    # a = sorted(a, reverse=True)
    # print(a[2])
    if len(a) >= k:
        return a[k]
    else:
        return None


class Test(unittest.TestCase):

    def test_1(self):
        expected_output = 2
        actual_output = kth_smallest(a=[1, 9, 2, 0, 5])
        self.assertEqual(actual_output, expected_output)

    def test_2(self):
        expected_output = 3
        actual_output = kth_smallest(a=[1, 4, 3, 5, 2])
        self.assertEqual(actual_output, expected_output)  # 3

    def test_3(self):
        expected_output = 3
        actual_output = kth_smallest(a=[1, 3, 5, 8, 2])
        self.assertEqual(actual_output, expected_output)  # 3

    def test_4(self):
        expected_output = None
        actual_output = kth_smallest(a=[1])
        self.assertEqual(actual_output, expected_output)  # None

    def test_5(self):
        expected_output = 2
        actual_output = kth_smallest(a=[1, 3, 5, 8, 2], k=1)
        self.assertEqual(actual_output, expected_output) # 2

    def test_6(self):
        expected_output = 1
        actual_output = kth_smallest(a=[1], k=0)
        self.assertEqual(actual_output, expected_output) # 1


class Test2(unittest.TestCase):

    def test_1(self):
        expected_output = 3
        actual_output = kth_smallest(a=[1, 4, 3, 5, 2])
        self.assertEqual(actual_output, expected_output)  # 3

    def test_2(self):
        expected_output = 3
        actual_output = kth_smallest(a=[1, 3, 5, 8, 2])
        self.assertEqual(actual_output, expected_output)  # 3


if __name__ == '__main__':
    unittest.main()
