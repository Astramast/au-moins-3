import socket
from threading import Thread, Lock

class ClientSocket:
    def __init__(self, serv_host: str, serv_port: int):
        self.serv_host: str = serv_host
        self.serv_port: int = serv_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.serv_port, int(self.serv_port)))
        self.main_loop()
    
    def main_loop(self):
        try:
            while True:
                msg = client.recv(1024).decode()
                if not message:
                    break
                print(msg)
                msg = input("Message to the server: ")
                client.send(msg.encode)
        except KeyboardInterrupt:
            print("Deconnexion.")
        finally:
            self.client.close()