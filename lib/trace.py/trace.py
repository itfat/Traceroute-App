from flask import Flask
import socket
import random
import struct
import time
import sys

from flask.globals import request

result_final = {}
result = []

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.values.get("trace"))
        trace(request.values.get("trace"), 30)
        result_final.clear() #not working
        for i in range (0,len(result)):
            print(result[i])
            result_final[i] = result[i]
        print("result final is+++++++++++++++++++++++++++++++++++++++++", result_final)
        return result_final


def trace(destination, hops):
    # type: (str, int) -> None
    """
    Function that does the work previous to the tracert, such as choosing a port,
        finding the destination_ip and printing basic info about the command it
        was given.
    It also calls the function that does the tracert.
    :param destination: destination selected
    :param hops: max number of hops
    :return: None
    """
    result_final = {}
    port = random.choice(range(33434, 33535))

    try:
        # get the ip of the input destination
        destination_ip = socket.gethostbyname(destination)
    except socket.error as e:
        print('Unable to find ' + str(destination) + ': ' + str(e))
        result.append('Unable to find ' + str(destination) + ': ' + str(e))
        
        return

    # print the traceroute command details
    print('traceroute to ' + str(destination) + ' ( ' + str(destination_ip) + ' ), ' + str(hops) + ' hops max\n')
    result.append('traceroute to ' + str(destination) + ' ( ' + str(destination_ip) + ' ), ' + str(hops) + ' hops max')

    # print the header
    print_formatted('Hop', 'Address', 'Host Name', 'Time', True)
    # result.append('Hop', 'Address', 'Host Name', 'Time', True)

    # call the tracert
    aux_trace(destination, destination_ip, port, hops, 1)


def aux_trace(destination, destination_ip, port, hops, ttl):
    # type: (str, str, int, int, int) -> None
    """
    Recursive function that does the tracert
    :param destination: destination input by user
    :param destination_ip: ip of param destination
    :param port: port randomly chosen in trace
    :param hops: max number of hops
    :param ttl: count of hops that already happened
    :return: None
    """
    # create sockets
    receiver = create_receiver(port)
    sender = create_sender(ttl)

    # send data to socket
    sender.sendto(b'', (destination, port))

    # starting time
    start = time.time()

    address = None
    try:
        # receive data and address of the socket that sent the data
        data, address = receiver.recvfrom(1024)
    except socket.error:
        pass

    # ending time
    end = time.time()
    # calculate the response time
    response_time = round((end - start) * 1000, 2)

    if address:  # if recvfrom was successful
        addr = address[0]

        try:  # if possible it will get the host name
            host = socket.gethostbyaddr(addr)[0]
        except socket.error:  # otherwise it will just assume the host name is the ip itself
            host = addr

        print_formatted(ttl, addr, host, str(response_time) + 'ms', False)

        if address[0] == destination_ip:  # if it reached the desired destination
            print('\nreached destination\n')
            result.append('Reached destination')

            return

    else:  # if recvfrom was unsuccessful
        print_formatted(ttl, '*'*10, '*'*10, str(response_time) + 'ms', False)

    if ttl > hops:  # if it reached max number of hops
        print('\nreached max number of hops\n')
        result.append('Reached max number of hops')
        return

    # recursive call
    aux_trace(destination, destination_ip, port, hops, ttl + 1)


def print_formatted(ttl, addr, host, resp_time, header):
    if header:
        print('|{:<5}+{:<20}+{:<45}+{:<10}|'.format('-'*5, '-'*20, '-'*45, '-'*10))
        # result.append('{:<5} {:<20} {:<45} {:<10}'.format('-'*5, '-'*20, '-'*45, '-'*10))

    print(' {:<5} {:<20} {:<45} {:<10} '.format(ttl, addr, host, resp_time))
    result.append('{:<3} {:<15} {:<35} {:<10}'.format(ttl, addr, host, resp_time))
    
    print('|{:<5}+{:<20}+{:<45}+{:<10}|'.format('-'*5, '-'*20, '-'*45, '-'*10))
    # result.append('|{:<5}+{:<20}+{:<45}+{:<10}|'.format('-'*5, '-'*20, '-'*45, '-'*10))


def create_receiver(port):
    """
    creating receiver socket
    """
    s = socket.socket(
        family=socket.AF_INET,  # indicates the address family used(ipv4)
        type=socket.SOCK_RAW,  # bypass OS TCP/IP
        proto=socket.IPPROTO_ICMP  # Internet Control Message Protocol
                                   # Used to send error messages and operational information
    )

    # how long it will wait until stops trying
    timeout = struct.pack('ll', 5, 0)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)
    # params(family, type, timeout)
    # SOL_SOCKET: Sets the socket protocol level
    # SO_RCVTIMEO: Specify the receiving or sending timeouts until reporting an error.

    try:
        s.bind(('', port))
    except socket.error as e:
        raise IOError('Unable to bind receiver socket: {}'.format(e))

    return s


def create_sender(ttl):
    """
    creating sender socket
    """
    s = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_DGRAM,  # Sets UDP protocol instead of TCP(SOCK_STREAM)
        proto=socket.IPPROTO_UDP  # Sets UDP protocol instead of TCP
    )

    # Changes the default value set by TCP/IP in TTL field of the IP header
    s.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

    return s





if __name__ == "__main__":
    app.run(host='192.168.100.9', port=7001,debug =True)
