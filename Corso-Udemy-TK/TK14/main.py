import tkinter as tk

def leggiValore():
    v = scelta.get()
    print(v)
    lab["text"] = v


app = tk.Tk()
app.geometry("300x200")

scelta = tk.StringVar()
ck = tk.Checkbutton(app, command=leggiValore)
ck["text"] = "Accetto le condizioni"
ck["state"] = "active"
ck["onvalue"] = "OK"
ck["offvalue"] = "KO"
ck["variable"] = scelta
ck.pack()

lab = tk.Label(app)
lab.pack()

'''
• text – il testo da riportare di fianco alla casella.
• width, height –definiscono le sue dimensioni in pixel.
• background – per impostare il colore dello sfondo della casella;
• foreground – per il colore del testo.
• font – utilizzato per modificare il carattere utilizzato per il testo.
• state – per abilitare (‘normal’, ‘active’) o disabilitare (‘disabled’) la casella.
'''

app.mainloop()