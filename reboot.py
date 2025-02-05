from djitellopy import Tello

drone= Tello()
drone.connect()
print("dron je spojen")
drone.reboot()
print("dron je rebootan")