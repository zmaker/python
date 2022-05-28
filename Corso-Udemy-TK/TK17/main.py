import tkinter as tk

app = tk.Tk()
app.geometry("300x200")
app.title('Pack')

lab = tk.Label(app)
lab['text'] = 'Come funziona pack()?'
lab['background'] = '#fdffc7'
lab.pack()

ent = tk.Entry(app)
ent['background'] = '#c7f9ff'
ent.pack()

bt = tk.Button(app)
bt['background'] = '#d3ffc7'
bt['text'] = 'Cliccami'
bt.pack()

app.mainloop()

