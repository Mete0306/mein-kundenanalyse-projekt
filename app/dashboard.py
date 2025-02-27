import streamlit as st
import pandas as pd
import sqlite3

dbName= "database/kundenanalyse.db"


def getKundenDaten():
    c= sqlite3.connect(dbName)

    cursor = c.cursor()

    # Prüfe, ob die Tabelle existiert
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='kunden';")
    if not cursor.fetchone():
        print("Tabelle 'kunden' existiert nicht!")
        c.close()
        return None  # Verhindert Fehler, falls die Tabelle nicht existiert

    daten= pd.read_sql("SELECT * FROM kunden ",c)

    c.close()
    return daten

st.title("📊 Kundenanalyse Dashboard")
daten=getKundenDaten()
st.dataframe(daten)

st.subheader("📈 Statistische Analyse")
st.write(f"Durchschnittiches Einkommen: {daten['Einkommen'].mean():,.2f} €")
st.write(f"Kaufwarscheinlichkeit : {daten['Kaufwarscheinlichkeit'].mean():.2f}")




