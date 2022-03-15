import tkinter as tk

def clic():
    print("hello")

def clic2(event):
    print("hello2")
    print(event)

def clic3(event):
    print("clic3")

app = tk.Tk()
app.geometry("300x200")

'''
width, height –definiscono le sue dimensioni e sono espresse in pixel.
foreground – per il colore del testo;
font – per modificare il tipo di caratteri utilizzati;
image – per associare un icona o un’immagine.
'''
#bt = tk.Button(app, command=clic)
bt = tk.Button(app)
bt["text"] = "Un pulsante!"
bt["state"] = 'active' #disabled
bt.pack()

bt.bind("<Button-1>", clic2)
bt.bind("<Button-2>", clic3)

app.mainloop()