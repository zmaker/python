import tkinter as tk

def clic1():
    print("clic!!")

def azione1(e):
    print(e.x, e.y)

def azione2(e):
    print("tasto dx")

def azione3(e):
    print("doppio clic")

def azione4(e):
    print("x:", e.x, "y:", e.y)

def azione5(e):
    print("INVIO")

def azione6(e):
    print("azione 6")


app = tk.Tk()
app.geometry("300x200")

#bt = tk.Button(app, text="Clic", command=clic1)
bt = tk.Button(app, text="Clic")
bt.pack(fill=tk.BOTH, expand=True)

bt.bind('<Button-1>', azione1)
bt.bind('<Button-2>', azione2)
bt.bind('<Double-Button-1>', azione3)

#bt.bind('<Motion>', azione4)

bt2 = tk.Button(app, text="Clic2")
bt2.pack(fill=tk.BOTH, expand=True)
bt2.focus()
bt2.bind('<Return>', azione5)
bt2.bind('<Return>', azione6, add='+')

#bt2.unbind('<Return>')

app.mainloop()
'''
https://web.archive.org/web/20201111211515id_/https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
Ecco alcuni possibili codici/nomi per i tasti:
• <Alt>
• <Control>
• <Shift>
• <Alt_L>
• <Alt_R>
• <BackSpace> tasto backspace
• <Cancel> tasto CANC
• <Caps_Lock>
• <Control_L>
• <Control_R>
• <Delete>
• <End>
• <Escape>
• <F1>
• <Home>
• <Insert>
• <Return>
• <Right>, <Left>, <Up>, <Down>
• <Tab> tasto tabulazione
Qui di seguito una lista di eventi scatenati in seguito a varie condizioni:
• <Activate> un widget si attiva
• <Button-1>, <Button-2>, <Button-3> pressione di uno dei tasti del mouse
• <ButtonRelease-> tasto rilasciato
• <Deactivate> un widget si disattiva.
• <Enter> Il puntatore del entra nell’area del widget
• <Leave> il puntatore del mouse esce dal widget
• <Motion> il puntatore si muove
'''