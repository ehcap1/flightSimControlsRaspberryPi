# telnet program example
import socket, select, string, sys, time, random

#main function
if __name__ == "__main__":

    host = input("type host name: ")
    port = input("which port would you like to use? ")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try :
        s.connect((host, port))
        print ('Connected to remote host')
    except :
        print ('Unable to connect')
        sys.exit()



    msg = 'sub sim/flightmodel/controls/flaprqst\n'
    s.send(msg)
    time.sleep(0.5)


    while 1:

        socket_list = [s]
        # socket_list = [sys.stdin,s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])#, 1)

        for sock in read_sockets:
            if sock == s:
                    data = sock.recv(4096)
                    sys.stdout.write(data)

        time.sleep(0.5)
        msg = 'set sim/flightmodel/controls/flaprqst '+str(random.random())+'\n'
        s.send(msg)


