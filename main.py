import socket
import sys

UDP_IP = '0.0.0.0'


def get_port():
    if len(sys.argv) <= 1:
        return None
    port_udp = sys.argv[1]
    if port_udp.isnumeric():
        return port_udp
    return None


def get_proxy_ip():
    if len(sys.argv) <= 2:
        return None
    return sys.argv[2]


def get_proxy_port():
    if len(sys.argv) <= 3:
        return None
    port_udp = sys.argv[3]
    if port_udp.isnumeric():
        return port_udp
    return None


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    port_udp = get_port()
    if not port_udp:
        raise ValueError('Need set UDP PORT')
    sock.bind((UDP_IP, int(port_udp)))
    print(f'Listen IP:{UDP_IP},PORT:{port_udp}')
    sock_proxy = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        data_hex = data.hex()
        print(f'address={addr}')
        print("received message: %s" % data)
        proxy_ip = get_proxy_ip()
        proxy_port = get_proxy_port()
        if proxy_ip and proxy_port:
            print(f'Send proxy {proxy_ip}:{proxy_port}')
            sock_proxy.sendto(data, (proxy_ip, int(proxy_port)))
        else:
            print('Not set proxy')
