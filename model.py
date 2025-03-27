#importing the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading the data set named heart.csv
df=pd.read_csv('heart.csv')

#first five rows of a dataset
df.head()

df.tail()

"""**Data** **preprocessing**"""

df.describe()

df.shape

df.info()

df.isnull().sum()

df.columns

df['target'].value_counts()

plt.figure(figsize=(10,5))
sns.countplot(x='target',data=df)

"""HERE ----------------->


DEFECTIVE HEART ------------> 0

GOOD HEART -----------------> 1
"""

X=df.drop('target',axis=1)
y=df['target']

"""WE HAVE TAKEN THE VALUES FOR

DEPENDENT VARAIABLE --->y

INDEPENDENT VARAIABLE ---->X
"""

print(X)

print(y)

"""**SPLITING** ***THE*** ***DATA*** ***INTO*** ***TRAIN*** ***AND*** ***TEST***"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,stratify=y,random_state=0)

print(X_train.shape , X_test.shape , y_train.shape , y_test.shape)

""" **MODEL**  **SELECTION**"""

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(X_train,y_train)

model.score(X_train,y_train)

y_pred=model.predict(X_test)

from sklearn.metrics import accuracy_score

acc=accuracy_score(y_test,y_pred)

print("the Acuuracy for the test data is:",acc*100)

import pickle

pickle.dump(model,open('model.pkl','wb'))
