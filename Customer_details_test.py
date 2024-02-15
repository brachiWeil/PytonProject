import unittest
from datetime import datetime
from io import StringIO
from unittest.mock import patch

import pandas as pd

from Customer_details import Customer_details


class TestCustomerDetails(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Customer_details class
        self.sales_data = pd.DataFrame({"Product": ["Sidur", "Book", "Pen"],
                                        "Quantity": [10, 20, 30],
                                        "Total": [100, 200, 300]})
        self.sales_data_cust = Customer_details(self.sales_data)

    # def test_handle_error(self):
    #     # Prepare the error object
    #     error = ValueError("Test error")
    #
    #     # Define expected outputs
    #     timestamp = datetime.now().strftime("%d.%m.%y, %H:%M")
    #     author = "brachi&dvority"
    #     error_msg = "Invalid value entered."
    #
    #     # Redirect standard output to capture printed output
    #     with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
    #         # Call the handle_error method
    #         Customer_details.handle_error(error)
    #
    #         # Get the printed output
    #         output = mock_stdout.getvalue().strip()
    #
    #     # Check if the printed output matches the expected format and content
    #     expected_output = f"<{author}, {timestamp}> {error_msg} <{author}>"
    #     self.assertEqual(output, expected_output)
    #
    #     # Check if the log file is updated correctly
    #     with open("error_log.txt", "r") as log_file:
    #         log_content = log_file.read().strip()
    #     self.assertIn(expected_output, log_content)

    def test_generate_random_sales(self):
        # Test the generate_random_sales method

        # Test when data for the specified product exists
        product_name = "Sidur"
        self.sales_data_cust.generate_random_sales(product_name)

        # Additional tests for possible outputs:
        # 1. Check that the output is formatted correctly (as per the explanation)
        # 2. Check that the output matches the data in the CSV

        # Test when no data for the specified product exists
        product_name = "Notebook"
        self.sales_data_cust.generate_random_sales(product_name)
        # Check if it prints "No data for product: Notebook"

    def test_print_python_version(self):
        # Test the print_python_version method
        # Redirect standard output to capture printed output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            Customer_details.print_python_version()
            output = out.getvalue().strip()
            self.assertEqual(output, f"Python version: {sys.version}")
        finally:
            sys.stdout = saved_stdout

        # Additional tests for possible outputs:
        # 1. Check that the output is formatted correctly (as per the explanation)

    def test_process_parameters(self):
        # Test the process_parameters method
        args = (10, "NAME=kali", "NAME=John", 5.5, "AGE=30")
        result = self.sales_data_cust.process_parameters(*args)
        expected_result = {'NAME': 'John', 'AGE': '30'}
        self.assertEqual(result, expected_result)

        # Additional tests for possible outputs:
        # 1. Check that the output is formatted correctly (as per the explanation)

    def test_print_head_tail_rand(self):
        # Test the print_head_tail_rand method
        # Redirect standard output to capture printed output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.sales_data_cust.print_head_tail_rand()
            output = out.getvalue().strip()
            # Check if the output contains the first 3 rows, last 2 rows, and a random row
            self.assertIn("Product", output)  # Assuming "Product" is part of the output
            self.assertIn("Quantity", output)  # Assuming "Quantity" is part of the output
            self.assertIn("Total", output)  # Assuming "Total" is part of the output
        finally:
            sys.stdout = saved_stdout

        # Additional tests for possible outputs:
        # 1. Check that the output is formatted correctly (as per the explanation)
        # 2. Check that the output matches the data in the CSV

    def test_process_numeric_columns(self):
        # Test the process_numeric_columns method
        # Redirect standard output to capture printed output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.sales_data_cust.process_numeric_columns()
            output = out.getvalue().strip()
            # Check if the output contains information about numeric columns
            self.assertIn("Column", output)  # Assuming "Column" is part of the output
            self.assertIn("Total", output)  # Assuming "Total" is part of the output
            self.assertIn("Average", output)  # Assuming "Average" is part of the output
        finally:
            sys.stdout = saved_stdout

        # Additional tests for possible outputs:
        # 1. Check that the output is formatted correctly (as per the explanation)
        # 2. Check that the output matches the data in the CSV


if __name__ == '__main__':
    unittest.main()
