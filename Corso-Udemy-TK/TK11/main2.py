import tkinter as tk

def accedi():
   u = user.get()
   p = pwd.get()
   print(u, " ", p)
   user.set("")
   pwd.set("")

app = tk.Tk()
app.geometry("300x200")

user = tk.StringVar()
pwd = tk.StringVar()

tx1 = tk.Entry(app, textvariable = user)
tx1.focus()
tx1.pack()

tx2 = tk.Entry(app, textvariable = pwd)
tx2["show"] = '*'
tx2.pack()

bt = tk.Button(app, text="Accedi", command=accedi)
bt.pack()

app.mainloop()