# You have to write a forever executable python program to read sensor data and send it to the cloud server.
import socket
import pandas

df = pandas.read_csv('dataset.csv')
print(df)

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 80        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(df)
    data = s.recv(1024)

print('Received', repr(data))
