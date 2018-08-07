import unittest

from phonebook import Phonebook


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def tearDown(self):
        # to clean up
        pass

    def test_lookup_entry_by_name(self):
        print(id(self.phonebook))
        self.phonebook.add("Bob", "12345")
        # By convention first should go the expected values
        self.assertEqual("12345", self.phonebook.lookup("Bob"))

    def test_missing_raises_KeyErro(self):
        print(id(self.phonebook))
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("poor exampless")
    # if one the assert fails, fails the test case
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())

        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

        self.phonebook.add("Sue", "12345")
        self.assertFalse(self.phonebook.is_consistent())

        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_entries_is_inconsistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "123")
        self.assertFalse(self.phonebook.is_consistent())

