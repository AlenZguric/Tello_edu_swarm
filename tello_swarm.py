from threading import Thread
from time import sleep
from djitellopy import TelloSwarm, Tello

# Definicija dronova i njihovih IP adresa
drones = {
    "Alen": "192.168.137.107",
    "Goran": "192.168.137.52",
}

# Povezivanje svih dronova putem njihovih IP adresa
All = TelloSwarm.fromIps([ip for ip in drones.values()])

# Inicijalizacija pojedinačnih dronova i dodavanje imena
drone_objects = {}
for name, ip in drones.items():
    drone = Tello(ip)
    drone.drone_name = name  # Dodajemo atribut za ime
    drone_objects[name] = drone

# Maksimalna visina
MAX_HEIGHT = 100

def execute_command(drone_name, drone, command, *args):
    """Izvršava komandu i prikazuje ime drona u ispisu"""
    try:
        print(f"🛸 {drone_name} izvodi naredbu: {command} {args}")
        response = getattr(drone, command)(*args)
        sleep(1)  # Pauza za stabilnost
        print(f"✅ {drone_name} response: {response}")  # Dodan response u output
    except Exception as e:
        print(f"⚠️ Greška kod drona {drone_name}: {str(e)}")

# 🔋 Dohvati stanje baterije i prikaži ime drona
def get_battery_status(drone_name, drone):
    """Dohvaća stanje baterije drona i ispisuje ime drona u response"""
    try:
        battery = drone.send_command_with_return("battery?")  # Ispravan način dohvaćanja baterije
        print(f"🔋 Stanje baterije na {drone_name} dronu ({drones[drone_name]}) je {battery}%")
        return battery
    except Exception as e:
        print(f"⚠️ Greška pri dohvaćanju baterije za {drone_name}: {str(e)}")
        return None

# 🔥 Spektakularni manevri 🔥
def spiral_maneuver(drone_name, drone):
    """Dron leti u spirali prema gore"""
    for _ in range(5):
        execute_command(drone_name, drone, 'move_up', 10)
        execute_command(drone_name, drone, 'rotate_clockwise', 45)
        execute_command(drone_name, drone, 'move_forward', 50)

def wave_movement(drone_name, drone):
    """Dron se kreće sinusoidno (gore-dolje)"""
    for _ in range(3):
        execute_command(drone_name, drone, 'move_up', 20)
        execute_command(drone_name, drone, 'move_down', 20)
        
def drone_dance():
    """Svi dronovi sinkronizirano plešu u zraku"""
    for _ in range(3):
        print("🕺 Svi dronovi plešu!")
        All.move_left(50)
        All.move_right(50)
        All.rotate_clockwise(90)
        All.rotate_counter_clockwise(90)

# Poveži dronove i započni show
print("🔌 Povezivanje dronova...")
All.connect()

# Provjera baterije svakog drona prije leta
for name, drone in drone_objects.items():
    get_battery_status(name, drone)

print("🚀 Svi dronovi polijeću!")
All.takeoff()

# Početni formacijski let
All.move_up(30)
All.move_forward(100)
All.rotate_clockwise(90)

# Pokretanje spektakularnih manevra u odvojenim threadovima
threads = []
for name, drone in drone_objects.items():
    if name == "Alen":
        t = Thread(target=wave_movement, args=(name, drone))
    elif name == "Goran":
        t = Thread(target=wave_movement, args=(name, drone))
    else:
        continue  # Ako ima više dronova, dodaj nove manevre ovdje

    threads.append(t)
    t.start()

# Čekamo završetak svih manevra
for t in threads:
    t.join()
sleep(2)

# Završni ples u zraku
drone_dance()

# Sigurno spuštanje
print("🛬 Svi dronovi slijeću...")
All.land()
All.end()
