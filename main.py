# import RPi.GPIO as GPIO
from Adafruit_GPIO.MCP230xx import *
import socket, select, string, sys, time, random, smbus

#-------BUTON ASSIGNMENT--------
engineKey0 = 0
engineKey1 = 1
engineKey2 = 2
engineKey3 = 3
engineKey4 = 4

switch1 = 5
switch2 = 6
switch3 = 7
switch4 = 8
switch5 = 9
switch6 = 10
switch7 = 11
switchlist = [switch1, switch2, switch3, switch4, switch5, switch6, switch7 ]
mcp = MCP23017_x20()
mcp2 = MCP23017_x21()


messages = ["sub sim/flightmodel/controls/flaprqst\n", "sub sim/cockpit2/switches/beacon_on\n", "sub sim/cockpit/engine/fuel_pump_on 1\n", "sub sim/cockpit2/engine/actuators/ignition_key 1\n", "sub sim/cockpit2/switches/landing_lights_on\n" , "sub sim/cockpit2/switches/taxi_light_on\n", "sub sim/cockpit2/switches/navigation_lights_on\n", "sub sim/cockpit2/switches/strobe_lights_on \n","sub sim/cockpit2/ice/ice_pitot_heat_on_pilot\n"]

if __name__ == "__main__":
    #----need to set pins to items here--------
    mcp = MCP23017_x21()
    mcp.setup(0, GPIO.IN)
    mcp.setup(1, GPIO.IN)
    mcp.setup(2, GPIO.IN)
    mcp.setup(3, GPIO.IN)
    mcp.setup(4, GPIO.IN)
    mcp.setup(5, GPIO.IN)
    mcp.setup(6, GPIO.IN)
    mcp.setup(7, GPIO.IN)
    mcp.setup(8, GPIO.IN)
    mcp.setup(9, GPIO.IN)
    mcp.setup(10, GPIO.IN)
    mcp.setup(11, GPIO.IN)
    mcp.pullup(11, 1)
    mcp.pullup(10, 1)
    mcp.pullup(9, 1)
    mcp.pullup(8, 1)
    mcp.pullup(7, 1)
    mcp.pullup(6, 1)
    mcp.pullup(5, 1)
    mcp.pullup(4, 1)
    mcp.pullup(3, 1)
    mcp.pullup(2, 1)
    mcp.pullup(1, 1)
    mcp.pullup(0, 1)




    host = "192.168.0.102" #input("type host name: ")
    port = 51000   #int(input("which port would you like to use? "))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # sockect to remote host
    try :
        s.connect((host, port))
        print ('connected to remote host')

    except :
        print ('Unable to connect')
        sys.exit()

    for msg in messages:
     #python 3 str.encode('')
        s.send(str.encode(msg)) #bytes(msg, 'utf-8'))
        time.sleep(0.5)

    def engineKey():
        if not mcp.input(engineKey3):
            msg = ("set sim/cockpit2/engine/actuators/ignition_key [3,0,0,0,0,0,0,0] \n")
            s.send(str.encode(msg))


        elif not mcp.input(engineKey4):
            while not mcp.input(engineKey4):
                msg = ("set sim/cockpit2/engine/actuators/ignition_key [4,0,0,0,0,0,0,0]\n")
                s.send(str.encode(msg))


        elif not mcp.input(engineKey2):
            msg = ("set sim/cockpit2/engine/actuators/ignition_key [2,0,0,0,0,0,0,0]\n")
            s.send(str.encode(msg))


        elif not mcp.input(engineKey1):

            msg = ("set sim/cockpit2/engine/actuators/ignition_key [1,0,0,0,0,0,0,0]\n")
            s.send(str.encode(msg))


        elif not mcp.input(engineKey0):
            msg = ("set sim/cockpit2/engine/actuators/ignition_key [0]\n")
            s.send(str.encode(msg))


        else:
            pass

    def funcswitch1():#fuel pump
        # mcp.setup(5, GPIO.IN)


        if mcp.input(switch1):
            msg = ("set sim/cockpit/engine/fuel_pump_on [1,0,0,0,0,0,0,0]\n")
            s.send(str.encode(msg))

        else:
            msg = ("set sim/cockpit/engine/fuel_pump_on [0,0,0,0,0,0,0,0]\n")
            s.send(str.encode(msg))


    def funcswitch2():#BCN
        if mcp.input(switch2):
            # Check whether the switch is on or not.
            msg = ('set sim/cockpit2/switches/beacon_on 1\n')
            s.send(str.encode(msg))

        else:
            msg = ('set sim/cockpit2/switches/beacon_on 0\n')
            s.send(str.encode(msg))


    def funcswitch3():#lAND
        if mcp.input(switch3):
            # Check whether the switch is on or not.
            msg = ('set sim/cockpit2/switches/landing_lights_on 1\n')
            s.send(str.encode(msg))

        else:
            msg = ('set sim/cockpit2/switches/landing_lights_on 0\n')
            s.send(str.encode(msg))


    def funcswitch4():#TAXI
        if mcp.input(switch4):
            # Check whether the switch is on or not.
            msg = ('set sim/cockpit2/switches/taxi_light_on 1\n')
            s.send(str.encode(msg))

        else:
            msg = ('set sim/cockpit2/switches/taxi_light_on 0\n')
            s.send(str.encode(msg))


    def funcswitch5():#Nav
        if mcp.input(switch5):
            # Check whether the switch is on or not.
            msg = ('set sim/cockpit2/switches/navigation_lights_on 1\n')
            s.send(str.encode(msg))


        else:
            msg = ('set sim/cockpit2/switches/navigation_lights_on 0\n')
            s.send(str.encode(msg))


    def funcswitch6():#STROBE
        if mcp.input(switch6):
            # Check whether the switch is on or not.
            msg = ('set sim/cockpit2/switches/strobe_lights_on 1\n')
            s.send(str.encode(msg))

        else:
            msg = ('set sim/cockpit2/switches/strobe_lights_on 0\n')
            s.send(str.encode(msg))


    def funcswitch7():#pitoHeat
        # mcp.setup(11, GPIO.IN)
        if mcp.input(switch7):
            # Check whether the switch is on or not.
            msg = ('set sim/cockpit2/ice/ice_pitot_heat_on_pilot 1\n')
            s.send(str.encode(msg))

        else:
            msg = ('set sim/cockpit2/ice/ice_pitot_heat_on_pilot 0\n')
            s.send(str.encode(msg))






    btnlist = [funcswitch1, funcswitch2, funcswitch3, funcswitch4, funcswitch5, funcswitch6, funcswitch7, engineKey]

    while 1:

        socket_list = [s]

        # socket_list = [sys.stdin,s]
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [], 1)

        # for sock in read_sockets:
        #     if sock == s:
        #         data = sock.recv(4096)
        #         reply = data.decode('utf-8')
        #         print (reply)
        #         # sys.stdout.write(str(data))

        for func in btnlist:
            func()
            # time.sleep(.5)
