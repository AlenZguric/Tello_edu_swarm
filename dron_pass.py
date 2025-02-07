import os

def getIps():
    # Pozivanje komande za prikaz ARP tabele (Windows)
    result = os.popen('arp -a').read()
    #print(result)
    drone_ips, drone_mac = [], ["48-1c-b9-9b-fd-68", "48-1c-b9-9b-fd-69", "48-1c-b9-9b-fd-6a", "48-1c-b9-99-73-fe", \
                                "48-1c-b9-9b-fd-2f", "48-1c-b9-9b-fd-76", "48-1c-b9-99-7e-bf", "48-1c-b9-9b-fd-7b", \
                                "48-1c-b9-9b-fe-22", "48-1c-b9-9b-fd-c3", "48-1c-b9-99-7e-ba", "48-1c-b9-99-7d-2f"]
    for i in drone_mac: 
        j = result.find(i)
        if j>0: drone_ips.append(result[j-22:j].strip())
    #print(drone_ips)
    return drone_ips
