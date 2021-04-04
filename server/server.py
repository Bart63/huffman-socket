from txtHandler import txtHandler
import socket
import time
import unicodedata

HEADERSIZE = 8

def sendFileServer(tree):
    # Inicjalizacja gniazda z IPv4 i protokołu do komunikacji strumieniowej TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Nasłuchuj dane gniazdo (IPv4, port)
    s.bind(('192.168.8.107', 1243))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        print(f"Połączono z {address}.")
        msg = tree + txtHandler().getEncoded()
        msg = msg.encode("utf-8")
        msg = b''.join([(f"{len(msg):<{HEADERSIZE}}").encode("utf-8"), msg])
        clientsocket.send(msg)
        print("Wysłano wiadomość")
        time.sleep(5)

    s.close()