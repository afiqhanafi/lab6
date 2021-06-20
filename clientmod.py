import socket
import signal
import sys

ClientSocket = socket.socket()
host = '192.168.43.14'
port = 8888

print('Connecting...')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    print("Function available :")
    print("Log statement(log)")
    print("Square Root(sqrt)")
    print("Exponential(exp)")
    Input = input('\nFunction you want to use : ')

    if Input == 'log' or Input == 'sqrt' or Input == 'exp':
        num = input("Input number : ")
        Input = Input + " : " + num
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))

    elif Input == 'exit':
        break

    else:
        print("The function not available is log,sqrt,exp and exit only. Try again")
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

ClientSocket.close()

