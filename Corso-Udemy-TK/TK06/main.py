import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

#fr = tk.Frame(master=app, width=200, height=100)
fr = tk.Frame(master=app)
fr["width"] = 200
fr["height"] = 100
fr["background"] = '#01906A'
fr["relief"] = 'sunken'
#flat, raised, sunken, solid, ridge, groove
fr["borderwidth"] = 2
#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
fr["cursor"] = 'pencil'

fr.pack()

app.mainloop()
