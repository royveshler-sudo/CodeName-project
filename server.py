__author__ = "ROY"

import socket
import threading

def handle_client(sock, tid, addr):
    global all_to_die
    finish = False
    print(f'New Client number {tid} from {addr}')

    while not finish:
        if all_to_die:
            break

def main():
    global all_to_die
    threads = []
    srv_sock = socket.socket()
    srv_sock.bind(('0.0.0.0', 1279))
    srv_sock.listen(20)
    srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    i = 1
    while True:
        print('\nMain thread: before accepting ...')
        cli_sock, addr = srv_sock.accept()
        t = threading.Thread(target=handle_client, args=(cli_sock, str(i), addr))
        t.start()
        i += 1
        threads.append(t)
        if i > 100000000:
            break

    all_to_die = True
    for t in threads:
        t.join()
    srv_sock.close()

