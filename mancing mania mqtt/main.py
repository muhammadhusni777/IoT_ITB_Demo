######  PROGRAM MEMANGGIL WINDOWS PYQT5 ##########################

####### memanggil library PyQt5 ##################################
#----------------------------------------------------------------#
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtQml import * 
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import *  
import sys
import threading

import paho.mqtt.client as paho

broker="127.0.0.1"
#broker="mqtt.ardumeka.com"#"broker.emqx.io"
#port = 11219
port = 1883
topic_test = ""

import pygame
import random
pygame.init()
#----------------------------------------------------------------#

analog1_x = 0
analog1_y = 0
analog1_x_prev = 0
analog1_y_prev = 0

analog2_x = 0
analog2_y = 0
analog2_x_prev = 0
analog2_y_prev = 0

hat = ""
hat_prev = ""


up_color = "#122e55"
left_color = "#122e55"
right_color = "#122e55"
down_color = "#122e55"

button1_color = "#122e55"
button2_color = "#122e55"
button3_color = "#122e55"
button4_color = "#122e55"

button_L1_color = "#122e55"
button_L2_color = "#122e55"
button_R1_color = "#122e55"
button_R2_color = "#122e55"

analog1_color = "#122e55"
analog2_color = "#122e55"

ship_pos = 0
ship_speed = 0

import random
fish1_x = 400
fish1_y = 100
fish1_x_dir = 0
fish1_y_dir = 0

rope_status = 0
rope_status_prev = 0
rope_length = 10

current_score = 0
score = 0
strike_status = 0
strike_status_prev = 0

########## mengisi class table dengan instruksi pyqt5#############
#----------------------------------------------------------------#
class table(QObject):    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.app = QApplication(sys.argv)
        self.engine = QQmlApplicationEngine(self)
        self.engine.rootContext().setContextProperty("backend", self)    
        self.engine.load(QUrl("main.qml"))
        sys.exit(self.app.exec_())
        
        
    @pyqtSlot(result=str)
    def up_color(self):  return (up_color)
    
    
    @pyqtSlot(result=str)
    def left_color(self):  return (left_color)
    
    @pyqtSlot(result=str)
    def right_color(self):  return (right_color)
    
    @pyqtSlot(result=str)
    def down_color(self):  return (down_color)
    
    @pyqtSlot(result=str)
    def button1_color(self):  return (button1_color)
    
    @pyqtSlot(result=str)
    def button2_color(self):  return (button2_color)
    
    @pyqtSlot(result=str)
    def button3_color(self):  return (button3_color)
    
    @pyqtSlot(result=str)
    def button4_color(self):  return (button4_color)

    @pyqtSlot(result=str)
    def button_L1_color(self):  return (button_L1_color)

    @pyqtSlot(result=str)
    def button_L2_color(self):  return (button_L2_color)
    
    @pyqtSlot(result=str)
    def button_R1_color(self):  return (button_R1_color)

    @pyqtSlot(result=str)
    def button_R2_color(self):  return (button_R2_color)
    
    @pyqtSlot(result=float)
    def analog1_x(self):  return float(analog1_x * 10)
    
    @pyqtSlot(result=float)
    def analog1_y(self):  return float(analog1_y * 10)
    
    @pyqtSlot(result=float)
    def analog2_x(self):  return float(analog2_x*10)
    
    @pyqtSlot(result=float)
    def analog2_y(self):  return float(analog2_y*10)
    
    @pyqtSlot(result=str)
    def analog1_color(self):  return analog1_color
    
    @pyqtSlot(result=str)
    def analog2_color(self):  return analog2_color
    
    @pyqtSlot(result=int)
    def ship_pos(self):  return ship_pos
    
    
    @pyqtSlot(result=int)
    def fish1_x(self):  return int(fish1_x)
    
    @pyqtSlot(result=int)
    def fish1_y(self):  return int(fish1_y)
    
    @pyqtSlot(result=int)
    def rope_length(self):  return int(rope_length)
    
    @pyqtSlot(result=str)
    def current_score(self):  return str(current_score)
    
    
    

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    t = str(message.topic)

    if(msg[0] == 'c'):
        val =  1
    else:
        val = (msg)
    
    if (t == "sensor"):
        global topic_test
        topic_test = (msg)
        print(topic_test)
        



#----------------------------------------------------------------#

def pygame_run(num):
    global analog1_x
    global analog1_y
    global analog1_x_prev
    global analog1_y_prev

    global analog2_x
    global analog2_y
    global analog2_x_prev
    global analog2_y_prev
    
    global hat
    global hat_prev
    
    global up_color
    global down_color
    global left_color
    global right_color
    
    global button1_color
    global button2_color
    global button3_color
    global button4_color
    
    
    global button_L1_color
    global button_L2_color
    global button_R1_color
    global button_R2_color
    
    global analog1_color
    global analog2_color
    global ship_pos
    global ship_speed
    
    global fish1_x
    global fish1_x_dir
    
    global fish1_y
    global fish1_y_dir
    global rope_status
    global rope_length
    global rope_status_prev
    global current_score
    global score
    global strike_status
    global strike_status_prev
    
    clock = pygame.time.Clock()
    joysticks = {}
    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                #print("Joystick button pressed.")
                status_button = "pressed"
                joy_button_status = status_button
                joy_button_event = event.button
                #print(joy_button_status)
                print(joy_button_event)
                if (joy_button_event == 0):
                    button1_color = "#d84860"
                    
                if (joy_button_event == 1):
                    button2_color = "#d84860"
                    
                if (joy_button_event == 2):
                    button3_color = "#d84860"
                    
                if (joy_button_event == 3):
                    button4_color = "#d84860"
                    rope_status = 1
                    
                    
                if (joy_button_event == 4):
                    button_L1_color = "#d84860"
                    
                if (joy_button_event == 5):
                    button_R1_color = "#d84860"
                    
                if (joy_button_event == 6):
                    button_L2_color = "#d84860"
                
                if (joy_button_event == 7):
                    button_R2_color = "#d84860"
                    
                if (joy_button_event == 10):
                    analog1_color = "#d84860"
                    
                if (joy_button_event == 11):
                    analog2_color = "#d84860"
                
                if event.button == 0:
                    
                    joystick = joysticks[event.instance_id]
                    
                
                
           
            if event.type == pygame.JOYBUTTONUP:
                #print("Joystick button released.")
                joy_button_status = status_button
                joy_button_event = event.button
                
                if (joy_button_event == 0):
                    button1_color = "#122e55"
                    
                if (joy_button_event == 1):
                    button2_color = "#122e55"
                    
                if (joy_button_event == 2):
                    button3_color = "#122e55"
                    
                if (joy_button_event == 3):
                    button4_color = "#122e55"
                    rope_status = 0
                    
                    
                if (joy_button_event == 4):
                    button_L1_color = "#122e55"
                    
                if (joy_button_event == 5):
                    button_R1_color = "#122e55"
                    
                if (joy_button_event == 6):
                    button_L2_color = "#122e55"
                
                if (joy_button_event == 7):
                    button_R2_color = "#122e55"
                    
                if (joy_button_event == 10):
                    analog1_color = "#122e55"
                    
                if (joy_button_event == 11):
                    analog2_color = "#122e55"

                
                
                
            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print("Joystick {} connected".format(joy.get_instance_id()))
                

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print("Joystick {} disconnected".format(event.instance_id))

       
            
        # For each joystick:
        for joystick in joysticks.values():
                
            jid = joystick.get_instance_id()
            name = joystick.get_name()
            guid = joystick.get_guid()
            power_level = joystick.get_power_level()
            axes = joystick.get_numaxes()
            

            for i in range(axes):
                axis = joystick.get_axis(i)
                if i == 0 :
                    analog1_x = axis
                if i == 1 :
                    analog1_y = axis
                if i == 2 :
                    analog2_y = axis
                if i == 3 :
                    analog2_x = axis
                    #print(axis)
                
                a =+ 1
            
            
            
            buttons = joystick.get_numbuttons()
            

            for i in range(buttons):
                button = joystick.get_button(i)
                
            hats = joystick.get_numhats()
            
            
            
            for i in range(hats):
                hat = joystick.get_hat(i)
            
        if (hat != hat_prev):    
            print(hat)
            if (hat[0] == -1 and strike_status == 0):
                left_color = "#d84860"
                right_color = "#122e55"
                ship_speed = -5
                
                print(ship_pos)
                
            if (hat[0] == 0):
                left_color = "#122e55"
                right_color = "#122e55"
                ship_speed = 0
                
            if (hat[0] == 1 and strike_status == 0):
                left_color = "#122e55"
                right_color = "#d84860"
                ship_speed = 5
                print(ship_pos)
                
                
            if (hat[1] == -1):
                down_color = "#d84860"
                up_color = "#122e55"
                
            if (hat[1] == 0):
                down_color = "#122e55"
                up_color = "#122e55"
                
            if (hat[1] == 1):
                down_color = "#122e55"
                up_color = "#d84860"
                
                
        hat_prev = hat
        
        if (analog1_x != (analog1_x_prev) ):
            print(analog1_x)
            
        if (analog1_y != (analog1_y_prev) ):
            print(analog1_y)
            
        if (analog2_x != (analog2_x_prev) ):
            print(analog2_x)
            
        if (analog2_y != (analog2_y_prev) ):
            print(analog2_y)
        
        
             
        analog1_x_prev = analog1_x
        analog1_y_prev = analog1_y
        analog2_x_prev = analog2_x
        analog2_y_prev = analog2_y
        
        
        fish1_x = (fish1_x) + int(fish1_x_dir)
        fish1_y = (fish1_y) + int(fish1_y_dir)
        
        
        ship_pos = ship_pos+ship_speed
        
        
        if (rope_status == 1 and strike_status == 0):
            rope_length = rope_length + 10
            
        if (rope_status == 0 or strike_status == 1):
            rope_length = rope_length - 10
            if (rope_length < 10):
                rope_length = 10
                strike_status = 0
                
        if (strike_status == 0):
            
            fish1_x_dir = random.randint(-5,5)
            fish1_y_dir = random.randint(-5,5)
            fish1_x = (fish1_x) + int(fish1_x_dir)
            fish1_y = (fish1_y) + int(fish1_y_dir)
            
            if(fish1_x < 0):
                fish1_x = 0
            if(fish1_x > 400):
                fish1_x = 400
                
            if(fish1_y < 0):
                fish1_y = 0
                
            if(fish1_y > 300):
                fish1_y = 300
            
        
        if (strike_status == 1):
            
            fish1_x_dir = 0
            fish1_y_dir = 0
            fish1_y = fish1_y - 10
        
        if(rope_status !=rope_status_prev):
            if (rope_status == 0):
                print((rope_length - fish1_y), (ship_pos-fish1_x))
                if (150 < abs(rope_length - fish1_y) and (190 > abs(rope_length - fish1_y)) and(122 < abs(ship_pos - fish1_x) and(155 > abs(ship_pos - fish1_x)))):
                    score = 1
                    strike_status = 1
                    if(score < 0):
                        score = 0
                    current_score = current_score + score
        
        
        if (strike_status != strike_status_prev):
            
            if (strike_status == 1):
                client.publish("IoTDevice2024/lamp", "ON")
                
            if (strike_status == 0):
                client.publish("IoTDevice2024/lamp", "OFF")
        
        if (strike_status != strike_status_prev and strike_status == 0):
            
            
            fish1_x = random.randint(100,300)
            fish1_y = random.randint(100,300)
            
            
            
        rope_status_prev = rope_status
        strike_status_prev = strike_status
        clock.tick(30)




########## memanggil class table di mainloop######################
#----------------------------------------------------------------#    
if __name__ == "__main__":
    
    client= paho.Client("PC_1")
    client.on_message=on_message

    print("connecting to broker ",broker)
    client.connect(broker,port)#connect
    print(broker," connected")
    
    client.loop_start()
    print("Subscribing")

    client.subscribe("sensor")
    
    t1 = threading.Thread(target=pygame_run, args=(10,))
    t1.start()
    main = table()
    
    
#----------------------------------------------------------------#