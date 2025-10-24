import pandas as pd
import numpy as np

data = {
        'Age': [20, 36, np.nan, 36, 72, 19, 45],
        'Salary': [95000, 54000, 82000, np.nan, 94000, np.nan, 110000],
        'Department': ['IT', 'HR', 'Sales', 'IT', np.nan, 'IT', 'Sales']
    }

df = pd.DataFrame(data)
df_copy = df.copy()
print("Original DataFrame with missing Values:\n")
print(df)
print("\nMissing value counts:")
print(df.isnull().sum())

mean_age = df_copy['Age'].mean()
df_copy['Age_filled_mean'] = df_copy['Age'].fillna(mean_age)
print("\nAfter Imputation of column'Age' :\n")
print(df_copy)

mode_dept = df_copy['Department'].mode()[0]
df_copy['Dept_filled_mode'] = df_copy['Department'].fillna(mode_dept)
print("\nAfter Imputation of column 'Department' :\n")
print(df_copy)

median_salary = df_copy['Salary'].median()
df_copy['salary_filled_median'] = df_copy['Salary'].fillna(median_salary)
print("\nAfter Imputation of column 'Salary' :\n")
print(df_copy)
