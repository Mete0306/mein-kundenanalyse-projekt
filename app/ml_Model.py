import pickle
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
class KundenanalyseML:


    def __init__(self):
        self.dbName="C:/Users/Metehan Yigiter/PycharmProjects/mein_erstesProjekt/mein_kundenanalyse_projekt/database/kundenanalyse.db"
        self.modellPfad="C:/Users/Metehan Yigiter/PycharmProjects/mein_erstesProjekt/mein_kundenanalyse_projekt/models/ml_model.pkl"
        self.modell=None

    def ladeDaten(self):

        c= sqlite3.connect(self.dbName)
        daten= pd.read_sql("SELECT * FROM kunden",c)

        c.close()
        return daten

    def trainiereModel(self):

        daten = self.ladeDaten()

        x= daten[['Alter','Einkommen']]
        y= daten['Kaufwahrscheinlichkeit']

        xTrain,xTest,yTrain, yTest = train_test_split(x,y,test_size=0.2, random_state=42)


        self.modell= LinearRegression()

        self.modell.fit(xTrain,yTrain)
        print(f"Modell trainiert mit {len(xTrain)} Trainingsdaten")

        self.speichereModel()

    def speichereModel(self):
        if  self.modell is not None:
            with open(self.modellPfad,"wb") as s:
                pickle.dump(self.modell,s)
            print("Modell wurde gespeichert")


    def ladeModell(self):
        try:
            with open(self.modellPfad, "rb") as s:
                self.modell = pickle.load(s)
            print("Modell erfolgreich geladen")

        except FileNotFoundError:
            print("Datei nicht gefunden")

    def vorhersage(self,einkommen,alter):
        if self.modell is None:
            self.ladeModell()

        eingabe= [[einkommen,alter]]
        yVorhersage= self.modell.predict(eingabe)

        return yVorhersage[0]


