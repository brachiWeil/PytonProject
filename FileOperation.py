import pandas as pd

# import Customer_details as cust


class FileOperation:

    def read_csv(self, file_path: str):
        try:
            data = pd.read_csv(file_path)
            return data
       #מדפיס שגיאה מתאימה על ידי הפונקציה handle_error
        except Exception as e:
            print("error")

    def write_to_csv(self, data, file_name: str):
        try:
            data.to_csv(file_name, index=False)
            print(f"נתונים נשמרו בהצלחה בקובץ: {file_name}")
        except Exception as e:
            print(f"אירעה שגיאה בשמירת הנתונים לקובץ CSV: {str(e)}")
