"""
The script is a rudimentary tool for network diagnostics,
 particularly useful for testing network security and server configuration.
It iterates through a range of ports, checking each for connectivity.
"""

import socket  # Import the socket library for network interactions.

# Create a socket object.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET is for IPv4, SOCK_STREAM is for TCP.

# Target server details.
server = 'pythonprogramming.net'  # Define the server address.
port = 80  # Define the port to connect.

# Function to check if a port is open.
def pscan(port):
    try:
        s.connect((server, port))  # Try to connect to the server on the specified port.
        return True  # If the connection is successful, the port is open.
    except:
        return False  # If the connection fails, the port is closed.

# Scan ports 75 to 85.
for x in range(75, 86):
    if pscan(x):
        print(f'Port {x} is open')  # Print if the port is open.
    else:
        print(f'Port {x} is closed')  # Print if the port is closed.
