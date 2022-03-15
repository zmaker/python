import tkinter as tk

def getSelected():
    v = selected.get()
    lab['text'] = "hai selezionato: " + str(v)

app = tk.Tk()
app.geometry("300x200")

selected = tk.StringVar()
livelli = ('off','min','med','max')

i = 0
for lv in livelli:
    r = tk.Radiobutton(app)
    r["text"] = lv
    r["value"] = i
    i += 1
    r["variable"] = selected
    r["command"] = getSelected
    r.pack()

lab = tk.Label(app)
lab.pack()

'''
• text – il testo da riportare di fianco ad ogni voce.
• width, height –definiscono le dimensioni dell’elemento, in pixel.
• background – per impostare il colore dello sfondo dell’area del componente;
• foreground – per il colore del testo di solito posto alla destra del pallino di spunta.
• font – utilizzato per modificare il carattere utilizzato per il testo.
'''

app.mainloop()