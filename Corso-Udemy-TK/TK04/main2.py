import tkinter as tk

def btHandler():
    lb["text"] = "Ciao!"

app = tk.Tk()
app.title("Hello!")
app.geometry("300x200")

bt = tk.Button(text="Cliccami!", command=btHandler)
bt.pack()

lb = tk.Label(text="...")
lb.pack()

app.mainloop()