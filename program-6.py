import pandas as pd
# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'D:/Downloads/bca a.csv'
# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)
# Print the first 5 lines (+header) of the CSV file
print("First 5 Lines:")
print(df.head(5))
# Print the last 5 lines (+header) of the CSV file
print("\nLast 5 Lines:")
print(df.tail(5))







********(changes are here ::    'D:/Downloads/bca a.csv')******




output:   First 5 Lines:
   bca a  Unnamed: 1  Unnamed: 2  ...  Unnamed: 24  Unnamed: 25  Unnamed: 26
0      1         1.0         2.0  ...         24.0         25.0         26.0
1      2         NaN         NaN  ...          NaN          NaN          NaN
2      3         NaN         NaN  ...          NaN          NaN          NaN
3      4         NaN         NaN  ...          NaN          NaN          NaN
4      5         NaN         NaN  ...          NaN          NaN          NaN

[5 rows x 27 columns]

Last 5 Lines:
    bca a  Unnamed: 1  Unnamed: 2  ...  Unnamed: 24  Unnamed: 25  Unnamed: 26
15     16         NaN         NaN  ...          NaN          NaN          NaN
16     17         NaN         NaN  ...          NaN          NaN          NaN
17     18         NaN         NaN  ...          NaN          NaN          NaN
18     19         NaN         NaN  ...          NaN          NaN          NaN
19     20         NaN         NaN  ...          NaN          NaN          NaN

[5 rows x 27 columns]
