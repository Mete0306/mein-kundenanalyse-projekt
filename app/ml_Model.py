import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


dbName = "C:/Users/Metehan Yigiter/PycharmProjects/mein_erstesProjekt/mein_kundenanalyse_projekt/database/kundenanalyse.db"

def ladeDaten():

    c= sqlite3.connect(dbName)
    daten= pd.read_sql("SELECT * FROM kunden",c)

    c.close()
    return daten


daten = ladeDaten()
print(daten.head())

x= daten[['Alter','Einkommen']]
y= daten['Kaufwahrscheinlichkeit']

xTrain,xTest,yTrain, yTest = train_test_split(x,y,test_size=0.2, random_state=42)

print(f"Trainingsdaten: {len(xTrain)} Stk")
print(f"Testdaten: {len(yTest)} Stk")