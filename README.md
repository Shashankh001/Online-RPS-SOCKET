# Online-RPS-SOCKET

Lets explore this amazing code of rock paper scissors.

Since this is a client-server based program, there will be two files:- `client.py` and `server.py`. The one whose computer shall be shutted down must be running `server.py`.

`server.py`
```py
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
```

Let us now have a look at the `client.py` file.
```py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.102',1234))

while True:
    welcome_msg = s.recv(1024)
    f_msg = welcome_msg.decode("utf-8")
    print(f_msg)

    g_input = str(input("Choose your object! [R, P, S]: "))
    s.send(bytes(g_input,"utf-8"))
    print("Waiting for the opponents answer...")

    server_input = s.recv(1024)
    output = server_input.decode("utf-8")
    output = str(output)
    print(f"The opponent used: {output}")

    if g_input == output :
        print("Draw")
        s.send(bytes("Draw", "utf-8"))

    elif g_input == str("R") and output == str("P") :
        print("You Lose")
        s.send(bytes("You Win", "utf-8"))

    elif g_input == str("P") and output == str("R") :
        print("You Win", "utf-8")
        s.send(bytes("You Lose", "utf-8"))

    elif g_input == str("S") and output == str("R") :
        print("You lose")
        s.send(bytes("You Win", "utf-8"))

    elif g_input == str("R") and output == str("S") : 
        print("You Win")
        s.send(bytes("You Lose", "utf-8"))

    elif g_input == str("S") and output == str("P") :
        print("You Win")
        s.send(bytes("You Lose", "utf-8"))

    elif g_input == str("P") and output == str("S") :
        print("You Lose")
        s.send(bytes("You Win", "utf-8"))
    
    quit()
```
Note: The `server.py` should be ran before `client.py` is run.

Let's now test the game!

`server.py` output:
```
Connection from ('192.168.0.102', 63316) has been established
```
Once the client joins, the game shall start and you can choose your object.
```
The opponent has joined the game!
Choose your object! [R, P, S]: S
```

Once the client has given his input as well, the game shall proceed into the decision making, giving the following output:
```
The opponent used: R
You Lose
```

