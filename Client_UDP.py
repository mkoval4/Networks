'''
 Maksym Koval - 250848178 - October 17, 2018
 Client_UDP.py - Assignment 2 - 3357A
 The following program allows user to enter text commands to be sent to the server
 It also displays response back from server
'''
import socket

UDP_IP = "192.168.180.1"
UDP_PORT = 5005

#Set up the internet and UDP connection
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("send: ")

try:
    #Send the message 
    print("Attempting to send message...")
    sent = s.sendto(message.encode(), (UDP_IP, UDP_PORT))

    #Receive response
    reply, server = s.recvfrom(2048) 
    print(reply.decode("ascii"))
except socket.error as serr:
    print("There was an error connecting to the server")

#Free up the socket
print("Exiting Client")

