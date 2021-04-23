#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:55:00 2020

@author: emmanuel
"""
from tkinter import *
from tkinter import messagebox as MessageBox    #En esta parte se importan las respectivas bibliotecas y librerias que se utilizarán en el código
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

        self.window = Tk() #se crea una ventana en tkinter.
        self.window.title("Gauss-Siedel")
        self.window.geometry("1300x640")
        self.window.resizable(0,0)
        
        self.ecs=IntVar(value=0) #se crean los atributos y datos de entrada que se ocuparán posteriormente.
        self._entry = {}
        self._entry2 = {}
        self._entry3 = {}
        self.it=IntVar(value=0)
        self.err=DoubleVar(value=0.0)
        
        self.lbl1=Label(self.window,text='Indique el número de ecuaciones: ') #etiquetas que se muestran en la ventana del programa.
        self.lbl1.place(x=10, y=20)
        self.lbl3=Label(self.window,text='Indique el número de iteraciones: ')
        self.lbl3.place(x=10, y=60)
        self.lbl6=Label(self.window,text='Ingrese el error (válido desde 0.01 a 0.00001): ')
        self.lbl6.place(x=10, y=100)

        
        self.t1=Entry(self.window,textvariable=self.ecs)    #estas son las casillas en las cuales se ingresarán datos como el número de ecuaciones, iteraciones, etc. dentro de la ventana del programa.
        self.t1.place(x=240, y=20,width='50')
        self.t1.delete(0,'end')
        self.t1.focus_set()
        self.t2=Entry(self.window,textvariable=self.it)
        self.t2.place(x=240, y=60,width='50')
        self.t2.delete(0,'end')
        self.t4=Entry(self.window,textvariable=self.err)
        self.t4.place(x=323, y=100,width='80')
        self.t4.delete(0,'end')
        

        
        self.textC=scrolledtext.ScrolledText(self.window,width=55,height=30)    #Este es un bloque de texto en el cual se desplegarán los resultados del método de Gauss-Siedel dentro de la ventana principal.
        self.textC.place(x=860, y=80)
        
        self.b1=Button(self.window,text='Ingresar coeficientes',command=self.CrearMa)   #Estos son los botones los cuales realizaran las acciones correspondientes a la creación de matrices y el procedimiento de Gauss-Siedel.
        self.b1.place(x=10, y=150)
        self.b4=Button(self.window,text='Calcular',command=self.Show)
        self.b4.place(x=1000, y=20)
        self.b2=Button(self.window,text='Ingresar solución propuesta',command=self.CrearAp)
        self.b2.place(x=620, y=20)
        self.b3=Button(self.window,text='Reiniciar todo',command=self.reset)
        self.b3.place(x=1155, y=600)

        self.window.mainloop() 

 def reset(self):    #Este es el método que resetea la ventana principal.
             python = sys.executable
             os.execl(python, python, * sys.argv)
             
 def MecValEc(self): # Mecanismo de validación (método) para el número de ecuaciones.
     ecs1=(self.t1.get())
     try:
         entero = int(ecs1)
     except ValueError:
         MessageBox.showwarning("Error","El número de ecuaciones debe ser entero, por favor ingrese un valor entero positivo.")  
  
 def MecValEr(self):    # Mecanismo de validación (método) para el valor del error. 
     error1=(self.t4.get())
     try:
             floatante = float(error1)
     except ValueError:
                 MessageBox.showerror("Error","El valor del error debe ser decimal, por favor ingrese un valor dentro del rango.") 
                 
 def MecValIt(self):  # Mecanismo de validación (método) para el número de iteraciones. 
     it1=(self.t2.get()) 
     try:
                 entero = int(it1)
     except ValueError:
                 MessageBox.showerror("Error","El número de iteraciones debe ser entero, por favor ingrese un valor entero positivo.")  

        
 def CrearMa(self):  #Este es el método para crear la matriz de coeficientes en la interfaz de la ventana principal.
    self.MecValEc()  
    if not self.t1.get():
        MessageBox.showerror("Error","Ingrese el número de ecuaciones")  #Estos son mensajes de verificación (mecanismos de verificación) para verificar que los números que ingresa el usuario esten en un rango válido.
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
                        self.lbl4=Label(self.window,text='A')   #Esta es la parte donde se comienza a crear la matriz en la ventana principal.
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
    
                
 def CrearAp(self):  #Este es el método el cual crea un vector para ingresar la solución propuesta en la ventana principal.
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
     

 def GetDat(self):  #Este método recoje los datos ingresados en la matriz creada en la intefaz y crea una matriz (La famosa matriz de coeficientes A).  

        ecs=int(self.t1.get()) 
        result = []
        for row in range(ecs):
            current_row = []
            for column in range(ecs):
                index = (row, column)
                current_row.append(float(self._entry[index].get()))
            result.append(current_row)          
        return result
        
 def GetDat2(self):    #Este método recoje los datos ingresados de los resultados a los cuales se iguala cada una de las ecuaciones del sistema de ecuaciones y crea el vector B.

        ecs=int(self.t1.get()) 
        result2 = []
        for row in range(ecs):
                index2 = row
                result2.append(float(self._entry2[index2].get()))          
        return result2     
        
 def GetDat3(self):    #Este método recoje los datos ingresados en la solución propuesta y crea un vector x^{0}.

        ecs=int(self.t1.get()) 
        result3 = []
        for row in range(ecs):
                index3 = row
                result3.append(float(self._entry3[index3].get()))          
        return result3   
        
    
 def GaussXSie(self,A, x, b, n): #Este método realiza el algoritmo del método de Gauss-Siedel, regresando un vector con la solución aproximada.
    error=float(self.t4.get())
    L = np.tril(A)
    U = A - L
    for i in range(0,n):
        xold=x
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        norma1=np.linalg.norm(x-xold)
        norma2=np.linalg.norm(x)
        errorCal=norma1/norma2
        if errorCal>error:
            self.textC.insert(INSERT,"Iteracón: "+str(i+1)+"\n")
            xfinal1=[]
            for j in range(len(x)):
                xfinal1.append("{0:.5f}".format(float(x[j])))
            self.textC.insert(INSERT,"aproximación: "+str(xfinal1)+"\n")
            self.textC.insert(INSERT,"\n")
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

        
 def Show(self):    #Este método muestra toda la información del algoritmo dentro del bloque de texto ubicado en la ventana principal.
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

     
                
def main(): #Fin XD
    objeto=Falsapos()
    return 0

if __name__ == '__main__':
    main()