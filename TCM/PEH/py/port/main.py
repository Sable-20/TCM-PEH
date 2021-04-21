import sys
import socket
from datetime import datetime

# define targets
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # translate hostname to IPv4
else:
    print("Invalid amount of arguments")

# banner
print("--==[ IP SWEEPER ]==--\n\n\n")
print("-" * 50)
print(f"Scanning target: {target}")
print(f"time started: {str(datetime.now())}")
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socker(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"port {port} is open")
        s.close()
except Exception as err:
    print("Error: {}".format(err))
except KeyboardInterrupt:
    print("Exiting...\n")
    sys.exit()
except socket.gaierror:
    print("hostname could not be resolved\n")
    sys.exit()
except socket.error:
    print("couldnt connect to server...\n")
    sys.exit()