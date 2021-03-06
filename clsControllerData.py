#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math
class ControllerData:

    axis_data = None
    button_data = None
    changed = False
    newData=False
        
    R_Ctr_D= False
    R_Ctr_R= False
    R_Ctr_U= False
    R_Ctr_L= False
    L1= False
    R1= False
    L2= False
    R2= False
    Share= False
    Options= False
    PS= False
    L_Ball_Btn= False
    R_Ball_Btn= False
    Pad = False

#...................................
    L_Ball_H=0.000
    L_Ball_V=0.000
    L2= -1.000
    L2_bool= False
    R_Ball_H=0.000
    R_Ball_V=0.000
    R2= -1.000
    R2_bool=False
    L_Ctr_H=0.000
    L_Ctr_V=0.000
    #Added Values
    L_Ctr_R=False
    L_Ctr_L=False
    L_Ctr_D=False
    L_Ctr_U=False
    #End Added Values
    @staticmethod
    def simplfyData():
        """ This Method for  
        @type  paramName: Bool
        @param paramName : Description
        @rtype:  Boolean
        @return: True : everything went fine
        False : Something went wrong
        """ 
        try: 
            
                ControllerData.R_Ctr_D= ControllerData.button_data.get(0)
                ControllerData.R_Ctr_R= ControllerData.button_data.get(1)
                ControllerData.R_Ctr_U= ControllerData.button_data.get(2)
                ControllerData.R_Ctr_L= ControllerData.button_data.get(3)
                ControllerData.L1= ControllerData.button_data.get(4)
                ControllerData.R1= ControllerData.button_data.get(5)
                ControllerData.L2= ControllerData.button_data.get(6)
                ControllerData.R2= ControllerData.button_data.get(7)
                ControllerData.Share= ControllerData.button_data.get(8)
                ControllerData.Options= ControllerData.button_data.get(9)
                ControllerData.PS= ControllerData.button_data.get(12)
                ControllerData.L_Ball_Btn= ControllerData.button_data.get(10)
                ControllerData.R_Ball_Btn= ControllerData.button_data.get(11)
                ControllerData.Pad= ControllerData.button_data.get(13)


                #......................

                ControllerData.L_Ball_H=ControllerData.axis_data.get(0)
                #ControllerData.L_Ball_H=CentrollerData.axis_data.get_axis(0)
                ControllerData.L_Ball_V=ControllerData.axis_data.get(1)*-1
                ControllerData.L2= ControllerData.axis_data.get(3)
                ControllerData.R_Ball_H=ControllerData.axis_data.get(2)
                ControllerData.R_Ball_V=ControllerData.axis_data.get(5)*-1
                ControllerData.R2= ControllerData.axis_data.get(4)
                ControllerData.L_Ctr_H=ControllerData.axis_data.get(6)
                ControllerData.L_Ctr_V=ControllerData.axis_data.get(7)
                #Added Values
                ControllerData.L_Ctr_R=False
                ControllerData.L_Ctr_L=False
                ControllerData.L_Ctr_D=False
                ControllerData.L_Ctr_U=False
                ControllerData.L2_bool=False
                ControllerData.R2_bool = False
                if ControllerData.L_Ctr_H>0:
                    ControllerData.L_Ctr_R=True
                else:
                    if ControllerData.L_Ctr_H<0:
                        ControllerData.L_Ctr_L=True

                if ControllerData.L_Ctr_V>0:
                    ControllerData.L_Ctr_D = True
                else:
                    if ControllerData.L_Ctr_V<0:
                        ControllerData.L_Ctr_U = True

                #L 2 and R 2 Bool
                if ControllerData.L2>-1:
                    ControllerData.L2_bool =True
                if ControllerData.R2>-1:
                    ControllerData.R2_bool= True
                return True
        except Exception as e:
            #print (e)
            return False
    @staticmethod
    def printSimplifiedValues():


        # buttons Data
        print("R_Ctr_D : "+str(ControllerData.R_Ctr_D))
        print("R_Ctr_R : "+str(ControllerData.R_Ctr_R))
        print("R_Ctr_U : "+str(ControllerData.R_Ctr_U))
        print("R_Ctr_L : "+str(ControllerData.R_Ctr_L))
        print("L1 : " +str( ControllerData.L1))
        print("R1 : "+str(ControllerData.R1))
        print("L2 : "+str( ControllerData.L2))
        print("R2 : "+str( ControllerData.R2))
        print("Share : "+str(ControllerData.Share))
        print("Options : "+ str(ControllerData.Options))
        print("PS : "+ str(ControllerData.PS))
        print("L_Ball_btn : "+ str(ControllerData.L_Ball_Btn))
        print("R_Ball_Btn : " + str(ControllerData.R_Ball_Btn))

        print ("Range Data ")
        print("L_Ball_H : "+str(ControllerData.L_Ball_H))
        print("L_Ball_V : "+str(ControllerData.L_Ball_V))
        print("L2 : "+ str(ControllerData.L2))
        print ("R_Ball_H : " +  str(ControllerData.R_Ball_H))
        print ("R_Ball_V : " +  str(ControllerData.R_Ball_V))
        print ("R2 : " +  str(ControllerData.R2))
        print("L_Ctr_H : "+str(ControllerData.L_Ctr_H))
        print("L_Ctr_V : "+str(ControllerData.L_Ctr_V))
        #Added Values
        print ("Added Buttons  Data ")
        print("L_Ctr_R : "+str(ControllerData.L_Ctr_R))
        print("L_Ctr_L : "+str(ControllerData.L_Ctr_L))
        print("L_Ctr_D : "+str(ControllerData.L_Ctr_D))
        print("L_Ctr_U : "+str(ControllerData.L_Ctr_U))
        print("L2_bool : "+str(ControllerData.L2_bool))
        print("R2_bool : "+str(ControllerData.R2_bool))

    """
    Functions for movement 
    """
    @staticmethod
    def getAngle360(cx, cy, ex, ey):
        theta = ControllerData._getAngle(cx, cy, ex, ey) # range (-180, 180]
        if theta < 0:
            theta = 360 + theta #range [0, 360)
        if theta == 0:
            theta = 360
        #print theta
        return theta
    @staticmethod
    def _getAngle(cx, cy, ex, ey):

        dy = ey - cy

        dx = ex - cx

        theta = math.atan2(dy, dx) # range (-PI, PI]

        theta *= 180 / math.pi   # rads to degs, range (-180, 180]
        return theta