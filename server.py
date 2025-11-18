import socket
import threading

clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            for client in clients:
                if client != conn:
                    client.send(f"{addr}: {msg}".encode())

        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"[DISCONNECTED] {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen()

    print("[SERVER STARTED] Listening on port 5000")

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start_server()
