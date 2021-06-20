import math
import socket
import sys
import time
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode('\nCALCULATOR'))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        try:
            operation, val = data.split(" : ")
            opt = str(operation)
            num = float(val)

            if opt[0] == 'l':
                opt = 'Log Statement'
                ans = math.log10(num)
            elif opt[0] == 's':
                opt = 'Square Root'
                ans = math.sqrt(num)
            elif opt[0] == 'e':
                opt = 'Exponential'
                ans = math.exp(num)
            else:
                answer = ('Invalid')

            sendAns = (str(opt)+ ' ['+ str(num) +' ] = ' + str(ans))
            print ('Calculation complete ;)')
        except:
            print('...Client has exited...')
            sendAns = ('...Client has exited...')

        if not data:
            break

        s_sock.send(str.encode(str(sendAns)))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("Listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                print("Connected")
                p.start()

            except socket.error:

                print('Got socket error')

    except Exception as e:
                print("An exception occurred!")
                print(e)
    finally:
     	   s.close()
