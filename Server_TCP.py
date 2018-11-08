'''
 Maksym Koval - 250848178 - October 17, 2018
 Server_TCP.py - Assignment 2 - 3357A
 Only handles one client interaction at a time, can listen on any IP & port you choose
 Responds to invalid requests with an error message, valid request is “What is the current date and time?”
 Response to valid request must be in the format: “Current Date and Time – MM/DD/YYYY hh:mm:ss”
'''
import time
import socket 
import errno

TCP_IP = "192.168.180.1"
TCP_PORT = 5005

#Create socket using connection-based protocol 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Establishing server...")

try:
    #used for TCP connection establishment 
    s.bind((TCP_IP, TCP_PORT))
    
#Catch errors if the port is in use or IP is wrong
except socket.error as serr:
    print("There was an error in creating the server, please enter valid a address.")
    s.close()
    quit()


run_exec = True

while run_exec:
    #listen for a client request
    s.listen(1)

    #Accept a connection, where conn is a socket object
    conn, addr = s.accept()

    #OUTPUT
    print("Connection to Client Established!")
    print("Server Address: ", TCP_IP)
    print("Client Address: ", addr)
    
    #Receive client request using recv (TCP)
    request = conn.recv(2048)
    
    #Acknowledge received request
    print("Client inquiry received" )

    #Handle the user request 
    if request.decode('ascii') == "What is the current date and time?":
        reply = "Current Date and Time - " + time.strftime("%m/%d/%Y %H:%M:%S")
    
    #EXIT REQUEST
    elif request.decode('ascii') == "exit": 
        run_exec = False
        reply = "Shutting down server..."
    
    #Unsupported cases
    else:
        reply = "Your request is not yet supported"

    #Now that we have the reply we can send it 
    print("Sending Response...")
    conn.send(reply.encode())   
    print("Disconnecting from client...")

print("Shutting down server...")
s.close()
quit()