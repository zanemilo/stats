# First goal is to show the mathods of a data analysis library, 
# working through exampoles of that, also thinking a jupyter 
# notebook or atleast a video walk through with each module will
# be useful here.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load a sample dataset
data = sns.load_dataset('iris')
print(data.head())

# Mean

mean_sepal_length = data['sepal_length'].mean()
print(f"Mean Sepal Length: {mean_sepal_length}")

# Median
median_sepal_length = data['sepal_length'].median()
print(f"Median Sepal Length: {median_sepal_length}")

# Standard Deviation
std_sepal_length = data['sepal_length'].std()
print(f"Standard Deviation of Sepal Length: {std_sepal_length}")

# # Correlation
# correlation = data.corr()
# print("Correlation Matrix:")
# print(correlation)

# Visualization
sns.pairplot(data, hue='species')
plt.show()

