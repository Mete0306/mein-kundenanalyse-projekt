import streamlit as st
import pandas as pd
import sqlite3
from ml_Model import KundenanalyseML
import os

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Verzeichnis des Skripts
dbName = os.path.join(BASE_DIR, "..", "database", "kundenanalyse.db")  # Relativer Pfad zur DB



def getKundenDaten():
    c= sqlite3.connect(dbName)

    cursor = c.cursor()


    daten= pd.read_sql("SELECT * FROM kunden ",c)

    c.close()
    return daten



st.title("📊 Kundenanalyse Dashboard")
daten=getKundenDaten()
st.dataframe(daten)

st.subheader("📈 Statistische Analyse")
st.write(f"Durchschnittiches Einkommen: {daten['Einkommen'].mean():,.2f} €")
st.write(f"Kaufwarscheinlichkeit : {daten['Kaufwahrscheinlichkeit'].mean():.2f}")

eingabeEinkommen=st.number_input("Einkommen" , min_value=0,value=50000)
eingabeAlter = st.number_input("Alter", min_value=18, max_value=100, value=30)

if st.button("Vorhersage treffen"):
    model= KundenanalyseML()
    model.trainiereModel()

    vorhersage=model.vorhersage(eingabeEinkommen,eingabeAlter)

    st.success(f"-> Geschätzte Kaufwahrscheinlichkeit: {vorhersage}")



