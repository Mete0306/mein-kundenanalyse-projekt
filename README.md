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
🔗 [Kundenanalyse-Dashboard]([https://kundenanalyse.streamlit.app](https://mein-kundenanalyse-projekt-fedf8dym6prdqfqpaqj2m6.streamlit.app/)

## 🛠️ Installation

### 1.Repository klonen

git clone https://github.com/Mete0306/mein_kundenanalyse_projekt.git
cd mein_kundenanalyse_projekt

### 2.Virtuelle Umgebung erstellen und aktivieren

python -m venv .venv
source .venv/bin/activate  # macOS & Linux
.venv\Scripts\activate    # Windows

### 3.Benötigte Abhängigkeiten installieren
pip install -r requirements.txt
```

## 🐂 Projektstruktur 

mein_kundenanalyse_projekt/
│── app/
│   ├── dashboard.py          # Streamlit-Dashboard
│   ├── ml_Model.py           # Machine-Learning-Modelle
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
## 🏃‍♂️ Anwendung starten

### Datenbank aus CSV erstellen:
python database/csvToDatabase.py

### Dashboard starten:
streamlit run app/dashboard.py


Dashboard starten:
## 🛠 Technologien  
📌 **Python**, **SQLite**, **Streamlit**, **Scikit-Learn**, **Pandas**

## 🏆 Autor  
👤 **Metehan Yigiter**  
📧 metehanyigiter5@gmail.com  
📌 Mete0306  

---
🎉 Viel Spaß mit dem Kundenanalyse-Dashboard!  

---
