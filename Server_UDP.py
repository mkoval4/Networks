'''
 Maksym Koval - 250848178 - October 17, 2018
 Server_UDP.py - Assignment 2 - 3357A
 The following prgram accepts UDP commands from a client
 and responds back to the client
'''

import socket
import time 
import errno

UDP_IP = "192.168.180.1"
UDP_PORT = 5005

#Create socket using datagram based protocal
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Establishing Server...")

try:
    #Bind the socket with corrrect IP and Port
    s.bind((UDP_IP, UDP_PORT))

#Catch errors if the port is in use or IP is wrong
except socket.error as serr:
    print("There was an error in creating the server, please enter valid a address.")
    quit()

while True:
    data, addr = s.recvfrom(4096) #BUFFER SIZE
    print("Client inquiry received")

    #Handle the user request 
    if data.decode("ascii") == "What is the current date and time?":
        reply = "Current Data and Time - " + time.strftime("%m/%d/%Y %H:%M:%S")
    else:
        reply = "Your request is not yet supported"
    
    sent = s.sendto(reply.encode(), addr)
    print("Reply sent...")






