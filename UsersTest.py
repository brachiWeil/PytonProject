
import unittest
import os
import re
import itertools

from Users import check_file_exists, read_usernames_generator, RestrictedUserArray, even_index_users, read_emails, gmail_addresses, match_email_username, check_username, check_names, calculate_payment


class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_file = "test_users.txt"
        with open(self.test_file, "w") as file:
            file.write("user1\nuser2\nuser3\nuser4\nuser5\nuser6\nuser7\nuser8\nuser9\nuser10\n")

    def tearDown(self):
        # Remove the temporary file created for testing
        os.remove(self.test_file)

    def test_check_file_exists(self):
        # Test file existence
        self.assertTrue(os.path.exists(self.test_file))
        # Test file creation
        check_file_exists("nonexistent_file.txt")
        self.assertTrue(os.path.exists("nonexistent_file.txt"))

    def test_read_usernames_generator(self):
        # Test reading usernames from file
        expected_usernames = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10"]
        actual_usernames = list(read_usernames_generator(self.test_file))
        self.assertListEqual(expected_usernames, actual_usernames)

    # def test_restricted_user_array(self):
    #     # Test get_restricted_users method
    #     restricted_user_array = RestrictedUserArray(["user1", "user2", "user3", "user4", "user5"])
    #     restricted_users = restricted_user_array.get_restricted_users()
    #     print(restricted_users)  # Add this line to print the result
    #     self.assertEqual(restricted_users, ["user1", "user2"])

    def test_even_index_users(self):
        # Test even_index_users function
        self.assertEqual(even_index_users(["user1", "user2", "user3", "user4"]), ["user1", "user3"])

    def test_read_emails(self):
        # Test read_emails function
        with open("test_emails.txt", "w") as file:
            file.write("example1@gmail.com\ninvalidemail\nexample2@gmail.com")
        expected_emails = ["example1@gmail.com", "example2@gmail.com"]
        self.assertEqual(read_emails("test_emails.txt"), expected_emails)
        os.remove("test_emails.txt")

    def test_gmail_addresses(self):
        # Test gmail_addresses function
        emails = ["example1@gmail.com", "example2@hotmail.com", "example3@gmail.com"]
        self.assertEqual(gmail_addresses(emails), ["example1@gmail.com", "example3@gmail.com"])

    def test_match_email_username(self):
        # Test match_email_username function
        emails = ["example1@gmail.com", "example2@hotmail.com"]
        usernames = ["example1", "user2"]
        expected_result = {"example1@gmail.com": True, "example2@hotmail.com": False}
        self.assertDictEqual(match_email_username(emails, usernames), expected_result)

    # def test_check_username(self):
    #     # Test check_username function
    #     self.assertEqual(check_username("user1", self.test_file), (True, 1))

    def test_check_names(self):
        # Test check_names function
        self.assertTrue(check_names(["NAME1", "NAME2"]))
        self.assertFalse(check_names(["Name1", "NAME2"]))

    def test_calculate_payment(self):
        # Test calculate_payment function
        self.assertEqual(calculate_payment([8, 16, 24, 10, 12]), 100)


if __name__ == "__main__":
    unittest.main()
