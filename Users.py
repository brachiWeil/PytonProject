import os
import re
import itertools

from FileOperation import FileOperation

    # תרגיל 8
def check_file_exists(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            pass


def read_usernames_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

    # 3


class RestrictedUserArray:
    def __init__(self, users):
        self.users = users

    def get_restricted_users(self):
        try:
            restricted_users_count = int(0.1 * sum(1 for _ in self.users))
            self.users, restricted_user = itertools.tee(self.users)
            return list(itertools.islice(restricted_user, restricted_users_count))
        except Exception as e:
            print("error")

    def get_even_row_users(self):
        even_row = [u for idx, u in enumerate(self.users) if idx % 2 == 0]
        return even_row


file_op = FileOperation()
all_users = file_op.read_csv("UsersName.txt")
restricted_user_array = RestrictedUserArray(all_users)
restricted_users = restricted_user_array.get_restricted_users()
print("Restricted Users:")
for user in restricted_users:
    print(user)
    # 4
    even_row_users = restricted_user_array.get_even_row_users()
    print("\nEven Row Users:")
    for u in even_row_users:
        print(user)


def even_index_users(users):
    return [user for index, user in enumerate(users) if index % 2 == 0]


# 5
def read_emails(filepath):
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    valid_emails = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                email = line.strip()
                if re.match(regex, email):
                    valid_emails.append(email)
                else:
                    print(f"Invalid email found: {email}")
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
    return valid_emails


# 6
def gmail_addresses(emails):
    gmails = [email for email in emails if email.endswith("@gmail.com")]
    return gmails


# 7
def match_email_username(emails, usernames):
    email_username_match = {}
    for email in emails:
        for username in usernames:
            if username.lower() in email.lower():
                email_username_match[email] = True
                break
        else:
            email_username_match[email] = False
    return email_username_match


# Task 8
def check_username(username, filepath):
    # Possible formats
    formats = [
        lambda name: name,  # Regular name
        lambda name: ''.join(str(ord(char)) for char in name),  # ASCII code
        lambda name: ''.join(chr(ord(char) + 13) if char.isalpha() else char for char in name)
    ]

    # Check if the username is in the list
    with open(filepath, "r") as f:
        usernames = (line.strip() for line in f)
        in_list = username.lower() in (username.lower() for username in usernames)

    # Check the number of occurrences of the letter A
    repetitions = 0
    for f in formats:
        converted_name = f(username)
        repetitions += converted_name.lower().count('a')
    return in_list, repetitions


# 9
def check_names(names):
    return all(map(str.isupper, names))


# task10
def calculate_payment(team_purchase):
    rounded_users = [user for user in team_purchase if user % 8 == 0]
    non_rounded_users = [user for user in team_purchase if user not in rounded_users]
    additional_payment = len(non_rounded_users) * 50
    return additional_payment


def main():
    # Task 1
    check_file_exists("UsersName2.txt")
    check_file_exists("UsersEmail2.txt")

    # Task 2
    usernames_generator = read_usernames_generator("UsersName.txt")
    usernames_generator = list(usernames_generator)
    print(usernames_generator)

    # task5
    valid_emails = read_emails("UsersEmail.txt")
    print("Valid email addresses:", valid_emails)
    # 6
    # Call the function in the main() function after reading and validating emails
    usernames_list = list(usernames_generator)

    gmails = gmail_addresses(valid_emails)
    print("Gmail addresses:", gmails)
    # 7
    email_username_match = match_email_username(valid_emails, usernames_list)
    print("Email-Username Match:", email_username_match)
    # Task 8
    username = "Chana"
    in_list, repetitions = check_username(username, "UsersName.txt")
    if in_list:
        print(f"Username '{username}' is present in the list.")
    else:
        print(f"Username '{username}' is not present in the list.")

    print(f"The letter A appears in the username '{username}' {repetitions} times.")

    # Task 9
    names = ["ALICE", "BOB", "ALICE"]
    all_names_are_uppercase = check_names(names)
    print("All names are in uppercase:", all_names_are_uppercase)

    # task 10
    team_purchase = [88, 24, 8, 15, 20, 76, 88, 4, 43, 19, 5, 9]
    total_additional_payment = calculate_payment(team_purchase)
    print("Total additional payment for non-rounded users:", total_additional_payment)


if __name__ == "__main__":
    main()
