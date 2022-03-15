import tkinter as tk

def calcola(*args):
    n = 0
    try:
        n = int(a.get())
    except:
        n = 0
    res = n*n
    b.set(str(res))

app = tk.Tk()
app.geometry("300x200")
app.title("calcolo potenza")

a = tk.StringVar()
a.trace('w', calcola)
b = tk.StringVar()

tx1 = tk.Entry(app, textvariable=a)
tx1.focus()
tx1.pack()

tx2 = tk.Entry(app, textvariable=b)
tx2.pack()

app.mainloop()