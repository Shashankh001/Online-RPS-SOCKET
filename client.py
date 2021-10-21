import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('0.0.0.0',1234)) #use the ip of the computer you want to connect!

while True:
    msg = s.recv(1024)
    f_msg = msg.decode("utf-8")
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
    
