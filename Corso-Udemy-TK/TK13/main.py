import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

text = tk.Text(app)
text.pack()

text.insert(tk.END, "Nel mezzo del cammin\n")
text.insert(tk.END, "di nostra vita\n")
text.insert(tk.END, "mi ritrovai...\n")

str = text.get("2.3", "2.10")
print(str)
text.delete('3.8', '3.12')

text.tag_config("mark", background="yellow", foreground="red")
text.tag_add("mark", "1.0", "1.3")

'''
• width, height –definiscono le sue dimensioni e sono espresse in pixel.
• background – il colore dello sfondo;
• foreground – per il colore del testo;
• font – per modificare il tipo di caratteri utilizzati;
• cursor – per specificare il tipo di cursore da utilizzare quando il componente è attivo.
• state – per abilitare (‘normal’, ‘active’) o disabilitare (‘disabled’) il componente.
'''

app.mainloop()