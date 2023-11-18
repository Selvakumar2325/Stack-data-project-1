

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("C:/Dataset/Stock_Data.csv")
x=dataset.iloc[:,1:4].values
y=dataset.iloc[:,-1].values



#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)


#Feature scating
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)


from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)


window = tk.Tk()
window.title("Stock Data ")
window.geometry("900x600")
window.resizable(False,False)
window.config(bg="#C0C0C0")

# Define the input fields

label1 = tk.Label(window, text="Open:",font=("Times New Roman",14,"bold"),bg="#C0C0C0")
label1.place(x=100,y=200)
entry1 = tk.Entry(window,width=30)
entry1.place(x=100,y=250)

title_label = tk.Label(window, text="PREDICT  PURCHASED",font=("Times New Roman",20,"bold"),bg="#C0C0C0")
title_label.place(x=300,y=100)


label2 = tk.Label(window, text="High:",font=("Times New Roman",14,"bold"),bg="#C0C0C0")
label2.place(x=100,y=300)
entry2 = tk.Entry(window,width=30)
entry2.place(x=100,y=350)

#define the input

label3 = tk.Label(window, text="Low:",font=("Times New Roman",14,"bold"),bg="#C0C0C0")
label3.place(x=100,y=400)
entry3 = tk.Entry(window)
entry3.place(x=100,y=450)



# Define the prediction function
def predict():
    try:
        Open = float(entry1.get())
        High = float(entry2.get())
        Low=float(entry3.get())
        

        test_data = sc.transform([[Open,High,Low]])
        prediction = regressor.predict(test_data)
        result_label.config(font=("Times New Roman",16,"bold"),bg="#C0C0C0",text="Predicted Species: " + str( prediction))
        result_label.place(x=400,y=200)
    except ValueError:
        result_label.config(font=("Times New Roman",16,"bold"),bg="#C0C0C0",text="Invaled: " )
        result_label.place(x=500,y=200)

# Define the prediction button
button = tk.Button(window, text="PREDICT",font=("Times New Roman",20,"bold"),bg="#C0C0C0", command=predict)
button.place(x=400,y=400)

# Define the result label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()