from socket import *

serverPort = 12006
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    connectionSocket.close()

    import subprocess

    # For execute python files in python file.

    while True:
        Input = input('Put: ')
        if 'quit' == Input:
            break
        else:
            subprocess.call(['python', 'ComputerClient.py'])




