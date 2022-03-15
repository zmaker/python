import tkinter as tk

def btHandler():
    print("hello!")

app = tk.Tk()
app.title("Hello!")
app.geometry("300x200")

bt = tk.Button(text="Cliccami!", command=btHandler)
bt.pack()

app.mainloop()