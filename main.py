#"_________________________________"
#ברכי וייל-עשיתי שיעורי בית (נראה לי שאת כולם )
#  ואני לא יודעת אם הגשתי את כולם המורה אמרה שאפשר לאמר לה שעשיתי בלי להגיש אותם
# וזה בסדר  גמור אז עשיתי את השיעורים תודה
#וגם בונוס של שאלות שעני מGEEKSFORGEEKS עניתי בערך על 7-8
# # הוראות והנחיות | בונוס % : 5קריאה שלהן בקול-קראנו בקול את ההנחיות.
#
# # דברים שנתרמתי משיעור פיתון:
# # 1- לפתור בעיות ולכתוב קוד בצורה יעילה ומובנית.
# # 2- ליצור תוכניות   באמצעות שימוש בספריות  שונות.
# # לכתוב קוד שמבצע פעולות בסיסיות, כמו חישובים, קלט ופלט, עבודה עם קבצים ועוד.
# # הכרות עם ספריות פייתון: למדתי על ספריות נפוצות כמו NumPy, Pandas ו-Matplotlib, ואיך להשתמש בהן למשימות שונות.
## סבלנות ואמונה
## דיני עבודה
# # הנאה מהתהליך: גיליתי את הסיפוק והאתגר שבכתיבת קוד ופיתוח תוכנות.
# # לסיכום, שיעור פיתון היה חוויה חיובית ומועילה מאוד. רכשתי ידע תיאורטי ומעשי חשוב, ופיתחתי מיומנויות חשיבה ותכנות שיסייעו לי בהמשך דרכי.
# # אני מודה למורה  על ההדרכה והתמיכה
# # יתרונות לשימוש בשפת פייתון:
# # מתאים למתחילים ולמתקדמים: פייתון מתאימה הן למתחילים בתחום התכנות והן למפתחים מנוסים.
# # קלות למידה: פייתון ידועה בשפה קלה יחסית ללימוד, עם תחביר פשוט וברור
# # יכולות רחבות: פייתון מתאימה לשימוש במגוון רחב של תחומים, כולל פיתוח אתרים , פיתוח משחקים, ניתוח נתונים, ועוד.
# # ספריות רבות: פייתון נהנית ממגוון רחב של ספריות , המאפשרות פתרון יעיל ומהיר של משימות רבות.
# # קוד פתוח וחינמי: פייתון היא שפה פתוחה, והיא זמינה לשימוש בחינם.
from FileOperation import FileOperation

import pandas as pd
from SalesData import SalesData
from Customer_details import Customer_details

# # דוגמאות שימוש
file_op = FileOperation()


# # Example usage:
sales_data = file_op.read_csv("YafeNof.csv")

sales_data_obj = SalesData(sales_data)
sales_data_obj.eliminate_duplicates()
print("DataFrame 'sales_data':")
print(sales_data_obj.data)
#
total_sales = sales_data_obj.calculate_total_sales()
print("Total sales for each product:")
print(total_sales)
#
total_sales_per_month = sales_data_obj.calculate_total_sales_per_month()
print("Total sales per month:")
print(total_sales_per_month)

best_selling_product = sales_data_obj.identify_best_selling_product()
print("Best-selling product:")
print(best_selling_product)
#
identify_month_with_highest_sales = sales_data_obj.identify_month_with_highest_sales()
print("month_with_highest_sales:")
print(identify_month_with_highest_sales)

analysis_results = sales_data_obj.analyze_sales_data()
print("Analysis Results:")
print(analysis_results)
#
# Calculate cumulative sales
cumulative_sales = sales_data_obj.calculate_cumulative_sales()
print("Cumulative Sales:")
print(cumulative_sales)
#
bar_chart_category_sum = sales_data_obj.bar_chart_category_sum()
print("month_with_highest_sales:")
#
mean, median, second_max = sales_data_obj.calculate_mean_quantity()
#
# Print the results
print("Mean:", mean)
print("Median:", median)
print("Second Maximum:", second_max)
#
filter_by_sellings = sales_data_obj.filter_by_sellings_or_and()
print("filter_by_sellings_or_and")
print(filter_by_sellings)
#
divide_by_2 = sales_data_obj.divide_by_2()
print("divide_by_2")
print(sales_data_obj.data)
#
calculate_stats = sales_data_obj.calculate_stats()
print("calculate_stats")
print(calculate_stats)

categorize_prices = sales_data_obj.categorize_prices()
print("categorize_prices")
print(sales_data_obj.data)

mask_list = [True, False, True, False, True]
#
filtered_df = sales_data_obj.filter_by_mask(mask_list)
print(filtered_df)  # תציג את ה-DataFrame המסונן
#
#
transposed_df = sales_data_obj.complex_data_transformation()
print(transposed_df)





