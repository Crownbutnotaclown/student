# -*- coding:utf -8 -*-
#!/usr/bin/python3

import random
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter.ttk import Combobox
import math
import csv

window = Tk()  
window.title("Работа со списками")  
width = 640
height = 390
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0, 0)

lbl3 = Label(text="ФИО преподавателей", font=("Time New Roman", 16))
lbl3.place(x=200, y=65)

txt = scrolledtext.ScrolledText(window, width=58, height=15)  
txt.place(x=5, y=95)

tree = ttk.Treeview(txt, columns=("Surname", "Name", "LastName"))
tree.heading('Surname', text="Surname", anchor=W)
tree.heading('Name', text="Name", anchor=W)
tree.heading('LastName', text="LastName", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=200)
tree.pack()


def clicked():
    with open('exams.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            Surname = row['Surname']
            Name = row['Name']
            LastName = row['LastName']
            tree.insert("", 0, values=(Surname, Name, LastName))

btn = Button(window, text="Вывести результат", command=clicked)  
btn.place(x=255, y=340)

window.mainloop()


