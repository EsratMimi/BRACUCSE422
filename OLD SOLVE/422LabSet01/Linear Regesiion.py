import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np 

from sklearn.model_selection import train_test_split

data=pd.read_csv('StockPriceData.csv',delimiter=',')
df= data[["Adj Close"]]
print(df)
d=data.dropna()
#print(d)
X=d.index.values.reshape(-1,1)
print("Printing X")
print(X)
Y=d['Adj Close'].values.reshape(-1,1)
print("Printing Y")
print(Y)

plt.scatter(X,Y)
#plt.show()
regressor=LinearRegression()
regressor.fit(X,Y)

xtrain,xtest,ytrain,ytest = train_test_split(X,Y, test_size = 0.5, random_state=42)

regressor.fit(xtrain,ytrain)
ypred=regressor.predict(xtest)

plt.plot(xtest,ypred,color='red',linewidth=2)
plt.show()

print (xtrain.shape, ytrain.shape)
print (xtest.shape, ytest.shape)
pred_train=regressor.predict(xtrain)
plt.scatter(xtrain,ytrain,s=3)
plt.plot(xtrain,pred_train,color='green',linewidth=2)
plt.show()

pred_test=regressor.predict(xtest)
plt.scatter(xtest,ytest,s=5)
plt.plot(xtest,pred_test,color='black',linewidth=2)
plt.show()