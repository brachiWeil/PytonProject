import sys
from datetime import datetime
import random
from functools import wraps
from collections import namedtuple

import numpy as np
import pandas as pd
from FileOperation import FileOperation

# תרגיל 7
class Customer_details:

    def __init__(self, data):
        self.data = data

    def handle_error(error: Exception) -> None:

        # רישום הודעת שגיאה:
        timestamp = datetime.now().strftime("%d.%m.%y, %H:%M")
        author = "brachi&dvority"
        error_type = type(error).__name__

        # התאמת הודעות שגיאה ספציפיות:
        if error_type == "ValueError":
            error_msg = "הערך שהוזן אינו תקין."
        elif error_type == "KeyError":
            error_msg = "המפתח שהוזן אינו קיים."
        elif error_type == "FileNotFoundError":
            error_msg = "קובץ לא נמצא בנתיב."
        else:
            error_msg = f"שגיאה לא ידועה: {str(error)}"

        # הדפסת הודעת שגיאה:
        print(f"<{author}, {timestamp}> {error_msg} <{author}>\n")
        with open("error_log.txt", "a") as file:
            file.write(f"<{author}, {timestamp}> {error_msg} <{author}>\n")

    def generate_random_sales(self, product_name):
        product_sales_data = self.data[self.data['Product'] == product_name]
        if not product_sales_data.empty:
            random_sales = np.random.randint(product_sales_data['Quantity'].min(),
                                             product_sales_data['Quantity'].max() + 1)
            random_amount_paid = np.random.uniform(product_sales_data['Total'].min(), product_sales_data['Total'].max())
            print(f"Product: {product_name}")
            print(f"Random Sales: {random_sales}")
            print(f"Random Amount Paid: {random_amount_paid}")
        else:
            print(f"No data for product: {product_name}")
    @staticmethod
    def print_python_version():
        """
        This function prints the Python version.
        """
        print(f"Python version: {sys.version}")

    def process_parameters(*args):

        params = {}
        for arg in args:
            if isinstance(arg, str):
                # Parameter with tag
                tag, value = arg[0:].split("=")
                params[tag] = value
            else:
                # Parameter without tag
                if isinstance(arg, int) or isinstance(arg, float):
                    # Print value if it is a number
                    print(arg)
        return params

    # ____________________

    def print_head_tail_rand(self):

        try:
            # Print the first 3 rows
            print(self.data.head(3))

            # Print the last 2 rows
            print(self.data.tail(2))

            # Print a random row
            random_row = random.randint(0, len(self.data) - 1)
            print(self.data.iloc[random_row])
        except Exception as e:
            print(f"An error occurred: {e}")

    # 7
    from functools import wraps
    def process_numeric_columns(self):
        df = pd.DataFrame(self.data)
        numeric_columns = df.select_dtypes(include='number')
        for column in numeric_columns:
            total = df[column].sum()
            average = df[column].mean()
            print(f"Column: {column}")
            print(f"Total: {total}")
            print(f"Average: {average}")
            print("-" * 30)



