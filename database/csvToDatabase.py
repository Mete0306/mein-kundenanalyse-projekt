import sqlite3
import pandas as pd
import os

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Verzeichnis des Skripts
dbName = os.path.join(BASE_DIR, "..", "database", "kundenanalyse.db")  # Relativer Pfad zur DB



def erstelleDatenbank ():

    c=sqlite3.connect(dbName)
    cursor= c.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS kunden "
                   "(KundeID INTEGER PRIMARY KEY , "
                   "Name TEXT ,"
                   "[Alter] INTEGER, "
                   "Einkommen INTEGER, "
                   "Kaufwahrscheinlichkeit REAL) ")

    c.commit()
    c.close()

def insertDatenVonCSV (csvPfad):
    if not os.path.exists(csvPfad):
        print(f"Fehler: Die Datei {csvPfad} existiert nicht!")
        return
    c= sqlite3.connect(dbName)
    datei=  pd.read_csv(csvPfad)
    datei.to_sql("kunden",c,if_exists="replace", index=False)
    c.close()

if __name__ == "__main__":
    erstelleDatenbank()
    insertDatenVonCSV(csvPfad = os.path.join(BASE_DIR, "..", "data", "kunden.csv"))
    print("Datenbank erstellt und CSV-Daten importiert!")



