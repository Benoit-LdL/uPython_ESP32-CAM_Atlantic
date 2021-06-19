import camera
import uos
import machine
import utime
from config import app_config
import webserver

import time 
import servo

################__BASE APP__#################
#############################################
server = webserver.webcam()
server.run(app_config)

##################__VARS__###################
#############################################
debugCounter = 0
prevCarOption = ""
carOption = ""

servoDict = {
    "motorR":0,
    "motorL":1,
    "doorR":2,
    "doorL":3,
    "bonnetR":4,
    "bonnetL":5,
    "trunk":6,
    "steering":7,
    "steering2":8,
    "lightR":9,
    "lightL":10,
    "lightF":11,
    "lightB":12,
    "X":13,
    "XX":14,
    "XXX":15
}


i2c = machine.SoftI2C(scl=machine.Pin(14),sda=machine.Pin(15))
servos = servo.Servos(i2c)
###########__METHODS & FUNCTIONS__###########
#############################################
def CheckCarOptions():
    global carOption
    global prevCarOption

    #Check if carOption variable has changed on webserver. If so, execute what's necessary
    ## create extra counter in webserver counting every get request, only execute here when this value increases
    ## ---------> makes it possible to push 2 times on bonnet to open and close
    carOption = webserver.carOption
    if carOption != prevCarOption: 
        print(carOption)
        prevCarOption = carOption

        #Big IF statement for all possible car options
        if carOption == "stop":
            for x in range(0,16):
                servos.position(x,0)
        elif carOption == "forward":
            servos.position(servoDict["motorR"],100)
            servos.position(servoDict["motorL"],-100)
        elif carOption == "backward":
            servos.position(servoDict["motorR"],-100)
            servos.position(servoDict["motorL"],100)
        elif carOption == "Left":
            servos.position(servoDict["steering"],-100)
        elif carOption == "Right":
            servos.position(servoDict["steering"],100)
        elif carOption == "bonnetL":
            servos.position(servoDict["bonnetL"],100)
        elif carOption == "bonnetR":
            servos.position(servoDict["bonnetR"],100)
        elif carOption == "doorL":
            servos.position(servoDict["doorL"],100)
        elif carOption == "doorR":
            servos.position(servoDict["doorR"],100)
        elif carOption == "lights":
            servos.position(servoDict["lightF"],100)
            servos.position(servoDict["lightB"],100)
        elif carOption == "turnL":
            servos.position(servoDict["lightL"],100)
        elif carOption == "turnR":
            servos.position(servoDict["lightR"],100)



    
#############################################


# print(uos.uname())

# print('Scan i2c bus...')
# devices = i2c.scan()

# #Check I2C devices
# while len(devices) == 0:
#  print("No i2c device !")
#  utime.sleep(1)
#  devices = i2c.scan()

# print('i2c devices found:',len(devices))
# for device in devices:  
#   print("Decimal address: ",device," | Hexa address: ",hex(device))



while True:
    CheckCarOptions()
    # for x in range(0,16):
    #     servos.position(x,30)
    #     utime.sleep(0.1)

    # for x in range(0,16):
    #     servos.position(x,80)
    #     utime.sleep(0.1)
    utime.sleep(1)