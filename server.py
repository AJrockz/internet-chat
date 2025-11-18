import os
import socket
import threading

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 10000))

clients = []

def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            # broadcast
            for c in clients:
                if c != conn:
                    c.send(f"{addr[0]}: {msg}".encode())

        except:
            break

    print(f"[DISCONNECTED] {addr}")
    clients.remove(conn)
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    print(f"[SERVER RUNNING] PORT {PORT}")

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
