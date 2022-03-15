import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

ll = tk.Label(app, text="Ecco una label!")
ll["background"] = "yellow"
ll["foreground"] = "blue"
#height width, cursor
ll["font"] = ("Kimberley", 20)

ll.pack()

app.mainloop()