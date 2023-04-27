import socket

def test1():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your computer name is: ",hostname)
    print("Yopur computer IP Address is: ",IPAddr)


def test_TCPinit():
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


test_TCPinit()