import socket;
s = socket.socket();
print("socket created");
port = 4567;
s.bind((",port"));
print("Socket bind to %s" %(port));
s.listen(5);
print ("socket is listening...");
while True:
    c, addr = s.accept();
    print("Connection from",addr);