import unittest


class TestWorkflow(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_to_fail(self):
	    self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
