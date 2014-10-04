import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host Name : %s" % host_name
    print "IP Address : %s" % ip_address

def get_remote_machine_info(remote_host):
    try:
        print "Host : %s, IP Address : %s" %(remote_host,socket.gethostbyname(remote_host))
    except socket.error, err_msg:
        print "%s: %s" %(remote_host, err_msg)

if __name__ == '__main__':
    print_machine_info()
    get_remote_machine_info('www.google.com')
