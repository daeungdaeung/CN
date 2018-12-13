from socket import *
# For execute python files in python file.
import subprocess

serverPort = 12006
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    subprocess.call(['python', 'ComputerClient.py'])
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    connectionSocket.close()
