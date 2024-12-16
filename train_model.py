#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Generate Fibonacci dataset
def generate_fib_data(n):
    data = []
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    for i, val in enumerate(fib):
        data.append([i, val])
    return data

# Dataset
data = generate_fib_data(50)  # First 50 Fibonacci numbers
df = pd.DataFrame(data, columns=['index', 'value'])

X = df[['index']]
y = df['value']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'fibonacci_model.pkl')
print("Model saved as fibonacci_model.pkl")


# In[ ]:




