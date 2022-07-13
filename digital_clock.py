#creating a digital clock with python 
from tkinter import *
from tkinter.ttk import *

from time import strftime

main = Tk()
main.title('Digital clock with python')

def clock():
    tick = strftime('%H:%M:%S %p')
    
    clock_label. config(text=tick)
    
    clock_label. after(1000, clock)
    
clock_label = Label(main, font=('sans', 80) ,background = 'yellow', foreground='black')   

clock_label.pack(anchor='center') 

clock()
mainloop() 
    