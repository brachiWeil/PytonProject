
import unittest
import pandas as pd
from SalesData import SalesData


class TestSalesData(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
            'Product': ['A', 'B', 'C'],
            'Price': [100, 200, 150],
            'Date': pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-03']),
            'Quantity': [1, 2, 3]
        })
        self.sales_data = SalesData(self.sample_data)

    def test_eliminate_duplicates(self):
        self.sales_data.eliminate_duplicates()
        self.assertEqual(len(self.sales_data.data), len(set(self.sales_data.data.index)))
        self.assertFalse(self.sales_data.data.isnull().values.any())

    def test_calculate_total_sales(self):
        total_sales = self.sales_data.calculate_total_sales()
        self.assertIsInstance(total_sales, pd.Series)
        self.assertEqual(len(total_sales), 3)
        # Add more specific assertions if needed

    def test_calculate_total_sales_per_month(self):
        self.sales_data.data['Date'] = pd.to_datetime(['2022-01-01', '2022-02-01', '2022-03-01'])
        total_sales_per_month = self.sales_data.calculate_total_sales_per_month()
        self.assertIsInstance(total_sales_per_month, pd.Series)
        self.assertEqual(len(total_sales_per_month), 3)

    def test_identify_best_selling_product(self):
        best_selling_product = self.sales_data.identify_best_selling_product()
        self.assertIsInstance(best_selling_product, str)
        # Add more specific assertions if needed

    # def test_identify_month_with_highest_sales(self):
    #     month_with_highest_sales = self.sales_data.identify_month_with_highest_sales()
    #     self.assertIsInstance(month_with_highest_sales, int)  # Assuming month is returned as integer
    #     # Add more specific assertions if needed

    def test_analyze_sales_data(self):
        result = self.sales_data.analyze_sales_data()
        self.assertIsInstance(result, dict)
        # Add more specific assertions if needed

    # def test_calculate_cumulative_sales(self):
    #     cumulative_sales = self.sales_data.calculate_cumulative_sales()
    #     self.assertIsInstance(cumulative_sales, pd.Series)
    #     # Add more specific assertions if needed

    def test_bar_chart_category_sum(self):
        # No assertions needed for plotting functions
        self.sales_data.bar_chart_category_sum()

    def test_filter_by_sellings_or_and(self):
        filtered_data = self.sales_data.filter_by_sellings_or_and()
        self.assertIsInstance(filtered_data, pd.DataFrame)
        # Add more specific assertions if needed

    def test_divide_by_2(self):
        # No assertions needed for plotting functions
        self.sales_data.divide_by_2()

    def test_calculate_stats(self):
        stats_dict = self.sales_data.calculate_stats()
        self.assertIsInstance(stats_dict, dict)
        # Add more specific assertions if needed

    def test_categorize_prices(self):
        # No assertions needed for plotting functions
        self.sales_data.categorize_prices()

    def test_filter_by_mask(self):
        mask_list = [True, False, True]  # Example mask
        filtered_data = self.sales_data.filter_by_mask(mask_list)
        self.assertIsInstance(filtered_data, pd.DataFrame)
        # Add more specific assertions if needed


if __name__ == '__main__':
    unittest.main()
