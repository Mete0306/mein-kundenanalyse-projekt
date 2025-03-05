import pickle
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler
import os

class KundenanalyseML:


    def __init__(self):

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        MODEL_DIR = os.path.join(BASE_DIR, "..", "models")
        self.dbName = os.path.join(BASE_DIR, "..", "database", "kundenanalyse.db")
        self.modellPfad = os.path.join(MODEL_DIR, "ml_model.pkl")
        self.scalerPfad = os.path.join(MODEL_DIR, "ml_scaler.pkl")
        self.modell=None
        self.scaler=None


    def ladeDaten(self):
        try:
            c= sqlite3.connect(self.dbName)
            daten= pd.read_sql("SELECT * FROM kunden",c)

            c.close()


            return daten

        except sqlite3.OperationalError as e:
            print("Datenbank konnte nicht geladen werden ")
            return pd.DataFrame()

    def trainiereModel(self):

        daten = self.ladeDaten()

        x= daten[['Alter','Einkommen']]
        y= daten['Kaufwahrscheinlichkeit']
        self.scaler= StandardScaler()
        xSkaliert= self.scaler.fit_transform(x)

        xTrain,xTest,yTrain, yTest = train_test_split(xSkaliert,y,test_size=0.2, random_state=42)


        self.modell= LinearRegression()

        self.modell.fit(xTrain,yTrain)
        print(f"Modell trainiert mit {len(xTrain)} Trainingsdaten")

        self.speichereModell()
        self.speichereScaler()

    def speichereModell(self):
        if  self.modell is not None:
            with open(self.modellPfad,"wb") as s:
                pickle.dump(self.modell,s)
            print("Modell wurde gespeichert")
        else:
            print("Speichern Fehlgeschlagen!! Kein Modell gefunden. ")

    def speichereScaler(self):
        if self.scaler is not None:
            with open(self.scalerPfad,"wb") as s:
                pickle.dump(self.scaler,s)
            print("Scaler wurde gespeichert")
        else:
            print("Speichern fehlgeschlagen! Kein Scaler gefunden." )



    def ladeModell(self):
        try:
            with open(self.modellPfad, "rb") as s:
                self.modell = pickle.load(s)
            print("Modell erfolgreich geladen")

        except FileNotFoundError:
            print("Datei nicht gefunden")

    def ladeScaler(self):
         try:
             with open(self.scalerPfad,"rb") as s:
                 self.scaler= pickle.load(s)
             print("Scaler erfolgreich geladen")
         except FileNotFoundError :
             print("Datei nicht gefunden")

    def vorhersage(self,einkommen,alter):
        if self.modell is None:
            self.ladeModell()
        if self.scaler is None:
            self.ladeScaler()

        eingabe = pd.DataFrame([[alter, einkommen]], columns=['Alter', 'Einkommen'])
        eingabeSkaliert = self.scaler.transform(eingabe)
        yVorhersage = self.modell.predict(eingabeSkaliert)

        return round(yVorhersage[0],2)







