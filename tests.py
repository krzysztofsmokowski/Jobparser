from feedhandler import FeedHandler
import unittest


class FeedHandlerTest(unittest.TestCase):
    def test_string_to_compare_not_true(self):
        fh = FeedHandler('justjoin.it/feed','Python', 'Poznan')
        list_of_jobs = 'abcd'
        list_to_compare = 'cbd'
        if bool(set(list_of_jobs).intersection(list_to_compare)):
            returned = 'affirmative'
        else:
            returned = 'not true'
        self.assertEqual('not true', returned)

    def test_string_to_compare_affirmative(self):
        fh = FeedHandler('justjoin.it/feed','Python', 'Poznan')
        list_to_compare = ['abcd']
        second_list_to_compare = ['abcd']
        if bool(set(list_to_compare).intersection(second_list_to_compare)):
            returned = 'affirmative'
        else:
            returned = 'not true'
        self.assertEqual('affirmative', returned)


if __name__ == '__main__':
    unittest.main()
