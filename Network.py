import threading, socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
#host = socket.gethostname()
host = "192.168.42.129"

port = 9999

# connection to hostname on the port.
s.connect((host, port))

def decode(message):
    # decode the incoming message
    command = message
    return command
    pass

def send(message, pitch, speed, stt="f"):
    message = str(pitch) + ":" + str(speed) + ":" + message + ":" + stt + "\r\n"
    s.send(message.encode('ascii'))
    # print("Sent: %s" % message)

def createSendThread(message, pitch, speed, stt="f"):
    sendThread = threading.Thread(target=lambda msg=message, pitch=pitch, speed=speed, stt=stt: send(msg, pitch, speed, stt))
    sendThread.start()
    time.sleep(1)

def receive():
    # createSendThread("STT", 0, 0)
    # print("waiting")
    input = s.recv(1024)
    input = input.decode('ascii')
    # print(input)
    return decode(input)

# receiveThread = threading.Thread(target=receive)

# receiveThread.start()
