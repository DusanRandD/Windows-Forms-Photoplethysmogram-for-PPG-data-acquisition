#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Created by: Dušan Radivojević 10.2020
# Libraries
from scipy import signal
from scipy.signal import argrelextrema,savgol_filter
import numpy as np


# In[2]:


class spo2class:
    def __init__(self,irarr,redarr):
        self.ir = irarr
        self.red = redarr
    def run(self):
        IR_AC_arr=signal.detrend(self.ir)
        Red_AC_arr=signal.detrend(self.red)
        # Find IR max and min extrem
        Correction=savgol_filter(IR_AC_arr,301,2)
        IR_AC_arr-=Correction
        Smooth_ir_ac_arr=savgol_filter(IR_AC_arr,47,5)*1.3
        IR_max_arr_large=argrelextrema(Smooth_ir_ac_arr,np.greater)
        IR_min_arr_large=argrelextrema(Smooth_ir_ac_arr,np.less)
        suma=0
        IR_max_arr=[]
        fl=0
        for i in range (len(IR_max_arr_large[0])-1):
            suma+=IR_max_arr_large[0][i+1]-IR_max_arr_large[0][i]
        average=suma/(len(IR_max_arr_large[0])-1)
        for i in range (len(IR_max_arr_large[0])-1):
            if((IR_max_arr_large[0][i+1]-IR_max_arr_large[0][i])>=average-4):
                if (fl==0):
                    IR_max_arr.append(IR_max_arr_large[0][i])
                else:
                    fl=0
                if(i==(len(IR_max_arr_large[0])-2)):
                    IR_max_arr.append(IR_max_arr_large[0][i+1])
            else:
                if (Smooth_ir_ac_arr[i]>Smooth_ir_ac_arr[i+1]):
                    if (fl==0):
                        IR_max_arr.append(IR_max_arr_large[0][i])
                        fl=1
                    else:
                        fl=0
                else:
                    if (fl==0):
                        IR_max_arr.append(IR_max_arr_large[0][i+1])
                        fl=1
                    else:
                        fl=0
        suma=0
        IR_min_arr=[]
        fl=0
        for i in range (len(IR_min_arr_large[0])-1):
            suma+=IR_min_arr_large[0][i+1]-IR_min_arr_large[0][i]
        average=suma/(len(IR_min_arr_large[0])-1)
        for i in range (len(IR_min_arr_large[0])-1):
            if((IR_min_arr_large[0][i+1]-IR_min_arr_large[0][i])>=average-4):
                if (fl==0):
                    IR_min_arr.append(IR_min_arr_large[0][i])
                else:
                    fl=0
                if(i==(len(IR_min_arr_large[0])-2)):
                    IR_min_arr.append(IR_min_arr_large[0][i+1])
            else:
                if (Smooth_ir_ac_arr[i]<Smooth_ir_ac_arr[i+1]):
                    if (fl==0):
                        IR_min_arr.append(IR_min_arr_large[0][i])
                        fl=1
                    else:
                        fl=0
                else:
                    if (fl==0):
                        IR_min_arr.append(IR_min_arr_large[0][i+1])
                        fl=1
                    else:
                        fl=0
        #Find Red max and min extrem
        Correction1=savgol_filter(Red_AC_arr,301,2)
        Red_AC_arr-=Correction1
        Smooth_red_ac_arr=savgol_filter(Red_AC_arr,47,5)*1.3
        Red_max_arr_large=argrelextrema(Smooth_red_ac_arr,np.greater)
        Red_min_arr_large=argrelextrema(Smooth_red_ac_arr,np.less)
        suma=0
        Red_max_arr=[]
        fl=0
        for i in range (len(Red_max_arr_large[0])-1):
            suma+=Red_max_arr_large[0][i+1]-Red_max_arr_large[0][i]
        average=suma/(len(Red_max_arr_large[0])-1)
        for i in range (len(Red_max_arr_large[0])-1):
            if((Red_max_arr_large[0][i+1]-Red_max_arr_large[0][i])>=average-4):
                if (fl==0):
                    Red_max_arr.append(Red_max_arr_large[0][i])
                else:
                    fl=0
                if(i==(len(Red_max_arr_large[0])-2)):
                    Red_max_arr.append(Red_max_arr_large[0][i+1])
            else:
                if (Smooth_red_ac_arr[i]>Smooth_red_ac_arr[i+1]):
                    if (fl==0):
                        Red_max_arr.append(Red_max_arr_large[0][i])
                        fl=1
                    else:
                        fl=0
                else:
                    if (fl==0):
                        Red_max_arr.append(Red_max_arr_large[0][i+1])
                        fl=1
                    else:
                        fl=0
        suma=0
        Red_min_arr=[]
        fl=0
        for i in range (len(Red_min_arr_large[0])-1):
            suma+=Red_min_arr_large[0][i+1]-Red_min_arr_large[0][i]
        average=suma/(len(Red_min_arr_large[0])-1)
        for i in range (len(Red_min_arr_large[0])-1):
            if((Red_min_arr_large[0][i+1]-Red_min_arr_large[0][i])>=average-4):
                if (fl==0):
                    Red_min_arr.append(Red_min_arr_large[0][i])
                else:
                    fl=0
                if(i==(len(Red_min_arr_large[0])-2)):
                    Red_min_arr.append(Red_min_arr_large[0][i+1])
            else:
                if (Smooth_red_ac_arr[i]<Smooth_red_ac_arr[i+1]):
                    if (fl==0):
                        Red_min_arr.append(Red_min_arr_large[0][i])
                        fl=1
                    else:
                        fl=0
                else:
                    if (fl==0):
                        Red_min_arr.append(Red_min_arr_large[0][i+1])
                        fl=1
                    else:
                        fl=0
        # Calculation of AC p-p
        min_acc_red=0
        for i in range (len(Red_min_arr)):
            min_acc_red+=Smooth_red_ac_arr[Red_min_arr[i]]
        min_acc_red/=len(Red_min_arr)
        max_acc_red=0
        for i in range (len(Red_max_arr)):
            max_acc_red+=Smooth_red_ac_arr[Red_max_arr[i]]
        max_acc_red/=len(Red_max_arr)
        min_acc_ir=0
        for i in range (len(IR_min_arr)):
            min_acc_ir+=Smooth_ir_ac_arr[IR_min_arr[i]]
        min_acc_ir/=len(IR_min_arr)
        max_acc_ir=0
        for i in range (len(IR_max_arr)):
            max_acc_ir+=Smooth_ir_ac_arr[IR_max_arr[i]]
        max_acc_ir/=len(IR_max_arr)
        AC_Red=max_acc_red-min_acc_red
        AC_IR=max_acc_ir-min_acc_ir
        # Calculation of DC siglans
        DC_Red=0
        DC_IR=0
        for i in range (len(self.ir)):
            DC_Red+=self.red[i]
            DC_IR+=self.ir[i]
        DC_Red/=len(self.red)
        DC_IR/=len(self.ir)
        # Calculation of Perfusion Index
        PI=(AC_IR/DC_IR)*100
        # Calculation of SPO2
        R=(AC_Red/DC_Red)/(AC_IR/DC_IR)
        SPO2=-16.666666*R*R+8.333333*R+100-1.1
        # Hart rate
        suma=0
        for i in range (len(IR_min_arr)-1):
            suma+=IR_min_arr[i+1]-IR_min_arr[i]
        for i in range (len(IR_max_arr)-1):
            suma+=IR_max_arr[i+1]-IR_max_arr[i]
        suma/=len(IR_min_arr)+len(IR_max_arr)-2
        Pulse2=60/(suma*0.02)
        return int(Pulse2),np.round(SPO2,1),np.round(PI,2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




