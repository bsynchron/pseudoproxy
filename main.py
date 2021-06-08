#!/bin/python3
import socket, requests

proxies={"http":"http://109.193.195.7:8080",
         "http":"http://104.248.39.42:8080"}

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
    request=client_sock.recv(2048).decode()
    print(request)
    request_arr = request.split(" ")
    print("bitmex.com"+request_arr[1])
    r = requests.get('https://api.my-ip.io'+request_arr[1],proxies=proxies)
    print(r.text)
    response_body_raw=r.text
    response_headers_raw = f"'Content-Type': 'text/html; encoding=utf8'\n'Content-Length': {len(response_body_raw)}\n'Connection': 'close'"
    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'

    client_sock.send(f"{response_proto} {response_status} {response_status_text}\n{response_headers_raw}\n\n{response_body_raw}".encode())
    client_sock.close()
