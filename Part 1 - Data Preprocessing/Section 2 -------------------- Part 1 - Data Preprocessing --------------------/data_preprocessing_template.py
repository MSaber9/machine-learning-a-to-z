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

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X = LabelEncoder()
# This will encode the first column as a number. The numbers has the idea of comparing each other so one value could be bigger than other. 
# The problem with this is that these are categories not numbers, and it doesn't make sense to compare them as numbers
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])

# The following lines will encode a column with 1 for each o the categories on a colum category. In this case, the first column.
# This category encoding is called dummy variables.
oneHotEncoder = OneHotEncoder(categorical_features=[0])
X = oneHotEncoder.fit_transform(X).toarray()

labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)
