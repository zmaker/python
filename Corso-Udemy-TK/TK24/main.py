import tkinter as tk

def getTasto(e):
    print(e)
    if (e.char == 'a'):
        print("AAAA")

def close(e):
    app.destroy()

def x(e):
    print("---")

def y(e):
    print("+++")

app = tk.Tk()
app.geometry("300x200")

#app.bind("<Key>", getTasto)
app.bind("<Escape>", close)
app.bind("<Key-A>", x)
app.bind("<Shift-Tab>", y)


app.mainloop()