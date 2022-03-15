import tkinter as tk

'''
• fill – specifica come estendere il componente nello spazio a lui assegnato. Se il valore è
pari a X, il componente si estenderà in orizzontale, con Y in verticale e con BOTH in
entrambe le direzioni.
• side – indica all’algoritmo su che lato dell’area disponibile disporre il componente
rispetto. Le possibilità sono quattro: TOP, BOTTOM, LEFT, RIGHT. Se la proprietà non è
specificata il widget sarà centrato.
• expand – accetta i valori booleani True o False e serve a dare maggiore spazio al
componente nel caso in cui il contenitore del widget ne abbia in più. Se più componenti
richiedono spazio aggiuntivo, questo sarà diviso equamente.
• padx, pady – aggiungono un margine interno in orizzontale o verticale. Il valore da
indicare è in pixel.
'''

app = tk.Tk()
app.geometry("300x200")

lab = tk.Label(app, text="Come funziona pack?", background="#fdffc7")
lab.pack()

ent = tk.Entry(app, background="#c7f9ff")
ent.pack()

bt = tk.Button(app, text="cliccami")
bt.pack()


app.mainloop()