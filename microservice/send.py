import socket


def microservice(json_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 5000))
        message = json_data
        s.sendall(bytes(message.encode()))
        data = s.recv(1024)
        data = data.decode()
        return data
