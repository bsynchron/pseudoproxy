#!/bin/python3
import socket

serv_sock = socket.socket(
    socket.AF_INET,      # set protocol family to 'Internet' (INET)
    socket.SOCK_STREAM,  # set socket type to 'stream' (i.e. TCP)
    proto=0              # set the default protocol (for TCP it's IP)
)

serv_sock.bind(('127.0.0.1', 6543))
while True:
    serv_sock.listen(10)
    client_sock, client_addr = serv_sock.accept()
    print(client_addr)
    response_body_raw=f"<html><body>\n<span>no</span>\n</body></html>"
    response_headers_raw = f"'Content-Type': 'text/html; encoding=utf8'\n'Content-Length': {len(response_body_raw)}\n'Connection': 'close'"
    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'

    client_sock.send(f"{response_proto} {response_status} {response_status_text}\n{response_headers_raw}\n\n{response_body_raw}".encode())

proxies=[]
print("hi")
