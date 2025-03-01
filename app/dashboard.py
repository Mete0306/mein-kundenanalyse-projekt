import streamlit as st
import pandas as pd
import sqlite3
import pickle
dbName = "C:/Users/Metehan Yigiter/PycharmProjects/mein_erstesProjekt/mein_kundenanalyse_projekt/database/kundenanalyse.db"


def getKundenDaten():
    c= sqlite3.connect(dbName)

    cursor = c.cursor()


    daten= pd.read_sql("SELECT * FROM kunden ",c)

    c.close()
    return daten

def vorhersage(alter,einkommen):
    with open("models/ml_model.pkl", "rb") as f:

st.title("📊 Kundenanalyse Dashboard")
daten=getKundenDaten()
st.dataframe(daten)

st.subheader("📈 Statistische Analyse")
st.write(f"Durchschnittiches Einkommen: {daten['Einkommen'].mean():,.2f} €")
st.write(f"Kaufwarscheinlichkeit : {daten['Kaufwarscheinlichkeit'].mean():.2f}")




