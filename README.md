# **Drone Swarm - Synchronized Flight of Tello Drones**
[Watch video on YouTube](https://youtu.be/XPST8MOr8c0)

## **📌 Project Description**
This project enables **synchronized flight of multiple Tello drones** using **Python and the djitellopy library**. It implements **drone juggling**, where each drone moves according to predefined patterns.

---

## **📦 Prerequisites**

### **🔧 Hardware Requirements:**
- **Tello Edu drones** (at least 3)
- **WiFi hotspot or Tello app** for connecting the drones
- **Computer with a stable network connection**

### **💾 Software Requirements:**
- **Python 3.7+** (recommended version)
- Installed **djitellopy library**
- **Threading** for multithreading command execution

---

## **🔧 Installation**

Before running the code, you need to install the djitellopy library:

```bash
pip install djitellopy
```

Check if Python is installed using:

```bash
python --version
```

If not, install it from the [official Python website](https://www.python.org/downloads/).

---

## **🚀 Running the Project**

1️⃣ **Connect Tello drones to the same WiFi network** (Tello Edu app or mobile hotspot).  
2️⃣ **Adjust drone IP addresses** in the code to match your network:

```python
All = TelloSwarm.fromIps([
    '192.168.137.61',  # IP of the first drone
    '192.168.137.182', # IP of the second drone
    '192.168.137.177'  # IP of the third drone
])
```

3️⃣ **Run the Python script**:
```bash
python swarm.py
```

---

## **⚠️ Safety Notes**

🛑 **Check drone batteries before takeoff** – low battery can cause sudden drone drop.  
🛑 **Fly indoors** or outdoors without strong wind.  
🛑 **Establish a safe zone** – ensure enough space to avoid drone collisions.  
🛑 **In case of an error, use the manual command** for emergency landing:
```python
All.land()
```

---

## **📜 Code Features**

✅ **Connecting to multiple Tello drones via IP addresses**  
✅ **Automatic takeoff and coordinated flight**  
✅ **Multithreading for simultaneous movements of multiple drones**  
✅ **Safe landing and disconnection**  

---

