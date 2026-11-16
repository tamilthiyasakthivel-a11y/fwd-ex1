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