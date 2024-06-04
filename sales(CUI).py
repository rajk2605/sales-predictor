# Task 1 :-- Sales Volume Predictor


import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("sales.csv")  
print(data)
print(data.isnull().sum())

# features and target 
features = data[["TV", "Newspaper", "Radio"]]  
target = data["Sales"]  

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.5, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)
print(data.describe())
print(data.info())
print(data.mean())
print(data.dtypes)

#score
s1 = model.score(X_train, y_train)
print("Training Score =", s1)
s2 = model.score(X_test, y_test)
print("Training Score =", s2)

# Make a prediction
#new_data = pd.DataFrame([[38.2  ,  3.7,       13.8]], columns=['TV', 'Newspaper', 'Radio']) 
TV = float(input("Spent on TV :"))
Radio = float(input("Spent on Radio :"))
Newspaper = float(input("Spent on Newspaper :"))
prediction = model.predict([[TV, Radio, Newspaper]])
print("Predicted sales volume:", prediction)

#save 
f = open("re.model","wb")
pickle.dump(model,f)
f.close()





