import unittest

import pandas as pd

from FileOperation import FileOperation


class TestFileOperation(unittest.TestCase):

    def setUp(self):
        self.file_op = FileOperation()
        self.test_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    def test_read_csv(self):
        # Create a test CSV file
        test_csv_file = 'test_data.csv'
        self.test_data.to_csv(test_csv_file, index=False)

        # Test reading from CSV
        data = self.file_op.read_csv(test_csv_file)
        self.assertEqual(data.equals(self.test_data), True)

    def test_write_to_csv(self):
        # Test writing to CSV
        test_output_file = 'test_output.csv'
        self.file_op.write_to_csv(self.test_data, test_output_file)

        # Read the written CSV file to check if the data was written correctly
        written_data = pd.read_csv(test_output_file)
        self.assertEqual(written_data.equals(self.test_data), True)


if __name__ == '__main__':
    unittest.main()