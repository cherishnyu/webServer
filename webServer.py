# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      
      #opens the client requested file.
      f = open(filename[1:], 'rb')
      
      file_content = f.read()
      content_length = len(file_content)

      # 200 OK Response Headers
      outputdata = b"HTTP/1.1 200 OK\r\n"
      outputdata += b"Server: SimplePythonServer\r\n" # Added Server
      outputdata += b"Connection: close\r\n"          # Added Connection
      outputdata += b"Content-Length: " + str(content_length).encode() + b"\r\n" # Added Content-Length
      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n\r\n"

      #Fill in start - append your html file contents
      outputdata += file_content
      #Fill in end
      
      #Send the content of the requested file to the client
      # Fill in start
      connectionSocket.sendall(outputdata)
      # Fill in end
      
      connectionSocket.close() #closing the connection socket
      
    except IOError:
      # Send response message for file not found (404)
      #Fill in start
      not_found_body = b"<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1><p>The requested file was not found on this server.</p></body></html>"
      not_found_length = len(not_found_body)

      not_found_header = b"HTTP/1.1 404 Not Found\r\n"
      not_found_header += b"Server: SimplePythonServer\r\n" # Added Server
      not_found_header += b"Connection: close\r\n"          # Added Connection
      not_found_header += b"Content-Length: " + str(not_found_length).encode() + b"\r\n" # Added Content-Length
      not_found_header += b"Content-Type: text/html; charset=UTF-8\r\n\r\n"
      
      connectionSocket.sendall(not_found_header + not_found_body)
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

    except Exception as e:
      print(f"An unexpected error occurred: {e}")
      connectionSocket.close()

  #serverSocket.close()
  #sys.exit() 

if __name__ == "__main__":
  webServer(13331)
