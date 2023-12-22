"""
This script is a simple example of how Python's socket library can be used to interact with web servers.
It's an excellent starting point for understanding network programming and the basics of client-server communication in Python.
"""

import socket  # Import the socket module for network connections.

# Create a socket object.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET refers to the address family ipv4, SOCK_STREAM indicates a TCP connection.

# Server details.
server = 'pythonprogramming.net'  # Web server domain.
port = 80  # HTTP port.

# Retrieve the IP address of the server.
server_ip = socket.gethostbyname(server)  # Converts the domain to its corresponding IP address.
print('Server IP: ' + server_ip)  # Print the IP address of the server.

# HTTP request.
request = "GET / HTTP/1.1\nHost: "+server+"\n\n"  # HTTP GET request string.

# Establish a connection to the server.
s.connect((server, port))  # Connect to the server using the defined port.
s.send(request.encode())  # Send the GET request to the server.

# Receiving the server's response.
result = s.recv(4096)  # Receive up to 4096 bytes from the server.

# Print the server's response.
print(result.decode())  # Decode and print the server's response.

# Close the socket.
s.close()  # Close the connection to free up resources.
