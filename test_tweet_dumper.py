import unittest
import tweet_dumper


class MyTest(unittest.TestCase):
    def test(self):
        all_handles= tweet_dumper.get_all_handles()
        self.assertEqual(all_handles[0],"@abenaopp")

    def test_correct_number_of_handles(self):
        all_handles= tweet_dumper.get_all_handles()
        self.assertEqual(len(all_handles),589)

if __name__ == '__main__':
    unittest.main()

