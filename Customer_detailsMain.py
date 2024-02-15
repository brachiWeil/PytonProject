from Customer_details import Customer_details
from FileOperation import FileOperation


def main():
    file_op = FileOperation()
    sales_data = file_op.read_csv("YafeNof.csv")
    sales_data_cust = Customer_details(sales_data)
    sales_data_cust.generate_random_sales("Sidur")
    Customer_details.print_python_version()
    result = sales_data_cust.process_parameters(10, "NAME=kali", "NAME=John", 5.5, "AGE=30")
    print(result)

    sales_data_cust.print_head_tail_rand()
    sales_data_cust.process_numeric_columns()


if __name__ == "__main__":
    main()