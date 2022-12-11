import socket
import sys

UDP_IP = '0.0.0.0'
PROXY_IP = '192.168.0.29'


def get_port():
    if len(sys.argv) <= 1:
        return None
    port_udp = sys.argv[1]
    if port_udp.isnumeric():
        return port_udp
    return None


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    port_udp = get_port()
    if port_udp:
        raise ValueError('Need set UDP PORT')
    sock.bind((UDP_IP, int(port_udp)))
    print(f'Listen IP:{UDP_IP},PORT:{port_udp}')
    sock_proxy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_hex = data.hex()
        print(f'address={addr}')
        print(f'data_hex={data_hex}')
        print("received message: %s" % data)
        sock_proxy.sendto(data, (PROXY_IP, port_udp))
