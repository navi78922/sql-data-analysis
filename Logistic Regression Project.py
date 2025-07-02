Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## Logistc regression
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> from sklearn.linear_model import LogisticRegression
from sklearn .model_selection import train+
>>> from sklearn .model_selection import train+
SyntaxError: invalid syntax
>>> from sklearn.model_selection import train_test_split
>>> from slearn.metrics import classification_report,confusion_matrix
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    from slearn.metrics import classification_report,confusion_matrix
ModuleNotFoundError: No module named 'slearn'
>>> from skearn.metrics import classification_report,confusion_matrix

>>> from sklearn.metrics import classification_report,confusion_matrix
>>> data = {
...     'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
...     'Pass': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
... }
>>> df = pd.DataFrame(data)
>>> df
   Hours_Studied  Pass
0              1     0
1              2     0
2              3     0
3              4     0
4              5     1
5              6     1
6              7     1
7              8     1
8              9     1
9             10     1
sns.scatterplot(x='Hours_studied',y ='Pass',data=df)

import seaborn as sns
sns.scatterplot(x='Hours_studied',y ='Pass',data=df)

sns.scatterplot(x='Hours_studied',y ='Pass',data=df)

sns.scatterplot(x='Hours_Studied',y ='Pass',data=df)
<Axes: xlabel='Hours_Studied', ylabel='Pass'>
plt.title("Hours_Studied vs Pass")
Text(0.5, 1.0, 'Hours_Studied vs Pass')
plt.xlabel("Hours_Studied")
Text(0.5, 0, 'Hours_Studied')
plt.ylabel("Pass (1=Yes, 0=No)")
Text(0, 0.5, 'Pass (1=Yes, 0=No)')
plt.show()
## split
## split the data to train_test
x = df[['Hours_Studied']]
y = df['Pass;]
       
SyntaxError: unterminated string literal (detected at line 1)
y = df['Pass']
       
x_train,  x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 0)
       
x_train
       
   Hours_Studied
4              5
9             10
1              2
6              7
7              8
3              4
0              1
5              6
y_train
       
4    1
9    1
1    0
6    1
7    1
3    0
0    0
5    1
Name: Pass, dtype: int64
## Train the Regression  Model
       
model = LogisticRegression()
       
model.fit(x_train,y_train)
       
LogisticRegression()
## predect the data
       
y_pred = model.predict(x_test)
       
y_pred
       
array([0, 1])
## Evalaute the model
       
confusion_matrix(y_test,y_pred)
       
array([[1, 0],
       [0, 1]])
classification_report(y_test,y_pred)
       
'              precision    recall  f1-score   support\n\n           0       1.00      1.00      1.00         1\n           1       1.00      1.00      1.00         1\n\n    accuracy                           1.00         2\n   macro avg       1.00      1.00      1.00         2\nweighted avg       1.00      1.00      1.00         2\n'
## predict new value
       
new_hours = [[4.5]]
       
prediction = model.predict(new_hours)
       

model.predict(new_hours)


new_data = pd.DataFrame({'Hours_Studied': [4.5]})
prediction = model.predict(new_data)

prediction
array([1])
#