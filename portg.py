import cowsay
# import pyfiglet
import ipaddress
import sys
import socket
from datetime import datetime
tux=cowsay.kitty("HELLO THERE ! WLEACOME TO OUER PORT SCANNER")
# ascii_banner = pyfiglet.figlet_format("DADY")
# print(ascii_banner)
print(tux) 
target = input("Enter the IP address: ")


# ----------- IP VALIDATION -------------
while True:
    user_ip = target

    try:
        ipaddress.ip_address(user_ip)   # validates IPv4 / IPv6
        target = user_ip
        break                           # valid → exit loop
    except ValueError:
        print("Invalid IP!\n")




# Defining a target
# if len(sys.argv) == 2:
#     target = socket.gethostbyname(sys.argv[1])

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

open_ports = []   # <--- list to store open ports
 
try:
    # Scan ports 1 to 65 (you can change this)
    for port in range(1, 65):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)   # <--- store open port
        
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting Program !!!!")
    sys.exit()

except socket.gaierror:
    print("\nHostname Could Not Be Resolved !!!!")
    sys.exit()

except socket.error:
    print("\nServer not responding !!!!")
    sys.exit()

# After scanning:
print("\n" + "-" * 50)
print("Scan Completed!")
print("Open Ports:")

if open_ports:
    for p in open_ports:print(f" - Port {p} is open")
else:print("No open ports found.")
print("-" * 50)
