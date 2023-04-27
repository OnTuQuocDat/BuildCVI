from popup_window import *
import socket
import time

# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)

#Connect to Rofin server, install callnback function
def TCP_init():
    portNum = 1234

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    tempBuf = IPAddr

    # time.sleep(0.001)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (tempBuf,portNum)
    s.connect(server_address)    
    # time.sleep(0)
    print("Connection to Rofin server established")
    

    

#Start marking
def send_AS():
    transmitBuf = []
    receiveBuf = []

    #Client Send data to server
    if ClientTCPWrite() < 0:
        pop_up_content("TCP/IP transmition error")
