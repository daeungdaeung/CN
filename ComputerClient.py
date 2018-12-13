from socket import *

serverName = '192.168.0.14'
serverPort = 12014
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input: ')
clientSocket.send(sentence.encode())
clientSocket.close()
