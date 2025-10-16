import socket
from threading import Thread, Lock

class ServerSocket:
    def __init__(self, host, port):
        self.host: str = host
        self.port: int = port
        self.clients: list = []
        self.number_player = 0
        self.server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.init_server(self.host, self.port)
        self.main_loop()

    def init_server(self, host: str, port: int):
        self.server.bind((host, int(port)))
        self.server.listen(255)

    def main_loop(self):
        while True:
            conn, addr = self.server.accept()
            player_id = len(self.clients)
            self.clients.append(conn)
            thread = Thread(target=handle_client, args=(conn, addr, player_id))
            thread.start()

    def broadcast(msg: str):
        for c in clients:
            try:
                c.send(message.encode())
            except:
                pass     

    def handle_client(self, conn, addr, player_id):
        print(f"Client connected {addr}")
        while True:
            #with game_front.can_play(player_id):
                #if current_turn != player_id:
                    #continue
            try:
                data = conn.recv(1024).decode().strip()
                if not(data):
                    break
                print(data)
            except:
                break
        conn.close()
