# telnet program example
import RPi.GPIO as GPIO
import socket, select, string, sys, time, random
import flightfunctions


Btn1Pin = 11    # pin11 fuel pump off or on
Btn2Pin = 12    # pin12 bcn on or off

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Btn1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Set LedPin's mode is input
    GPIO.setup(Btn2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)

#subscribing to flaps, beacon, and fuel pump 1
messages = ["sub sim/flightmodel/controls/flaprqst\n", "sub sim/cockpit2/switches/beacon_on\n", "sub sim/cockpit/engine/fuel_pump_on 1\n"]

#main function
if __name__ == "__main__":
    setup()
    host = "192.168.0.102" #input("type host name: ")
    port = 51000   #int(input("which port would you like to use? "))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try :
        s.connect((host, port))
        print ('Connected to remote host')
    except :
        print ('Unable to connect')
        sys.exit()



    for msg in messages:
     #python 3 str.encode('')
        s.send(msg) #bytes(msg, 'utf-8'))
        time.sleep(0.5)
    def btn1():
        if (GPIO.input(Btn1Pin) == GPIO.HIGH):
            msg = ("set sim/cockpit/engine/fuel_pump_on [1,2,0,0,0,0,0,0]\n")
            s.send(msg)
        else:
            msg = ("set sim/cockpit/engine/fuel_pump_on [0,2,0,0,0,0,0,0]\n")
            s.send(msg)
    def btn2():
        if (GPIO.input(Btn2Pin) == GPIO.HIGH) :
                # Check whether the button is pressed or not.
                msg = ('set sim/cockpit2/switches/beacon_on 1\n')
                s.send(msg)
        else:
            msg = ('set sim/cockpit2/switches/beacon_on 0\n')
            s.send(msg)
    btnlist = [btn2,btn1]
    while 1:

        socket_list = [s]

        # socket_list = [sys.stdin,s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [], 1)

        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)

                sys.stdout.write(str(data))
        for func in btnlist:
            func()


        # if (GPIO.input(Btn1Pin) == GPIO.HIGH):
        #     msg = ("set sim/cockpit/engine/fuel_pump_on [1,2,0,0,0,0,0,0]\n")
        #     s.send(msg)




        # else:
        #     msg = ("set sim/cockpit/engine/fuel_pump_on [0,2,0,0,0,0,0,0]\n")
        #     s.send(msg)
        # for func in btnlist:
        #     func()


        # if (GPIO.input(Btn2Pin) == GPIO.HIGH) :
        #     # Check whether the button is pressed or not.

        #     msg = ('set sim/cockpit2/switches/beacon_on 1\n')

        #     s.send(msg)


        # else:
        #     msg = ('set sim/cockpit2/switches/beacon_on 0\n')
        #     s.send(msg)










           #msg = "set sim/flightmodel/controls/flaprqst 0\n"
            #s.send(msg)


        #time.sleep(0.5)
        # msg = 'set sim/flightmodel/controls/flaprqst '+str(random.random())+'\n'
        # s.send(msg)

