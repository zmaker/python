import tkinter as tk

def copia():
    str = tx1.get()
    tx2.delete(0, tk.END)
    tx2.insert(0, str)

def cancella():
    tx1.delete(0, tk.END)
    tx2.delete(0, tk.END)

app = tk.Tk()
app.geometry("300x200")

'''
• width, height –definiscono le sue dimensioni e sono espresse in pixel.
• background – il colore dello sfondo;
• foreground – per il colore del testo;
• font – per modificare il tipo di caratteri utilizzati;
• cursor - modifica l’aspetto del cursore quando scorre sopra all’elemento.
• show – specifica il carattere da usare per visualizzare i caratteri. È utilizzato per
trasformare la casella di testo in un campo password.
'''
tx1 = tk.Entry(app)
tx1.focus()
tx1.pack()

bt = tk.Button(app, text="Copia", command=copia)
bt.pack()
bt2 = tk.Button(app, text="Cancella", command=cancella)
bt2.pack()

tx2 = tk.Entry(app)
tx2.pack()



app.mainloop()