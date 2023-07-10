import socket
import time

while True:

    # Initialize Socket Instance
    sock = socket.socket()
    print ("Socket created successfully.")

    # Defining port and host
    port = 8800
    #host = '172.20.239.149'      #Wifi default ad
    #host = '192.168.1.39'        #ethernet default ad
    host = '127.0.0.1'            #localhost
    # Connect socket to the host and port
    sock.connect((host, port))
    print('Connection Established.')

    # Send a greeting to the server
    sock.send('A message from the client'.encode())

    # Write File in binary

    file = open('client-file.png', 'wb')

    # Keep receiving data from the server
    line = sock.recv(1024)

    while(line):
        file.write(line)
        line = sock.recv(1024)

    print('File has been received successfully, check client folder')
    file.close()
    time.sleep(0.1)
    
sock.close()
print('Connection Closed.')
