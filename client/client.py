import socket
from decoder import Decoder

HEADERSIZE = 8

print("Klient odkodowujący wiadomość. Autorzy:")
print("Bartosz Durys")
print("Filip Hajek")
print()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Numer IP serwera i jego numer portu
s.connect(('192.168.8.107', 1243))

full_msg = ''
new_msg = True
while True:
    # Pobierz 8 bajtów
    msg = s.recv(8)
    # Jak nowa wiadomość, to pobierz informację o długości pakietu
    # Jak nie, to dodaj następne znaki do wiadomości
    if new_msg:
        print("Długość przychodzącej wiadomości:", msg[:HEADERSIZE].decode("utf-8"))
        msglen = int(msg[:HEADERSIZE])
        new_msg = False
        full_msg = msg[HEADERSIZE:] 
    else:
        full_msg += msg
	
    print(f"Otrzymano pakiet! Obecna długość wiadomości: {len(full_msg)}")

    if len(full_msg) == msglen:
        # Zdekoduj znaki z utf-8
        full_msg = full_msg.decode("utf-8")
        print(f"Otrzymano pełną wiadomość: {full_msg}")
        break

# Inicjalizacja dekodera
decoder = Decoder(full_msg)
