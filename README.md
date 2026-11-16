# EX01 Developing a Simple Webserver
## Date:16/11/2026
## Reg no:26018068
~~~
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>List of TCP Protocols</title>
</head>
<body>

    <h1>List of TCP Protocols</h1>

    <h2>Common TCP-Based Protocols</h2>

    <ol>
        <li>HTTP - Hypertext Transfer Protocol</li>
        <li>HTTPS - Hypertext Transfer Protocol Secure</li>
        <li>FTP - File Transfer Protocol</li>
        <li>SMTP - Simple Mail Transfer Protocol</li>
        <li>POP3 - Post Office Protocol</li>
        <li>IMAP - Internet Message Access Protocol</li>
        <li>SSH - Secure Shell</li>
        <li>Telnet - Teletype Network</li>
    </ol>

    <h2>Other TCP-Based Protocols</h2>

    <ul>
        <li>DNS - Domain Name System (can use TCP)</li>
        <li>LDAP - Lightweight Directory Access Protocol</li>
        <li>SMB - Server Message Block</li>
    </ul>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
~~~

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
![alt text](<../Screenshot 2026-11-14 160635.png>)
## OUTPUT:
![alt text](<../Screenshot 2026-11-14 160654.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.

