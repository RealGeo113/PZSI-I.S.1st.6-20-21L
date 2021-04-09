from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

###   ###
# 29:19 #
###   ###

# STALE GLOBALNE
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 512

# ZMIENNE GLOBALNE
persons = []

def broadcast(msg, name):
    """
    Wysyłaj nowe wiadomości do wszystkich klientów.
    :param msg: bytes["utf8"]
    :param name: str
    :return:
    """
    for person in persons:
        client = person.client
        client.send(bytes(name + ": ", "utf8") + msg)


# tworzy obiekty klientow
# przechowuje adres ip i nazwe
# dzieki temu bedziemy wiedziec kto z kim czatuje i kto wysyla wiadomosci
def client_communication(person):
    """
    Wątek przechwytujący wszystkie wiadomości od klienta.
    :param client: socket
    :return: None
    """
    client = person.client
    addr = person.addr

    # get persons name
    name = client.recv(BUFSIZ).decode("utf8")
    msg = f"{name} dołączył do pokoju!"
    broadcast(msg)

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            client.send(bytes("{quit}", "utf8"))
            client.close()

            persons.remove(person)
        else:
            client.send(msg)

def wait_for_connection():
    """
    Czekaj na połączenie od nowych klientów, utwórz nowy wątek po połączeniu.
    :param SERVER: SOCKET
    :return:
    """
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[CONNECTION] {addr} połączył się z serwerem. Czas: {time.time()}")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False

    print("[ERROR] Błąd serwera.")




SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS)
    print("[STARTED] Czekam na połączenie...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()