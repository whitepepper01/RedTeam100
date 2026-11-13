import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #opens the socket, this one is a bit different because it's not using the TCP SOCK_. DGRAM is the UDP one.

s.bind(("127.0.0.1",8888)) #Binds the socket to a port on local host, port 8888

Users=[] #starts an empty list of all the users that will be in this chat.

#Chatroom will stay alive with this while loop.
while True:
	conn, addr = s.recvfrom(1024)	# Getting the IP and Port of the person sending the message. The text goes in conn, the IP and Port go into addr.
	if addr not in Users: #If the address is not in the list of users already, add it to the list of Users
		Users = [addr] + Users #Adding the Tuple of addr into the user list.
    for x in Users: #For loop goes through everyone in the list, one at a time
        if x != addr: # If a user wasn't the person who sent it..
            s.sendto(conn,x) #Send the message to everyone else
