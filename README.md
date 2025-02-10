# **Dron Swarm - Sinhronizirani Let Tello Dronova**
[Watch video on youtube](https://youtu.be/XPST8MOr8c0)
## **📌 Opis Projekta**
Ovaj projekt omogućuje **sinkronizirani let više Tello dronova**, koristeći **Python i biblioteku djitellopy**. Implementira **žongliranje dronovima**, pri čemu se svaki dron kreće prema unaprijed definiranim obrascima koristeći **multithreading** za paralelnu kontrolu.

---

## **📦 Preduvjeti**
### **🔧 Hardverski zahtjevi:**
- **Tello Edu dronovi** (minimalno 3)
- **WiFi hotspot ili Tello aplikacija** za povezivanje dronova
- **Računalo sa stabilnom mrežnom vezom**

### **💾 Softverski zahtjevi:**
- **Python 3.7+** (preporučena verzija)
- Instalirana biblioteka **djitellopy**
- **Threading** za multithreading izvršavanje komandi

---

## **🔧 Instalacija**

Prije pokretanja koda, potrebno je instalirati djitellopy biblioteku:

```bash
pip install djitellopy
```

Provjeri je li Python instaliran pomoću:

```bash
python --version
```

Ako nije, instaliraj ga sa [Python službene stranice](https://www.python.org/downloads/).

---

## **🚀 Pokretanje Projekta**

1️⃣ **Poveži Tello dronove na istu WiFi mrežu** (Tello Edu aplikacija ili mobilni hotspot).  
2️⃣ **Prilagodi IP adrese dronova** u kodu kako bi odgovarale tvojoj mreži:

```python
All = TelloSwarm.fromIps([
    '192.168.137.61',  # IP prvog drona
    '192.168.137.182', # IP drugog drona
    '192.168.137.177'  # IP trećeg drona
])
```

3️⃣ **Pokreni Python skriptu**:
```bash
python swarm.py
```

---

## **⚠️ Sigurnosne Napomene**

🛑 **Provjeri baterije dronova prije polijetanja** – niska baterija može dovesti do naglog pada drona.  
🛑 **Leti u zatvorenom prostoru** ili na otvorenom bez jakog vjetra.  
🛑 **Postavi sigurnu zonu** – osiguraj dovoljno prostora kako bi dronovi izbjegli sudare.  
🛑 **U slučaju greške, koristi ručnu komandu** za hitno slijetanje:
```python
All.land()
```

---

## **📜 Funkcionalnosti Koda**

✅ **Povezivanje s više Tello dronova putem IP adresa**  
✅ **Automatsko uzlijetanje i koordinirani let**  
✅ **Multithreading za istovremene pokrete više dronova**  
✅ **Sigurno slijetanje i prekid veze**  

---


