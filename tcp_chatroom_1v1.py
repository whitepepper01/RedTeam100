# I actually am taking the concept of the original tcp_server that is another script, and just basically creating a loop (obviously with some help of the internet and AI).
# Conceptually I'm thinking of taking basically creating a loop somewhere, probably after a listen I'm guessing? Or perhaps the whole thing can go in a loop.


# Required module for using socket
import socket

# Initialize the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific port and IP address
s.bind(("127.0.0.1",8888))

# Start the listener
s.listen()

#Accept the connection from the client
conn, addr = s.accept()

#This is actually where the loop should start. We don't want it to necessary loop the connection and socket binding, start, etc.

while True:


  data = conn.recv(1024)
  print(data.decode())
  reply = input("")
  conn.send((reply + "\n".encode())

  
  
# Data gets recieved just like before. But we added the reply variable which takes the input of the server, and then the conn.send is sending the encoded reply.
# REMINDER: Add a new line somehow when doing the conn.send because the client then has to write on the new line afterwards. At first I tried
# conn.send('\nreply.encode()) But I guess the proper syntax would be like conn.send((reply + "\n".encode())
