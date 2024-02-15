import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from FileOperation import FileOperation


# import pylot as plt


class SalesData:
    def __init__(self, data):
        self.data = data

    file_op = FileOperation()

    # 2.4
    def eliminate_duplicates(self):
        file_op = FileOperation()

        try:
            # self.data = self.data.drop_duplicates().dropna()
            file_op.write_to_csv(self.data.drop_duplicates().dropna(), "YafeNof.csv")
            print("Duplicate rows have been successfully removed.")
        except Exception as e:
            print(f"An error occurred while removing duplicate rows: {str(e)}")

    # 2.5
    def calculate_total_sales(self):

        try:
            total_sales_per_product = self.data.groupby('Product').apply(lambda x: (x['Price'] * x['Quantity']).sum())
            return total_sales_per_product
        except Exception as e:
            print(f"An error occurred while calculating total sales per product: {str(e)}")

    # 2.6
    def calculate_total_sales_per_month(self):

        try:
            # self.data['Date'] = pd.to_datetime(self.data['Date'])
            self.data['Month'] = self.data['Date'].dt.month
            total_sales_per_month = self.data.groupby('Month').apply(lambda x: (x['Price'] * x['Quantity']).sum())
            return total_sales_per_month
        except Exception as e:
            print(f"An error occurred while calculating total sales per month: {str(e)}")

    # 2.7
    def identify_best_selling_product(self):

        try:
            best_selling_product = self.data.groupby('Product')['Quantity'].sum().idxmax()
            return best_selling_product
        except Exception as e:
            print(f"An error occurred while identifying the best-selling product: {str(e)}")

    # 2.8.idxmin(),
    #                          # 'average_sales_per_month': self.calculate_total_sales_per_month().mean()
    def identify_month_with_highest_sales(self):
        try:
            total_sales_per_month = self.calculate_total_sales_per_month()
            if not isinstance(total_sales_per_month, pd.Series):
                raise ValueError("Output of calculate_total_sales_per_month must be a pandas Series.")

            # 1. Line plot
            plt.figure(figsize=(10, 6))
            plt.plot(total_sales_per_month.index, total_sales_per_month.values, label='Total Sales', color='skyblue')
            plt.xlabel('Month')
            plt.ylabel('Total Sales')
            plt.title('Total Sales per Month')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            plt.legend()
            plt.show()

            return total_sales_per_month.idxmax()
        except Exception as e:
            print(f"An error occurred while identifying the month with the highest sales: {str(e)}")
            return None

    # 2.9,10
    def analyze_sales_data(self):
        analysis_dict = {'best_selling_product': self.identify_best_selling_product(),
                         'month_with_highest_sales': self.identify_month_with_highest_sales(),
                         'minitest_selling_product': self.data.groupby('Product')['Quantity'].sum()
                         }
        return analysis_dict

    # 3.11
    def calculate_cumulative_sales(self):
        try:
            cumulative_sales = self.data.groupby(['Product', 'Month'])['Quantity'].sum().groupby('Product').cumsum()
            return cumulative_sales
        except Exception as e:
            print(f"An error occurred while calculating cumulative sales: {str(e)}")

    # 3.12------
    # 3.13
    def bar_chart_category_sum(self):

        try:
            # 1. Group data by product and sum quantities
            product_quantity_sum = self.data.groupby('Product')['Quantity'].sum()

            # 2. Create a bar chart
            plt.figure(figsize=(10, 6))
            plt.bar(product_quantity_sum.index, product_quantity_sum.values, color='skyblue')
            plt.xlabel('Product')
            plt.ylabel('Quantity Sum')
            plt.title('Quantity Sum for Each Product')
            plt.xticks(rotation=45)  # Rotate X-axis labels for better readability
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"An error occurred while creating bar chart: {str(e)}")

    def calculate_mean_quantity(self):

        try:
            # Calculate the Total column
            self.data['Total'] = self.data['Price'] * self.data['Quantity']

            # Calculate mean, median, and second max
            mean = np.mean(self.data['Total'])
            median = np.median(self.data['Total'])
            second_max = np.partition(self.data['Total'], -2)[-2]  # Second maximum using partitioning

            # Visualize the distribution of 'Total' using Seaborn lmplot
            sns.lmplot(data=self.data, x='Price', y='Quantity', fit_reg=False)
            plt.title('Scatter Plot of Price vs Quantity')
            plt.xlabel('Price')
            plt.ylabel('Quantity')
            plt.grid(True)
            plt.show()

            # Visualize the distribution of 'Total' using Histogram
            plt.figure(figsize=(10, 6))
            plt.hist(self.data['Total'], bins=20, color='skyblue', edgecolor='black')
            plt.title('Histogram of Total Sales')
            plt.xlabel('Total Sales')
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.show()
            return mean, median, second_max
        except Exception as e:
            print(f"An error occurred while calculating mean, median, and second max: {str(e)}")

    def filter_by_sellings_or_and(self):

        try:
            filtered_data = self.data[
                ((self.data['Quantity'] > 5) | (self.data['Quantity'] == 0)) |
                ((self.data['Price'] > 300) & (self.data['Quantity'] < 2))
                ]
            # Visualize the filtered data using Scatter Plot
            plt.figure(figsize=(10, 6))
            plt.scatter(filtered_data['Price'], filtered_data['Quantity'], color='skyblue', alpha=0.7)
            plt.xlabel('Price')
            plt.ylabel('Quantity')
            plt.title('Filtered Sales Data')
            plt.grid(True)
            plt.show()

            return filtered_data
        except Exception as e:
            print(f"An error occurred while filtering data: {str(e)}")

    def divide_by_2(self):

        file_op = FileOperation()
        try:
            is_black_friday = self.data['Date'] == 'BLACK FRIDAY'

            self.data['BlackFridayPrice'] = self.data['Price'] / 2

            # Update only the rows where 'Date' is "BLACK FRIDAY"
            self.data.loc[is_black_friday, 'BlackFridayPrice'] = self.data.loc[is_black_friday, 'Price'] / 2
            # Visualize the distribution of 'BlackFridayPrice' using Seaborn Count Plot
            plt.figure(figsize=(10, 6))
            sns.countplot(data=self.data, x='BlackFridayPrice')
            plt.title('Count Plot of Black Friday Prices')
            plt.xlabel('Black Friday Price')
            plt.ylabel('Count')
            plt.grid(True)
            plt.show()
            file_op.write_to_csv(self.data, "YafeNof.csv")

            # Create Catplot to visualize distribution of 'BlackFridayPrice'
            sns.catplot(data=self.data, x='BlackFridayPrice', kind='box', y='Price', height=6, aspect=1.5)
            plt.title('Catplot of Black Friday Prices')
            plt.xlabel('Black Friday Price')
            plt.ylabel('Price')
            plt.grid(True)
            plt.show()


            # Create Box Plot to visualize distribution of 'BlackFridayPrice'
            plt.figure(figsize=(10, 6))
            plt.boxplot(self.data['BlackFridayPrice'])
            plt.title('Box Plot of Black Friday Prices')
            plt.ylabel('Price')
            plt.grid(True)
            plt.show()

            # Create Violin Plot to visualize distribution of 'BlackFridayPrice'
            plt.figure(figsize=(10, 6))
            plt.violinplot(self.data['BlackFridayPrice'], vert=False)
            plt.title('Violin Plot of Black Friday Prices')
            plt.xlabel('Price')
            plt.grid(True)
            plt.show()

            print("Values divided by 2 for BLACK FRIDAY and stored in 'BlackFridayPrice' column.")
        except Exception as e:
            print(f"An error occurred while dividing values: {str(e)}")

    def calculate_stats(self, columns: str = None):
        try:
            if columns is None:
                columns = self.data.columns  # If no specific columns are provided, consider all columns

            if isinstance(columns, str):
                columns = [columns]

            stats_dict = {}
            for col in columns:
                if pd.api.types.is_numeric_dtype(self.data[col]):  # Check if column contains numeric data
                    stats_dict[col] = {
                        'Max': self.data[col].max(),
                        'Sum': self.data[col].sum(),
                        'Abs': self.data[col].abs().sum(),  # Absolute sum
                        'Cumulative_Max': self.data[col].cummax().max()  # Cumulative maximum
                    }
                    # Visualize the data distribution using Seaborn
                    sns.histplot(self.data[col], bins='auto')
                    plt.title(f'Distribution of {col}')
                    plt.show()

                    # Apply cut to the column data
                    self.data[col] = pd.cut(self.data[col], bins=5)

                else:
                    print(f"Skipping column '{col}' as it contains non-numeric values.")

            return stats_dict
        except Exception as e:
            print(f"An error occurred while calculating statistics: {str(e)}")

    # 4.19
    def categorize_prices(self):
        file_op = FileOperation()
        try:
            # הגדרת קטגוריות מחיר
            price_categories = {
                "low": (0, 100),
                "medium": (100, 500),
                "high": (500, np.inf)
            }

            # יצירת עמודה חדשה
            self.data['category_price'] = np.where(
                self.data['Price'].between(*price_categories['low']),
                'low',
                np.where(self.data['Price'].between(*price_categories['medium']),
                         'medium', 'high')
            )
            file_op.write_to_csv(self.data, "YafeNof.csv")
            # Create a pie chart to visualize the distribution of prices categories
            category_counts = self.data['category_price'].value_counts()
            plt.figure(figsize=(8, 8))
            plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title('Distribution of Price Categories')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()



            # Create a pie chart to visualize the distribution of price categories
            category_counts = self.data['category_price'].value_counts()
            plt.figure(figsize=(8, 8))
            plt.subplot(2, 2, 1)
            plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title('Distribution of Price Categories')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Create a regression plot to visualize the relationship between Price and Quantity
            plt.subplot(2, 2, 2)
            sns.regplot(x='Price', y='Quantity', data=self.data, scatter_kws={"color": "skyblue"},
                        line_kws={"color": "red"})
            plt.title('Regression Plot: Price vs Quantity')

            # Create a polar plot to visualize the distribution of Price
            plt.subplot(2, 2, 3, polar=True)
            plt.polar(self.data['Price'], color='skyblue')
            plt.title('Polar Plot: Price Distribution')

            # Create a violin plot to visualize the distribution of Price
            plt.subplot(2, 2, 4)
            sns.violinplot(data=self.data['Price'], color='skyblue')
            plt.title('Violin Plot: Price Distribution')

            plt.tight_layout()
            plt.show()


        except Exception as e:
            print(f"אירעה שגיאה במהלך קטלוג מחירים: {str(e)}")
            return None

    def filter_by_mask(self, mask_list, is_by_index=False):

        try:
            if is_by_index:
                filtered_df = self.data[mask_list]
            else:
                filtered_df = self.data.loc[mask_list]

            print(f"Number of rows after filtering: {len(filtered_df)}")
            return filtered_df

        except Exception as e:
            print(f"An error occurred while filtering data: {str(e)}")

    def complex_data_transformation(self):


        try:
            # Transpose the DataFrame
            transposed_df = self.data.stack().unstack(fill_value=-1)  # Fill missing values with -1

            # Add index for rows
            transposed_df.index.name = 'index'  # Replace index name

            # Add additional transformations here (e.g., aggregations, calculations)

            return transposed_df

        except Exception as e:
            print(f"An error occurred during data transformation: {str(e)}")




