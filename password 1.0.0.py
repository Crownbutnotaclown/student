# -*- coding:utf -8 -*-
#!/usr/bin/python3

import random
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox
    
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('500x350')


lbl1 = Label(window, text="Колличество необходимых паролей:", font=("Time New Roman", 14))
lbl1.place(x=1, y=1)

combo = Combobox(window)  
combo['values'] = (1, 2, 3, 4, 5)  
combo.current(0) 
combo.place(x=330, y=6)

lbl2 = Label(text="Колличество символов в пароле:", font=("Time New Roman", 14))
lbl2.place(x=1, y=30)

combo2 = Combobox(window)  
combo2['values'] = (8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)  
combo2.current(0) 
combo2.place(x=300, y=35)

lbl3 = Label(text="Результат", font=("Time New Roman", 16))
lbl3.place(x=116, y=65)

txt = scrolledtext.ScrolledText(window, width=40, height=10)  
txt.place(x=5, y=95)

def clicked():
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = combo.get()
    length = combo2.get()
    number = int(number)
    length = int(length)
    for n in range(number):
        password =""
        for i in range(length):
            password += random.choice(chars)
        txt.insert(INSERT, password)
        txt.insert(INSERT, '\n')
    
btn = Button(window, text="Сгенерировать!", command=clicked)  
btn.place(x=370, y=155)  
window.mainloop()




