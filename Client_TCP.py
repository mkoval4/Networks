'''
 Maksym Koval - 250848178 - October 17, 2018
 Client_TCP.py - Assignment 2 - 3357A
 The following program allows user to enter text commands to be sent to the server
 It also displays response back from server
'''

import socket 

TCP_IP = '192.168.180.1'
TCP_PORT = 5005

#Create socket using IP and Port specified 
print("Attempting to contact server at ", TCP_IP, ":", TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Used to catch errors in case incorrect IP or Port is being used
try:
    #connect to the server on the provided IP and Port
    s.connect((TCP_IP, TCP_PORT))
    print("Connection to Server established!")
except socket.error as serr:
    print("There was an error connecting to server, please provide valid addresses")
    s.close()
    quit()


#Prompt user for a message to send to server
message = input("send: ")

#Our message is sent using the established socket 
s.send(message.encode())

#Using TCP wait for reply on the socket of the size 1024 bytes or smaller
m_reply = s.recv(2048)

#OUTPUT
print(m_reply.decode())

#Close out the connection 
s.close()
print("Session complete")
