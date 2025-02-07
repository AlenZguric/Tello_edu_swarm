from djitellopy import TelloSwarm
import time

# Initialize a swarm of 4 Tello drones with their IPs (in your local network range)
# Replace these with the actual IPs of your drones
drones = TelloSwarm.from_ips(['192.168.10.1', '192.168.10.2', '192.168.10.3', '192.168.10.4'])

def check_battery_and_safety(drones):
    # Check the battery status of all drones, if any drone has less than 20%, return False
    for drone in drones:
        battery = drone.get_battery()
        print(f"Drone {drone.get_ip()} battery: {battery}%")
        if battery < 20:  # Define a low battery threshold for safety
            return False
    return True

def stop_and_land_all(drones):
    """Stop all drones' movements and land them in case of error or safety failure."""
    print("Error occurred or battery below 20%, stopping and landing all drones.")
    
    # Send stop command to all drones to halt any movement
    for drone in drones:
        try:
            drone.send_control_command('stop')
        except Exception as e:
            print(f"Error stopping drone {drone.get_ip()}: {e}")
    
    # Wait for 3 seconds before landing all drones
    time.sleep(3)
    drones.land()

def first_row_movement(drones):
    try:
        # First row: Drone 1 and Drone 2 go up and back
        drones.takeoff()
        drones.set_speed(30)

        # Safety check for battery or if a drone can't go up
        if not check_battery_and_safety(drones):
            print("Safety check failed: Low battery or drone issue. Landing drones.")
            stop_and_land_all(drones)
            return

        # Drone 1 and Drone 2 go up
        drones.move_up(50)
        time.sleep(2)

        # Drone 1 and Drone 2 move back
        drones.move_back(100)
        time.sleep(5)

        drones.land()

    except Exception as e:
        # If any error occurs, print the exception and safely land all drones
        print(f"An error occurred during first row movement: {e}")
        stop_and_land_all(drones)

def second_row_movement(drones):
    try:
        # Second row: Drone 3 and Drone 4 go forward and up
        drones.takeoff()
        drones.set_speed(30)

        # Safety check for battery or if a drone can't go up
        if not check_battery_and_safety(drones):
            print("Safety check failed: Low battery or drone issue. Landing drones.")
            stop_and_land_all(drones)
            return

        # Drone 3 and Drone 4 go forward
        drones.move_forward(100)
        time.sleep(3)

        # Drone 3 and Drone 4 go up
        drones.move_up(50)
        time.sleep(2)

        drones.land()

    except Exception as e:
        # If any error occurs, print the exception and safely land all drones
        print(f"An error occurred during second row movement: {e}")
        stop_and_land_all(drones)

def start_swarm():
    try:
        # Split the swarm into two rows: drones 1,2 and drones 3,4
        first_row_drones = drones[:2]
        second_row_drones = drones[2:]

        # Execute movements for both rows in parallel
        first_row_movement(first_row_drones)
        second_row_movement(second_row_drones)

    except Exception as e:
        # If an error occurs at any point in the swarm, print it and land all drones
        print(f"An error occurred during swarm operation: {e}")
        stop_and_land_all(drones)

# Start the swarm operations
start_swarm()
