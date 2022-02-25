#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:55:00 2020

@author: emmanuel
"""
from tkinter import *
from tkinter import messagebox as MessageBox    
import sys
import os
import math
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tk_tools
from tkinter import scrolledtext
from tkinter import ttk

class Falsapos:
    

     

    
 def __init__(self):

        self.window = Tk() 
        self.window.title("Gauss-Siedel")
        self.window.geometry("1300x640")
        self.window.resizable(0,0)
        
        self.ecs=IntVar(value=0) 
        self._entry = {}
        self._entry2 = {}
        self._entry3 = {}
        self.it=IntVar(value=0)
        self.err=DoubleVar(value=0.0)
        
        self.lbl1=Label(self.window,text='Indique el número de ecuaciones: ') 
        self.lbl1.place(x=10, y=20)
        self.lbl3=Label(self.window,text='Indique el número de iteraciones: ')
        self.lbl3.place(x=10, y=60)
        self.lbl6=Label(self.window,text='Ingrese el error (válido desde 0.01 a 0.00001): ')
        self.lbl6.place(x=10, y=100)

        
        self.t1=Entry(self.window,textvariable=self.ecs)    
        self.t1.place(x=240, y=20,width='50')
        self.t1.delete(0,'end')
        self.t1.focus_set()
        self.t2=Entry(self.window,textvariable=self.it)
        self.t2.place(x=240, y=60,width='50')
        self.t2.delete(0,'end')
        self.t4=Entry(self.window,textvariable=self.err)
        self.t4.place(x=323, y=100,width='80')
        self.t4.delete(0,'end')
        

        
        
 def reset(self):   
             python = sys.executable
             os.execl(python, python, * sys.argv)
             
 def MecValEc(self): 
     ecs1=(self.t1.get())
     try:
         entero = int(ecs1)
     except ValueError:
         MessageBox.showwarning("Error","El número de ecuaciones debe ser entero, por favor ingrese un valor entero positivo.")  
  
 def MecValEr(self):    
     error1=(self.t4.get())
     try:
             floatante = float(error1)
     except ValueError:
                 MessageBox.showerror("Error","El valor del error debe ser decimal, por favor ingrese un valor dentro del rango.") 
                 
 def MecValIt(self):
     it1=(self.t2.get()) 
     try:
                 entero = int(it1)
     except ValueError:
                 MessageBox.showerror("Error","El número de iteraciones debe ser entero, por favor ingrese un valor entero positivo.")  

        
 def CrearMa(self): 
    self.MecValEc()  
    if not self.t1.get():
        MessageBox.showerror("Error","Ingrese el número de ecuaciones")  
        self.t1.delete(0,'end')
    self.MecValIt()
    if not self.t2.get():
        MessageBox.showerror("Error","Ingrese el número de iteraciones")
        self.t2.delete(0,'end')
    self.MecValEr()  
    if not self.t4.get():
        MessageBox.showerror("Error","Ingrese el error.")
        self.t4.delete(0,'end')
    else:
        ecs=int(self.t1.get())
        error=float(self.t4.get())
        if ecs>10:
            MessageBox.showerror("Error","El número máximo de ecuaciones es 10")
            self.t1.delete(0,'end')
        else:
            if ecs<=1:
                MessageBox.showerror("Error","El sistema de ecuaciones que puede ingresar va desde un 2x2, hasta un sistema 10x10")
                self.t1.delete(0,'end')
            else:       
                if error>0.01:
                    MessageBox.showerror("Error","Los valores válidos para el error van desde 0.01 a 0.00001")
                    self.t4.delete(0,'end')
                else:
                    if error<0.00001:
                        MessageBox.showerror("Error","Los valores válidos para el error van desde 0.01 a 0.00001")
                        self.t4.delete(0,'end')
                    else:
                        self.lbl4=Label(self.window,text='A')  
                        self.lbl4.place(x=10, y=180)
                        self.lbl5=Label(self.window,text='B')
                        self.lbl5.place(x=(ecs*58)-(ecs*1.3),y=180)
                        for fila in range(0,ecs):
                            for columna in range(0, ecs):
                                index = (columna,fila)
                                self.e = ttk.Entry(self.window,width=4)
                                self.e.grid(padx=5, pady=5,column=columna, row=fila)
                                self.e.place(x=fila*46+10,y=200+30*columna)
                                self._entry[index] = self.e
                    
                        for columna in range(0, ecs):
                            index2 = columna
                            self.e2 = ttk.Entry(self.window,width=4)
                            self.e2.place(x=(ecs*58)-(ecs*1.3),y=200+30*columna)
                            self._entry2[index2] = self.e2
    
                
 def CrearAp(self): 
        self.MecValEc()
        if not self.t1.get():
            MessageBox.showerror("Error","Primero ingrese el número de ecuaciones")
            self.t1.delete(0,'end')
        self.MecValIt()
        if not self.t2.get():
            MessageBox.showerror("Error","Primero ingrese el número de iteraciones")
            self.t2.delete(0,'end')
        self.MecValEr() 
        if not self.t4.get():
            MessageBox.showerror("Error","Primero ingrese el error")
            self.t4.delete(0,'end')
        else:
            ecs=int(self.t1.get())
            error=float(self.t4.get())
            if ecs>10:
                MessageBox.showerror("Error","El número máximo de ecuaciones es 10")
                self.t1.delete(0,'end')
            else:
                if ecs<=1:
                    MessageBox.showerror("Error","El sistema de ecuaciones que puede ingresar va desde un 2x2, hasta un sistema 10x10")
                    self.t1.delete(0,'end')
                else:            
                    if error>0.01:
                        MessageBox.showerror("Error","Los valores válidos para el error van desde 0.01 a 0.00001")
                        self.t4.delete(0,'end')
                    else:
                        if error<0.00001:
                            MessageBox.showerror("Error","Los valores válidos para el error van desde 0.01 a 0.00001")
                            self.t4.delete(0,'end')
                        else:
                            self.lbl7=Label(self.window,text='x^{0}')   
                            self.lbl7.place(x=700, y=180)
                            for columna in range(0, ecs):
                                index3 = columna
                                self.e3 = ttk.Entry(self.window,width=4)
                                self.e3.place(x=700,y=200+30*columna)
                                self._entry3[index3] = self.e3
     

 def GetDat(self):  

        ecs=int(self.t1.get()) 
        result = []
        for row in range(ecs):
            current_row = []
            for column in range(ecs):
                index = (row, column)
                current_row.append(float(self._entry[index].get()))
            result.append(current_row)          
        return result
        
 def GetDat2(self):   

        ecs=int(self.t1.get()) 
        result2 = []
        for row in range(ecs):
                index2 = row
                result2.append(float(self._entry2[index2].get()))          
        return result2     
        
 def GetDat3(self):    

        ecs=int(self.t1.get()) 
        result3 = []
        for row in range(ecs):
                index3 = row
                result3.append(float(self._entry3[index3].get()))          
        return result3   
        
    
 
        else:
            if errorCal<error:
                self.textC.insert(INSERT,"!!! Se llegó a una solución bajo el parámetro de error justo o antes de el número de iteraciones solicitadas !!!\n"+"\n")
                self.textC.insert(INSERT,"El número de iteraciones requeridas fueron: "+str(i+1)+"\n"+"\n")
                xfinal2=[]
                for j in range(len(x)):
                    xfinal2.append(round(float(x[j]),3))
                self.textC.insert(INSERT,"La solución final es: "+str(xfinal2)+"\n") 
                break    
    return x

        
 def Show(self):    
    self.MecValEc()
    if not self.t1.get():
        MessageBox.showerror("Error","Primero ingrese el número de ecuaciones")
        self.t1.delete(0,'end')
    self.MecValIt()
    if not self.t2.get():
        MessageBox.showerror("Error","Primero ingrese el número de iteraciones")
        self.t2.delete(0,'end')
    self.MecValEr() 
    if not self.t4.get():
        MessageBox.showerror("Error","Primero ingrese el error")
        self.t4.delete(0,'end')
    else:
            ecs=int(self.t1.get())
            error=float(self.t4.get())
            if ecs>10:
                MessageBox.showerror("Error","El número máximo de ecuaciones es 10")
                self.t1.delete(0,'end')             
            else:
                if ecs<=1:
                    MessageBox.showerror("Error","El sistema de ecuaciones que puede ingresar va desde un 2x2, hasta un sistema 10x10")
                    self.t1.delete(0,'end')
                else:
                    if error>0.01:
                        MessageBox.showerror("Error","Los valores válidos para el error van desde 0.01 a 0.00001")
                        self.t4.delete(0,'end')
                    else:
                        if error<0.00001:
                            MessageBox.showerror("Error","Los valores válidos para el error van desde 0.01 a 0.00001")
                            self.t4.delete(0,'end')
                        else:
                            it=int(self.t2.get()) 
                            self.textC.config(state="normal")
                            self.textC.delete(1.0,END)
                            self.textC.insert(INSERT,"*** Datos del sistema de ecuaciones a resolver ***"+"\n"+"\n") 
                            self.textC.insert(INSERT,"Matríz (A): "+str(self.GetDat())+"\n"+"\n") 
                            self.textC.insert(INSERT,"Resultados (B): "+str(self.GetDat2())+"\n"+"\n")
                            self.textC.insert(INSERT,"Solucion aproximada (propuesta): "+str(self.GetDat3())+"\n"+"\n")
                            self.textC.insert(INSERT,"Iteraciones solicitadas: "+str(it)+"\n") 
                            self.textC.insert(INSERT,"\n"+"\n") 
                            self.textC.insert(INSERT,"Resultados del método de Gauss-Siedel..."+"\n"+"\n")                 
                            x=self.GaussXSie(self.GetDat(), self.GetDat3(), self.GetDat2(),it)  
                            self.textC.config(state='disable')

     
                
def main():
    objeto=Falsapos()
    return 0

if __name__ == '__main__':
    main()
