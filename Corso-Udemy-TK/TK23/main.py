import tkinter as tk

def azione(nome):
    print("ciao", nome)

app = tk.Tk()
app.geometry("300x200")

add = lambda x: x + 1
n = add(2)
print(n)

nome = "Paolo"

bt = tk.Button(app, text="clic", command=lambda a=nome:azione(a) )
bt.pack()

app.mainloop()