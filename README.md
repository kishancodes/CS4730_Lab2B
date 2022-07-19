This exercise involves development of a Web Server. This Web Server i) creates a connection when contacted by a client (browser), ii) receives HTTP requests from this connection; iii) parses the request to find the file being requested iv) get the file from the server file system and send the response over the TCP connection to the browser. If the requested file is not available in your server, your server should return, “404 file not found.”

The skeleton code for the server is given below. Complete the code and run the server. Test it by sending requests from browsers.

To run the server:

Put a test HTML file (e.g., HelloWorld.html) in the same directory that the server is in. Run the server program. Determine the IP address of the host that is running the server (e.g., 128.238.251.26). From another host, open a browser and provide the corresponding URL. For example: http://128.238.251.26:6789/HelloWorld.html ‘HelloWorld.html’ is the name of the file you placed in the server directory. Replace the port# 6789 with whatever port you have used in the server code (do not use reserved port numbers). The browser should then display the contents of HelloWorld.html 
