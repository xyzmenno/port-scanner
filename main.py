import socket
import subprocess
import sys

ip_input = input("enter ip: ")
serverip = socket.gethostbyname(ip_input)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((serverip, port))
        if result == 0:
            print(f"port is open {port}")


except KeyboardInterrupt:
    print("stopped")
    sys.exit()

except socket.error:
    print("error")
    sys.exit()
    
