# Data Preprocessing

# Importing the libraties
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values
                
# Taking care of missing data
# There are some missing values on the dataset. We could eliminate the rows, but those rows could have valuable information.
# Instead of that, we need to replace it with some other values. For example, the mean value of the column or the most frequent value.
# In this case, the we replace them with the mean.
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])