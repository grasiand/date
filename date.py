from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("Grasiand Saat")
def time():
	string=strftime('%y : %B : %d ')
	label.config(text=string)
	label.after(1000, time)

label = Label(root, font=("ds-digital", 88), background="black", foreground="white")
label.pack(anchor='center')
time()
mainloop()
