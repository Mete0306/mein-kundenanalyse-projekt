# 📊 Kundenanalyse-Dashboard

Dieses Projekt ist ein interaktives Dashboard zur **Kundenanalyse** mit **Maschinellem Lernen**.  
Es analysiert Kundendaten aus einer SQLite-Datenbank und trifft **Vorhersagen** über die Kaufwahrscheinlichkeit basierend auf Einkommen und Alter.

## 🚀 Funktionen
✅ Datenimport aus einer CSV-Datei in eine SQLite-Datenbank  
✅ Streamlit-Dashboard zur Datenanalyse und Visualisierung  
✅ Maschinelles Lernmodell mit **Linearer Regression**  
✅ **Vorhersage der Kaufwahrscheinlichkeit** eines Kunden  


## 🚀 Live-Dashboard
Nutze das Kundenanalyse-Dashboard ohne Installation direkt hier:  
🔗 [https://kundenanalyse.streamlit.app](https://mein-kundenanalyse-projekt-fedf8dym6prdqfqpaqj2m6.streamlit.app/)

## 🛠️ Installation & Nutzung

### 🚀 1. Projekt herunterladen

Methode 1: Mit Git (Empfohlen)

Falls du Git installiert hast, kannst du das Repository mit folgendem Befehl klonen:

**git clone https://github.com/dein-github-account/mein-kundenanalyse-projekt.git**
**cd mein-kundenanalyse-projekt**

Methode 2: Manuell herunterladen

Falls du kein Git hast, kannst du das Repository als ZIP-Datei von GitHub herunterladen und entpacken.Dann öffnest du ein Terminal oder eine Eingabeaufforderung in dem entpackten Projektordner.


### 📞 2. Abhängigkeiten installieren

Installiere alle benötigten Pakete aus der Datei requirements.txt:

**pip install -r requirements.txt**

Falls Fehler auftreten, stelle sicher, dass du pip auf dem neuesten Stand hast:

**pip install --upgrade pip**

### 📂 4. Datenbank erstellen (falls nicht vorhanden)

Falls die SQLite-Datenbank kundenanalyse.db noch nicht existiert, erstelle sie mit:

**python database/csvToDatabase.py**

✅ Danach sollten die Kundendaten aus data/kunden.csv in die Datenbank importiert sein.

#### 🏃‍♂️ 5. Dashboard starten

Das Dashboard basiert auf Streamlit und kann mit folgendem Befehl gestartet werden:

**streamlit run app/dashboard.py**

Nach ein paar Sekunden öffnet sich die Kundenanalyse-Webapp im Browser unter:

http://localhost:8501

Falls es nicht automatisch öffnet, klicke auf den Link in der Konsole.

## 🐂 Projektstruktur 

mein_kundenanalyse_projekt/
│── app/
│   ├── dashboard.py          # Streamlit-Dashboard
│   ├── ml_Model.py           # Machine-Learning-Modell
│
│── data/
│   ├── kunden.csv            # Kundendaten
│
│── database/
│   ├── csvToDatabase.py      # CSV-Datenbank Import
│   ├── kundenanalyse.db      # SQLite Datenbank
│
│── models/
│   ├── ml_model.pkl          # Gespeichertes Modell
│   ├── ml_scaler.pkl         # Gespeicherter Scaler
│
│── README.md
│── requirements.txt          # Abhängigkeiten
│── .gitignore                # Ignorierte Dateien
```


## 🛠 Technologien  
📌 **Python**, **SQLite**, **Streamlit**, **Scikit-Learn**, **Pandas**

## 🏆 Autor  
👤 **Metehan Yigiter**  
📧 metehanyigiter5@gmail.com  
📌 Mete0306  

---
🎉 Viel Spaß mit dem Kundenanalyse-Dashboard!  

---
