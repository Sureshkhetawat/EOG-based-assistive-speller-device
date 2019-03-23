#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:06:38 2019

@author: suresh
"""

import sys
from tkinter import *
import tkinter
import numpy as np

#root = tkinter.Tk()
#root.geometry('500x500')

buttons = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','1/2']
buttons2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Clc','2/2']
#global var_add
#var_add = ''

class keyboard_switch(tkinter.Tk):
    
    def __init__(self,*arg,**kwargs):
        
        tkinter.Tk.__init__(self,*arg,**kwargs)
        container = tkinter.Frame(self)
        
        container.pack(side="top", fill='both',expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (kb_page1, kb_page2):
                
            frame  = F(container, self)
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(kb_page1)
        
    def show_frame(self, cont):
        cont.refill()
        frame = self.frames[cont]
        frame.tkraise()

class kb:
    var_add = ''
        
class kb_page1(tkinter.Frame, kb):
    txtDisplay = None
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        
        #print('hiiii')
        self.controller=controller
#        global txtDisplay
        kb_page1.txtDisplay = tkinter.Entry(self, font='Helvetica 25 bold', width=60, bd=15)
        kb_page1.txtDisplay.grid(row=1,column = 0,columnspan = 4,padx=5,pady=10,ipady=3)
        kb_page1.txtDisplay.insert(tkinter.END,kb.var_add)
        print("1")
        #txtDisplay.bind("<Button-1>", lambda e: Key_buttons())
        controller
        var_row = 2
        var_col = 0
        
        
        for button in buttons:
        #print(button)
            command = lambda x=button: self.select(x)
        
            tkinter.Button(self, text=button, height=5, width=15, font="Times 20 bold", bg="#3c4987", fg="#ffffff", command = command).grid(row = var_row,column = var_col)

            var_col = var_col + 1
    
            if var_col >= 4:
                var_col = 0
                var_row = var_row + 1
                #print(var_row,var_col)
                
    def select(self, var_button):
        if  var_button == '1/2':
            print("Change it1")
            self.controller.show_frame(kb_page2)
            #self.txtDisplay.insert(tkinter.END,kb.var_add)
            #global buttons
            #buttons = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','1/2']
                        
        else:
            #print("page1 select else")
            #print(var_button)
            kb.var_add = kb.var_add + var_button
            kb_page1.txtDisplay.delete(0,tkinter.END)
            kb_page1.txtDisplay.insert(tkinter.END,kb.var_add)
            
    @classmethod
    def refill(cls):
        cls.txtDisplay.delete(0,tkinter.END)
        cls.txtDisplay.insert(tkinter.END,kb.var_add) 

class kb_page2(tkinter.Frame, kb):
    txtDisplay = None
    def __init__(self, parent, controller):
        
        tkinter.Frame.__init__(self, parent)
        #print('hiiii')
        self.controller = controller
        print("2")
        
        #global txtDisplay
        kb_page2.txtDisplay = tkinter.Entry(self, font='Helvetica 25 bold', width=60, bd=15)
        kb_page2.txtDisplay.grid(row=1,column = 0,columnspan = 4,padx=5,pady=10,ipady=3)
        kb_page2.txtDisplay.insert(tkinter.END,kb.var_add)
        #txtDisplay.bind("<Button-1>", lambda e: Key_buttons())
        
        
        
        var_row = 2
        var_col = 0
        
        
        for button in buttons2:
        #print(button)
            command = lambda x=button: self.select(x)
        
            tkinter.Button(self, text=button, height=5, width=15, font="Times 20 bold", bg="#3c4987", fg="#ffffff", command = command).grid(row = var_row,column = var_col)

            var_col = var_col + 1
    
            if var_col >= 4:
                var_col = 0
                var_row = var_row + 1
                #print(var_row,var_col)
                
                
    def select(self, var_button):
    
        if  var_button == '2/2':
            print("Change it2")
            self.controller.show_frame(kb_page1)
            #self.txtDisplay.insert(tkinter.END,kb.var_add)
            
        elif var_button == 'Clc':
            print('pressed backspace')
            kb.var_add = kb.var_add[:len(kb.var_add)-1]
            kb_page2.txtDisplay.delete(0,tkinter.END)
            kb_page2.txtDisplay.insert(tkinter.END,kb.var_add)
            
               
        else:
            #print("page2 select else")
            kb.var_add = kb.var_add + var_button
            kb_page2.txtDisplay.delete(0,tkinter.END)
            kb_page2.txtDisplay.insert(tkinter.END,kb.var_add)  
    
    @classmethod
    def refill(cls):
        cls.txtDisplay.delete(0,tkinter.END)
        cls.txtDisplay.insert(tkinter.END,kb.var_add) 


app = keyboard_switch()
app.mainloop()

print('The text printed is :-\n',kb.var_add)
