from socket import *
import sys
serverPort = 6788
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("web server on port: ",serverPort)

while True:
	print("The server is ready to receive")
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		print (message,'::',message.split()[0],':',message.split()[1])
		filename = message.split()[1]
		print (filename,'||',filename[1:])
		f = open(filename[1:])
		outputdata = f.read()
		print (outputdata)
		f.close()
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()
	except IOError:
		print ("404 Not Found")
		connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
		connectionSocket.send('<html><head></head><body><p>404 NOT FOUND </p></body></html>\r\n'.encode())
		connectionSocket.close()
serverSocket.close()
sys.exit()