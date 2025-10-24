import pandas as pd
import numpy as np

data = {
        'ID': [101, 102, 103, 104, 105, 106],
        'size': ['small', 'medium', 'large', 'medium', 'small', 'large'],
        'temperature': ['cold', 'warm', 'hot', 'warm', 'cold', 'hot']
    }
df = pd.DataFrame(data)
df_copy = df.copy()

print("\nOriginal DataFrame:\n")
print(df)

size_mapping = {'small': 1, 'medium': 2, 'large': 3}
df_copy['size_encoded'] = df_copy['size'].map(size_mapping)
print("\nDataFrame after encoding 'size':\n")
print(df_copy)

temp_mapping = {'cold': 1, 'warm': 2, 'hot': 3}
df_copy['temp_encoded'] = df_copy['temperature'].map(temp_mapping)
print("\nDataFrame after encoding 'temperature':\n")
print(df_copy)
