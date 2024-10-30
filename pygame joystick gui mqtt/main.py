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
import time
import pygame
pygame.init()

import paho.mqtt.client as paho

broker="127.0.0.1"    #local broker
port =  1883
topic_test = ""
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


up_color = "#01ccf5"
left_color = "#01ccf5"
right_color = "#01ccf5"
down_color = "#01ccf5"


up_data = "off"
left_data = "off"
right_data = "off"
down_data = "off"

button1_color = "#01ccf5"
button2_color = "#01ccf5"
button3_color = "#01ccf5"
button4_color = "#01ccf5"

button1_data = "off"
button2_data = "off"
button3_data = "off"
button4_data = "off"

button_L1_color = "#01ccf5"
button_L2_color = "#01ccf5"
button_R1_color = "#01ccf5"
button_R2_color = "#01ccf5"

button_L1_data = "off"
button_L2_data = "off"
button_R1_data = "off"
button_R2_data = "off"

analog1_color = "#01ccf5"
analog2_color = "#01ccf5"
analog1_data = "off"
analog2_data = "off"

mqtt_time = 0.5
mqtt_time_now = time.time()
mqtt_time_prev = time.time()

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
    
    global up_data
    global down_data
    global left_data
    global right_data
    
    global button1_color
    global button2_color
    global button3_color
    global button4_color
    
    global button1_data
    global button2_data
    global button3_data
    global button4_data
    
    global button_L1_color
    global button_L2_color
    global button_R1_color
    global button_R2_color
    
    global button_L1_data
    global button_L2_data
    global button_R1_data
    global button_R2_data
    
    
    global up_data
    global down_data
    global left_data
    global right_data
    
    global analog1_color
    global analog2_color
    global analog1_data
    global analog2_data
    
    global mqtt_time
    global mqtt_time_now
    global mqtt_time_prev
    
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
                    button1_data = "on"
                    
                    
                if (joy_button_event == 1):
                    button2_color = "#d84860"
                    button2_data = "on"
                    
                if (joy_button_event == 2):
                    button3_color = "#d84860"
                    button3_data = "on"
                    
                if (joy_button_event == 3):
                    button4_color = "#d84860"
                    button4_data = "ON"
                    
                if (joy_button_event == 4):
                    button_L1_color = "#d84860"
                    button_L1_data = "on"
                    
                if (joy_button_event == 5):
                    button_R1_color = "#d84860"
                    button_R1_data = "on"
                    
                if (joy_button_event == 6):
                    button_L2_color = "#d84860"
                    button_L2_data = "on"
                
                if (joy_button_event == 7):
                    button_R2_color = "#d84860"
                    button_R2_data = "on"
                    
                if (joy_button_event == 10):
                    analog1_color = "#d84860"
                    analog1_data = "on"
                    
                if (joy_button_event == 11):
                    analog2_color = "#d84860"
                    analog2_data = "on"
                
                if event.button == 0:
                    
                    joystick = joysticks[event.instance_id]
                    
                
                
           
            if event.type == pygame.JOYBUTTONUP:
                #print("Joystick button released.")
                joy_button_status = status_button
                joy_button_event = event.button
                
                if (joy_button_event == 0):
                    button1_color = "#01ccf5"
                    button1_data = "off"
                    
                if (joy_button_event == 1):
                    button2_color = "#01ccf5"
                    button2_data = "off"
                    
                if (joy_button_event == 2):
                    button3_color = "#01ccf5"
                    button3_data = "off"
                    
                if (joy_button_event == 3):
                    button4_color = "#01ccf5"
                    button4_data = "OFF"
                    
                if (joy_button_event == 4):
                    button_L1_color = "#01ccf5"
                    button_L1_data = "off"
                    
                if (joy_button_event == 5):
                    button_R1_color = "#01ccf5"
                    button_R1_data = "off"
                    
                if (joy_button_event == 6):
                    button_L2_color = "#01ccf5"
                    button_L2_data = "off"
                
                if (joy_button_event == 7):
                    button_R2_color = "#01ccf5"
                    button_R2_data = "off"
                    
                if (joy_button_event == 10):
                    analog1_color = "#01ccf5"
                    analog1_data = "off"
                    
                if (joy_button_event == 11):
                    analog2_color = "#01ccf5"
                    analog2_data = "off"
                
                
                
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
            if (hat[0] == -1):
                left_color = "#d84860"
                right_color = "#01ccf5"
                left_data = "on"
                right_data = "off"
                
            if (hat[0] == 0):
                left_color = "#01ccf5"
                right_color = "#01ccf5"
                left_data = "off"
                right_data = "off"
                
            if (hat[0] == 1):
                left_color = "#01ccf5"
                right_color = "#d84860"
                left_data = "off"
                right_data = "on"
                
            if (hat[1] == -1):
                down_color = "#d84860"
                up_color = "#01ccf5"
                up_data = "off"
                down_data = "on"
                
            if (hat[1] == 0):
                down_color = "#01ccf5"
                up_color = "#01ccf5"
                up_data = "off"
                down_data = "off"
                
            if (hat[1] == 1):
                down_color = "#01ccf5"
                up_color = "#d84860"
                up_data = "on"
                down_data = "off"
                
                
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
        
        #KIRIM DATA VIA MQTT
        
        mqtt_time_now = time.time() - mqtt_time_prev
        
        if (mqtt_time_now > mqtt_time):
            #publish button
            client.publish("button1",str(button1_data))
            client.publish("button2",str(button2_data))
            client.publish("button3",str(button3_data))
            client.publish("IoTDevice2024/lamp",str(button4_data))
            client.publish("button_L1",str(button_L1_data))
            client.publish("button_R1",str(button_R1_data))
            client.publish("button_L2",str(button_L2_data))
            client.publish("button_R2",str(button_R2_data))
            client.publish("analog1_button",str(analog1_data))
            client.publish("analog2_button",str(analog2_data))
            
            #publish hat
            client.publish("up",str(up_data))
            client.publish("down",str(down_data))
            client.publish("left",str(left_data))
            client.publish("right",str(right_data))
            
            #publish axes
            client.publish("analog1_x",str(analog1_x))
            client.publish("analog2_x",str(analog2_x))
            client.publish("analog1_y",str(analog1_y))
            client.publish("analog2_y",str(analog2_y))
            
            mqtt_time_prev = time.time()
        
        
        clock.tick(30)


#----------------------------------------------------------------#   
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    t = str(message.topic)

    if(msg[0] == 'c'):
        val =  1
    else:
        val = (msg)


########## memanggil class table di mainloop######################
#----------------------------------------------------------------#    
if __name__ == "__main__":
    
    client= paho.Client("GUI")
    client.on_message=on_message

    print("connecting to broker ",broker)
    client.connect(broker,port)#connect
    print(broker," connected")
    
    client.loop_start()
    print("Subscribing")
    
    t1 = threading.Thread(target=pygame_run, args=(10,))
    t1.start()
    
    main = table()
    
    
#----------------------------------------------------------------#