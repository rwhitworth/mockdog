import socket
import sys
import re
import time

msg_format = re.compile(
    r"(?P<name>.*?):(?P<value>.*?)\|(?P<type>[a-z])\|#(?P<tags>.*)"
)

def bind_udp(ip=None, port=None):
    ip = ip or "0.0.0.0"
    port = port or 8125
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    return sock

def process(msg):
    m = msg_format.match(msg)
    if not m:
        print("mockdog message: `Regex Error` " + msg)
    else:
        msgs = msg.split("\n")
        for q in msgs:
            t = time.strftime("%Y-%m-%d %H:%M:%S ")
            print(t+q)

if __name__ == "__main__":
    sock = bind_udp()
    while True:
        data, addr = sock.recvfrom(65507)
        process(data.decode("utf-8"))
