import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.messagebox import showwarning
from tkinter.messagebox import showerror
from tkinter.messagebox import askyesno
from tkinter.messagebox import askretrycancel

#https://pythonguides.com/python-tkinter-messagebox/

def messaggio():
    tk.messagebox.showinfo('Attenzione!', "Ricordati di bagnare le piante!")

def messaggio2():
    tk.messagebox.showwarning('Attenzione!', "Ricordati di bagnare le piante!")

def messaggio3():
    tk.messagebox.showerror('Attenzione!', "Ricordati di bagnare le piante!")

def messaggio4():
    ans = tk.messagebox.askyesno(title="sei sicuro?", message="Vuoi uscire?")
    if ans:
        app.destroy()

app = tk.Tk()
app.geometry("300x200")

bt = tk.Button(app, text="clic me", command=messaggio)
bt.pack()
bt2 = tk.Button(app, text="warn", command=messaggio2)
bt2.pack()
bt3 = tk.Button(app, text="error", command=messaggio3)
bt3.pack()

bt4 = tk.Button(app, text="yes/no", command=messaggio4)
bt4.pack()




app.mainloop()