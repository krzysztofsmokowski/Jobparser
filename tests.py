from feedhandler import FeedHandler
import unittest


class FeedHandlerTest(unittest.TestCase):
    def test_string_to_compare_not_true(self):
        fh = FeedHandler('justjoin.it/feed','Python', 'Poznan')
        str_of_jobs = 'abcd'
        str_to_compare = 'cbd'
        if str_of_jobs == str_to_compare:
            returned = 'affirmative'
        else:
            returned = 'not true'
        self.assertEqual('not true', returned)

    def test_string_to_compare_affirmative(self):
        fh = FeedHandler('justjoin.it/feed','Python', 'Poznan')
        str_of_jobs = 'abcd'
        str_to_compare = 'abcd'
        if str_of_jobs == str_to_compare:
            returned = 'affirmative'
        else:
            returned = 'not true'
        self.assertEqual('affirmative', returned)


if __name__ == '__main__':
    unittest.main()
