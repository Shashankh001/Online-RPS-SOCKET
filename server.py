import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',1234))
s.listen(100)


while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("You have joined a game of ROCK PAPER SCISSORS!!", "utf-8"))
    print("The opponent has joined the game!")

    g_input = str(input("Choose your object! [R, P, S]: "))
    clientsocket.send(bytes(g_input,"utf-8"))

    server_input = clientsocket.recv(1024)
    output = server_input.decode("utf-8")
    output = str(output)
    print(f"The opponent used: {output}")

    result_recv = clientsocket.recv(1024)
    result = result_recv.decode("utf-8")
    print(result)

    quit()