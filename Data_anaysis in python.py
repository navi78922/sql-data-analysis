Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df = pd.read_csv("customer_data.csv")

>>> df = pd.read_csv("C:\\Users\\HP\\Desktop\\customer_data.csv")
>>> df
     Unnamed: 0        Date  Gender  ...  Quantity Price per Unit  Total Amount
0             0  24-11-2023    Male  ...         3             50           150
1             1  27-02-2023  Female  ...         2            500          1000
2             2  13-01-2023    Male  ...         1             30            30
3             3  21-05-2023    Male  ...         1            500           500
4             4  06-05-2023    Male  ...         2             50           100
..          ...         ...     ...  ...       ...            ...           ...
995         995  16-05-2023    Male  ...         1             50            50
996         996  17-11-2023    Male  ...         3             30            90
997         997  29-10-2023  Female  ...         4             25           100
998         998  05-12-2023  Female  ...         3             50           150
999         999  12-04-2023    Male  ...         4             30           120

[1000 rows x 8 columns]
>>> df.head()
   Unnamed: 0        Date  Gender  ...  Quantity Price per Unit  Total Amount
0           0  24-11-2023    Male  ...         3             50           150
1           1  27-02-2023  Female  ...         2            500          1000
2           2  13-01-2023    Male  ...         1             30            30
3           3  21-05-2023    Male  ...         1            500           500
4           4  06-05-2023    Male  ...         2             50           100

[5 rows x 8 columns]
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 8 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   Unnamed: 0        1000 non-null   int64 
 1   Date              1000 non-null   object
 2   Gender            1000 non-null   object
 3   Age               1000 non-null   int64 
 4   Product Category  1000 non-null   object
 5   Quantity          1000 non-null   int64 
 6   Price per Unit    1000 non-null   int64 
 7   Total Amount      1000 non-null   int64 
dtypes: int64(5), object(3)
memory usage: 62.6+ KB
d.describe()

df.describe()
        Unnamed: 0         Age     Quantity  Price per Unit  Total Amount
count  1000.000000  1000.00000  1000.000000     1000.000000   1000.000000
mean    499.500000    41.39200     2.514000      179.890000    456.000000
std     288.819436    13.68143     1.132734      189.681356    559.997632
min       0.000000    18.00000     1.000000       25.000000     25.000000
25%     249.750000    29.00000     1.000000       30.000000     60.000000
50%     499.500000    42.00000     3.000000       50.000000    135.000000
75%     749.250000    53.00000     4.000000      300.000000    900.000000
max     999.000000    64.00000     4.000000      500.000000   2000.000000
df['Product category'].value_counts()

df[' Product Category'].value_counts()

 Product Categorydf[' Product Category'].count()
 
SyntaxError: unexpected indent
Product Categorydf[' Product Category'].count()

df[' Product Category'].count()

df.groupby('Gender')['Total Amount'].sum()
Gender
Female    232840
Male      223160
Name: Total Amount, dtype: int64
total_sales = df['Quantity'] *['Price per Unit ']

import numpy as np
total_sales = df['Quantity'] *['Price per Unit ']

total_sales = df['Quantity'] * df['Price per Unit ']

total_sales = df['Quantity'] * df['Price Per Unit ']

total_amount = df['Quantity'] * df['Price Per Unit ']

df['total_amount'] = df['Quantity'] * df['Price Per Unit ']

df.groupby('Product Category')['Age'].mean()
Product Category
Beauty         40.371336
Clothing       41.948718
Electronics    41.736842
Name: Age, dtype: float64
df.groupby('Product Category')['Age'].max()
Product Category
Beauty         64
Clothing       64
Electronics    64
Name: Age, dtype: int64
"Total Revenue:", df['Total Amount'].sum()
('Total Revenue:', np.int64(456000))
"Total Revenue:", df['Total Amount'].sum()
('Total Revenue:', np.int64(456000))
df['Total Amount'].sum()
np.int64(456000)
df['Product Category'].value_counts()
Product Category
Clothing       351
Electronics    342
Beauty         307
Name: count, dtype: int64
