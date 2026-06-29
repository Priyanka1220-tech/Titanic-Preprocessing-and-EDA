Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
===== RESTART: C:/Users/Dell/AppData/Local/Programs/Python/Python314/GG.py =====
First 5 Rows:
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]

Shape of Dataset:
(5, 12)

Columns:
Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='str')

Data Types:
PassengerId      int64
Survived         int64
Pclass           int64
Name               str
Sex                str
Age              int64
SibSp            int64
Parch            int64
Ticket             str
Fare           float64
Cabin              str
Embarked           str
dtype: object

Missing Values:
PassengerId    0
Survived       0
Pclass         0
Name           0
Sex            0
Age            0
SibSp          0
Parch          0
Ticket         0
Fare           0
Cabin          3
Embarked       0
dtype: int64

Missing Values After Cleaning:
PassengerId    0
Survived       0
Pclass         0
Name           0
Sex            0
Age            0
SibSp          0
Parch          0
Ticket         0
Fare           0
Cabin          0
Embarked       0
dtype: int64

Summary Statistics:
       PassengerId  Survived    Pclass       Age     SibSp  Parch       Fare
count     5.000000  5.000000  5.000000   5.00000  5.000000    5.0   5.000000
mean      3.000000  0.600000  2.200000  31.20000  0.600000    0.0  29.521660
std       1.581139  0.547723  1.095445   6.83374  0.547723    0.0  30.510029
min       1.000000  0.000000  1.000000  22.00000  0.000000    0.0   7.250000
25%       2.000000  0.000000  1.000000  26.00000  0.000000    0.0   7.925000
50%       3.000000  1.000000  3.000000  35.00000  1.000000    0.0   8.050000
75%       4.000000  1.000000  3.000000  35.00000  1.000000    0.0  53.100000
max       5.000000  1.000000  3.000000  38.00000  1.000000    0.0  71.283300

Correlation Matrix:
              PassengerId  Survived        Pclass  ...     SibSp  Parch      Fare
PassengerId  1.000000e+00  0.000000 -6.409876e-17  ... -0.577350    NaN -0.085941
Survived     0.000000e+00  1.000000 -6.666667e-01  ...  0.166667    NaN  0.654408
Pclass      -6.409876e-17 -0.666667  1.000000e+00  ... -0.666667    NaN -0.977498
Age          5.321565e-01  0.360674 -7.079895e-01  ...  0.093508    NaN  0.730448
SibSp       -5.773503e-01  0.166667 -6.666667e-01  ...  1.000000    NaN  0.644310
Parch                 NaN       NaN           NaN  ...       NaN    NaN       NaN
Fare        -8.594059e-02  0.654408 -9.774977e-01  ...  0.644310    NaN  1.000000

[7 rows x 7 columns]
