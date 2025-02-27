import sqlite3
import pandas as pd
import os

dbName = "C:/Users/Metehan Yigiter/PycharmProjects/mein_erstesProjekt/mein_kundenanalyse_projekt/database/kundenanalyse.db"



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
    insertDatenVonCSV("C:/Users/Metehan Yigiter/PycharmProjects/mein_erstesProjekt/mein_kundenanalyse_projekt/data/kunden.csv")
    print("Datenbank erstellt und CSV-Daten importiert!")



