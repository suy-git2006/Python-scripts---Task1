import pandas as pd
import numpy as np

data = {
        'ID': [201, 202, 203, 204, 205],
        'colour': ['red', 'green', 'blue', 'red', 'green'],
        'alphabet': ['A', 'B', 'A', 'C', 'B']
    }
df = pd.DataFrame(data)
df_copy = df.copy()


print("--- Original Data ---")
print(df)

ohe_df = pd.get_dummies(df_copy, columns=['colour'])
print("\nOne-Hot Encoded DataFrame after encoding 'colour':\n")
print(ohe_df)

ohe_1_df = pd.get_dummies(df_copy, columns=['alphabet'])
print("\nOne-Hot Encoded DataFrame after encoding 'alphabet':\n")
print(ohe_1_df)
