##!/usr/bin/env python
# -*- coding: utf-8 -*-

#---Device for Controler(Client)

#Packages
import socket
import sys
import time
import bluetooth

#Settings
PORT =1
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

def main():
    print("connect...")
    server_socket.bind( ("",PORT ))
    server_socket.listen(1)
    
    client_socket,address = server_socket.accept()
    
    print("connection success!!")
    
    while 1:
        try:
            data = client_socket.recv(1024)
            print("receive [%s]" % data)
            print('\n')
        except KeyboardInterrupt:
            client_socket.close()
            server_socket.close()
            break
        except:
            print("error")
            print('\n')
            client_socket.close()
            server_socket.close()
            break

if __name__ == '__main__':
    main()

#---END---