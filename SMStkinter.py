import requests
import os
from tkinter import *
import time
from tkinter import messagebox as MessageBox


root = Tk()
root.title("SMSFREE")
root.geometry("430x200")
root.resizable(0, 0)
def contact():
    you = StringVar()
    you.set("https://www.youtube.com/channel/UCSJ0FKKF-tUeu_Oa-1Z07lA")
    Label(root, text="Youtube: ").grid(row=4, column=0)
    Entry(root, textvariable=you, width=45).grid(row=4, column=1)
    Label(root, text="Created By Piter", font="bold").grid(row=5, column=1)

def exit():
    root.destroy()
    

def enviar():
    enti1 = ent1.get()
    enti2 = ent2.get()
    if enti1 == "" or enti2 == "":
        MessageBox.showinfo("Error", "No puede dejar campos vacios")
    else:
        resp = requests.post('https://textbelt.com/text', {
          'phone': enti1,
          'message': enti2,
          'key': 'textbelt',
          })
        string = str(resp.json())
        
        if "error" in string:
            MessageBox.showinfo("Error", "No puede enviar mensajes a este numero")
        else:
            MessageBox.showinfo("Enviado", "Mensaje enviado al \n " + enti1)
            ent1.set("")
            ent2.set("")

ent1 = StringVar()
ent2 = StringVar()
Button(root, text="Salir", command=exit).grid(row=0, column=2)
Label(root, text="PiterSk", font="bold").grid(row=0, column=0)
Label(root, text="Ponga el numero: ", fg="black").grid(row=1, column=0)
Entry(root, textvariable=ent1, width=45).grid(row=1, column=1)

Label(root, text="Escriba el MSG: ", fg="black").grid(row=2, column=0)
Entry(root, textvariable=ent2, width=45).grid(row=2, column=1)

Button(root, text="Enviar", command=enviar).grid(row=3, column=0)
Button(root, text="Contacto", command=contact).grid(row=3, column=1)

root.mainloop()
