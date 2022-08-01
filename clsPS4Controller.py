#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pygame
import threading
import time
from clsControllerData import ControllerData 
class PS4Controller(threading.Thread):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(PS4Controller, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
        self.cTime = time.ctime
        self.paused = False
        self.error = False
        """Initialize the joystick components"""
        pygame.init()
        pygame.joystick.init()
        try: 
            self.controller = pygame.joystick.Joystick(0)
        except Exception as e:
            self.error = True
            print ("Error in Joystick : "+str(e))
            self.error=True
            return 
        self.controller.init()        

    def stop(self):
        self._stop.set()
        self.join()

    def stopped(self):
        return self._stop.isSet()



    def pause(self):
        self.paused = True
        #this is should make the calling thread wait if pause() is
        #called while the thread is 'doing the thing', until it is
        #finished 'doing the thing'

    #should just resume the thread
    def resume(self):
        self.paused = False


    def run(self):
        """Listen for events to happen"""
        
        if not self.axis_data:
            self.axis_data = {}
        if not self.button_data:
            self.button_data = {}
            try:
                for i in range(self.controller.get_numbuttons()):
                    self.button_data[i] = False
            except:
                self.error = True
                return False
        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
              
            if self.stopped():
                return
            if not self.paused:
                for event in pygame.event.get():
                    #print "Changed!"
                    ControllerData.changed=True
                    ControllerData.newData=True
                    if event.type == pygame.JOYAXISMOTION:
                        #get_axis()
                        self.axis_data[event.axis] = round(event.value,2)
                        #print (event.axis)
                        #print (event.value)
                    elif event.type == pygame.JOYBUTTONDOWN:
                        self.button_data[event.button] = True
                    elif event.type == pygame.JOYBUTTONUP:
                        self.button_data[event.button] = False
                        
                    #elif event.type == pygame.JOYHATMOTION:
                    #    print (event.value)
                    #    self.hat_data[event.hat] = event.value

                    # Insert your code on what you would like to happen for each event here!
                    # In the current setup, I have the state simply printing out to the screen.
                    
                    
                    #pprint.pprint(self.button_data)
                    #pprint.pprint(self.axis_data)
                    #pprint.pprint(self.hat_data)
                    #print ("buttuns Data")
                    #print self.button_data
                    #print ("Axis Data")
                    #print self.axis_data

                    #print ("Hat Data")
                    #print self.hat_data
                    ControllerData.button_data=self.button_data
                    ControllerData.axis_data = self.axis_data
                    
                    ControllerData.simplfyData()
                else:
                    ControllerData.changed =False


            self.cTime= time.ctime()
            #print(self.cTime)
            

if __name__ == "__main__":
    ps4 = PS4Controller()
    if not ps4.error:
        #ps4.init()
        ps4.start()
        #t = threading.Thread(target =ps4.listen)
        #print("listener will started ")
        #t.start()
        #print("listener started ")
        i=10000
        while(i>0):
            #print(thread.cTime)
            #time.sleep(0.01)
            #print(thread.cTime)
            #time.sleep(1)
            #print(thread.cTime)
            #if ControllerData.newData:
            os.system('clear')
            #print "Axis Data"
            #print ControllerData.axis_data
            #print "Buttons Data"
            #print ControllerData.button_data
            #x = ControllerData.axis_data[0]*15
            #y = (ControllerData.axis_data[1]*-1)*15
            if ControllerData.L_Ball_H!= None:
                angle =  ControllerData.getAngle360(0,0,ControllerData.L_Ball_H,ControllerData.L_Ball_V)
                print ("( L ) : "+str(angle))
            if ControllerData.R_Ball_H!= None:			
                angle =  ControllerData.getAngle360(0,0,ControllerData.R_Ball_H,ControllerData.R_Ball_V)
                print ("( R )  : "+str(angle))

            print ("Simplified Data")
            #ControllerData.printSimplifiedValues()
            if ControllerData.R1:
                break
            
            #arrWheelsValues= ControllerData.getwheelsValues(angle,x,y)
            
            #txtWheels = ControllerData.convertValuesToText(arrWheelsValues)
            #print txtWheels
            ControllerData.newData=False
            #print(ps4.cTime)
            #print ("timer"+str(i))
            i = i-1
        ps4.stop()
        print ("terminated ")
        time.sleep(1)
        print ("terminated and sleeped !")
        #ps4.join()
        #t.join()