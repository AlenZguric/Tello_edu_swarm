from threading import Thread
from time import sleep
from djitellopy import TelloSwarm, Tello

# Pomoću Tello Edu aplikacije i hot spota unesite IP adrese dronova
All = TelloSwarm.fromIps([
    '192.168.137.61',  # IP adresa prvog drona
    '192.168.137.182',   # IP adresa drugog drona
    '192.168.137.177'    # IP adresa trećeg drona
])

# Unesite različita imena varijabli za dronove u swarmu
drone1 = TelloSwarm.fromIps(['192.168.137.61'])  # Prvi dron
drone2 = TelloSwarm.fromIps(['192.168.137.182'])  # Drugi dron
drone3 = TelloSwarm.fromIps(['192.168.137.177'])  # Treći dron

# Maksimalna visina leta
MAX_HEIGHT = 170

def execute_command(drone, command, *args):
    """Izvršava komandu i čeka potvrdu da je završena"""
    try:
        getattr(drone, command)(*args)
        sleep(2)  # Pauza za stabilnost
    except Exception as e:
        print(f"Greška kod drona {drone}: {str(e)}")

# Funkcija za žongliranje dronova
def drone1_juggle():
    for _ in range(3):
        execute_command(drone1, 'move_up', min(50, MAX_HEIGHT - 40))
        execute_command(drone1, 'move_forward', 150)
        execute_command(drone1, 'move_down', 50)
        execute_command(drone1, 'move_back', 50)

def drone2_juggle():
    sleep(1)  # Lagano kašnjenje kako bi izgledalo kao žongliranje
    for _ in range(3):
        execute_command(drone2, 'move_up', min(50, MAX_HEIGHT - 20))
        execute_command(drone2, 'move_forward', 120)
        execute_command(drone2, 'move_down', 50)
        execute_command(drone2, 'move_back', 50)

def drone3_juggle():
    sleep(2)  # Još jedno kašnjenje kako bi izgledalo kao izmjena loptica
    for _ in range(3):
        execute_command(drone3, 'move_up', min(50, MAX_HEIGHT - 50))
        execute_command(drone3, 'move_forward', 150)
        execute_command(drone3, 'move_down', 50)
        execute_command(drone3, 'move_back', 50)

# Povežite dronove i započnite let
All.connect()

# Provjeri bateriju prije leta
'''battery_levels = [drone.get_battery() for drone in [drone1, drone2, drone3]]
if min(battery_levels) < 20:
    print("Baterija je preniska! Nemojte letjeti.")
    All.end()
    exit()'''

All.takeoff()

# Pokrećemo zasebne threadove za svaki dron s različitim uzorcima leta
t1 = Thread(target=drone1_juggle)
t2 = Thread(target=drone2_juggle)
t3 = Thread(target=drone3_juggle)

t1.start()
t2.start()
t3.start()

# Čeka završetak svih threadova
t1.join()
t2.join()
t3.join()

# Sigurno spuštanje i prekid veze
All.land()
All.end()
