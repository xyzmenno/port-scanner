import socket
import sys

target_input = input("enter ip: ")
target = socket.gethostbyname(target_input)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target_input, port))
        if result == 0:
            print(f"port is open {port}")
        s.close()


except KeyboardInterrupt:
    print("stopped")
    sys.exit()

except socket.error:
    print("error")
    sys.exit()
    
