import socket

# socket.AF_INET = The IPv4 address
# socket.SOCK_STREAM = TCP Connection, if this was UDP, it would be interchanged with socket.SOCK_DGRAM

# Module of socket gets imported, socket() function is used, and the constants that are defined in that variable are socket.AF_INET, and socket.SOCK_STREAM. This is all being defined in a variable called 's'. We just opened a socket to start the process.
# s is the "front desk", checking in the new clients

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind only accepts one argument. I learned that if you were to use, for instance, s.bind(127.0.0.1,8888), it won't work. That would create two arguments. Technically you can use a list here, but it makes more sense to use a "tuple", which is basically a fixed list if I understand it correctly. The IP and port which the socket is binding to should not be changing.
# Bind is like "reserving a room" for the client.

s.bind(("127.0.0.1",8888))

# Have the server start listening using s.listen(). This puts the server in "waiting mode".
# Listen "props the door open"

s.listen()

# s.accept() returns two values that can both be grabbed at once. A 'conn' and 'addr'. Conn and addr are technically empty variables until s.accept() pulls them out into something they can work with.
# Accept is like the receptionist letting the next client in. Conn is like a staff member to help that client specifically. Addr is the client's ID badge, where they "came from" (IP and Port).

conn, addr = s.accept()

# Data defined as a variable where we are connecting a recieving up to 1024 bytes of information.

data = conn.recv(1024)

# Decodes that data so it becomes human readable

print(data.decode())





