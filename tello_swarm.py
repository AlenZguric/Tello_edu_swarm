from threading import Thread
from time import sleep
from djitellopy import TelloSwarm, Tello


# Definicija dronova i njihovih IP adresa
# Definicija IP adresa dronova
dron1 = "192.168.137.78"
dron2 = "192.168.137.142"
dron3 = "192.168.137.205"
dron4 = "192.168.137.234"
#dron5 = "192.168.137.227"
#dron6 = "192.168.137.132"
dron7 = "192.168.137.60"
dron8 = "192.168.137.218"
dron9 = "192.168.137.155"
#dron10 = "192.168.137.176"
dron11 = "192.168.137.135"
#dron12 = "192.168.137.82"



# Organizacija dronova u redove
prvi_red = [dron1, dron2, dron3, dron4,  ]
drugi_red = [dron7, dron8, dron9, dron11 ]


# Kreiramo listu svih dronova
svi_dronovi = prvi_red + drugi_red 

# Povezivanje svih dronova putem njihovih IP adresa
All = TelloSwarm.fromIps(svi_dronovi)

# Inicijalizacija pojedinačnih dronova i dodavanje imena
# Inicijalizacija dronova s imenima Red_X_Dron_Y
drone_objects = {}
for i, row in enumerate([prvi_red, drugi_red], start=1):
    for j, ip in enumerate(row, start=1):
        name = f"Red_{i}_Dron_{j}"
        drone = Tello(ip)
        drone.drone_name = name
        drone_objects[name] = drone




def execute_command(drone_name, drone, command, *args):
    """Izvršava komandu i prikazuje ime drona u ispisu"""
    try:
        print(f"🛸 {drone_name} izvodi naredbu: {command} {args}")
        response = getattr(drone, command)(*args)
        sleep(1.5)  # Pauza za stabilnost
        print(f"✅ {drone_name} response: {response}")  # Dodan response u output
    except Exception as e:
        print(f"⚠️ Greška kod drona {drone_name}: {str(e)}")

# 🔋 Dohvati stanje baterije i prikaži ime drona
def get_battery_status(drone_name, drone):
    """Dohvaća stanje baterije drona i ispisuje ime drona u response"""
    try:
        battery = drone.get_battery()
        print(f"🔋 Stanje baterije na {drone_name} je {battery}%")
        return battery
    except Exception as e:
        print(f"⚠️ Greška pri dohvaćanju baterije za {drone_name}: {str(e)}")
        return None


'''# 🔥 Spektakularni manevri 🔥
def spiral_maneuver(drone_name, drone):
    """Dron leti u spirali prema gore"""
    for _ in range(3):
        execute_command(drone_name, drone, 'move_up', 30)
       # sleep(0.2)
        execute_command(drone_name, drone, 'rotate_clockwise', 45)
       # sleep(0.2)
        execute_command(drone_name, drone, 'move_forward', 50)
       # sleep(0.2)


def wave_movement(drone_name, drone):
    """Dron se kreće sinusoidno (gore-dolje)"""
    for _ in range(5):
         execute_command(drone_name, drone, 'move_up', 30)
        # sleep(0.2)
         execute_command(drone_name, drone, 'move_down', 25)
        
def drone_dance():
    """Svi dronovi sinkronizirano plešu u zraku"""
    for _ in range(3):
        print("🕺 Svi dronovi plešu!")
        All.move_left(50)
        All.move_right(50)
        All.rotate_clockwise(90)
        All.rotate_counter_clockwise(90)
'''
# Poveži dronove i započni show
print("🔌 Povezivanje dronova...")
All.connect()



# Provjera baterije svakog drona prije leta
for name, drone in drone_objects.items():
    get_battery_status(name, drone)


print("🚀 Svi dronovi polijeću!")
All.takeoff()

# Početni formacijski let
def prviRed():
    for i, row in enumerate([prvi_red], start=1):
        print(f"🚀 Red {i} izvodi manevar...")
        row_swarm = TelloSwarm.fromIps(row)
        row_swarm.move_up(120)
        row_swarm.move_back(100)
        row_swarm.move_down(120)
        row_swarm.move_forward(100)
        
        

    
def drugiRed():
    for i, row in enumerate([drugi_red], start=1):
        print(f"🚀 Red {i} izvodi manevar...")
        row_swarm = TelloSwarm.fromIps(row)
        row_swarm.move_forward(100)
        row_swarm.move_up(100)
        row_swarm.move_back(100) 
        row_swarm.move_down(100)
      

        
    

    
'''def wave_movement(drone_name, drone):
    print(f"{drone_name} slijeće")
    drone.land()'''
    
#All.sequential(lambda i, drone: drone.land())

'''def keep_alive():
    for i in All:        
        i.send_read_command("command")
        
keep_alive(prvi_red, drugi_red)'''
        

        
# for i in All.tellos: i.send_read_command("rc 0 0 0 0")
    

    
 

'''for name in ["Danijel", "Goran", "Zadnji"]:
    if name not in drone_objects: 
        name.send_rc_control(0,0,0,0)# Provjeri postoji li dron u rječniku
    else:   
        drone_objects[name].move_up(30)
       
        #drone_objects[name].flip_forward()'''
        
#All.send_rc_control(0,0,0,0)
'''All.move_up(30)
All.move_forward(100)
All.rotate_clockwise(90)'''


t1 = Thread(target=prviRed)

t2 = Thread(target=drugiRed)

# Pokretanje spektakularnih manevra u odvojenim threadovima
'''threads = []
for name, drone in drone_objects.items():
    if name == "Alen":
        t = Thread(target=wave_movement, args=(name, drone))
    elif name == "Djuro":
        t = Thread(target=wave_movement, args=(name, drone))
    elif name == "Goran":
        t = Thread(target=wave_movement, args=(name, drone))
    elif name == "Danijel":
        t = Thread(target=wave_movement, args=(name, drone))
    elif name == "Zadnji":
        t = Thread(target=wave_movement, args=(name, drone))
    elif name == "Predzadnji":
        t = Thread(target=wave_movement, args=(name, drone))
    else:
        continue  # Ako ima više dronova, dodaj nove manevre ovdje

    threads.append(t)
    t.start()'''
    
t1.start()
t2.start()
# Čekamo završetak svih manevra
t1.join()
t2.join()


# Završni ples u zraku
#drone_dance()

# Sigurno spuštanje
print("🛬 Svi dronovi slijeću...")
All.land()

for name, drone in drone_objects.items():
    get_battery_status(name, drone)
    
All.end()
