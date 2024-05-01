import tkinter as tk

def btclic(tbox):
    txt = tbox.get()
    print(txt)

app = tk.Tk()
app.geometry("300x200")

label1 = tk.Label(app, text="Name: ", bg='#c7f9ff')
label1.place(x=10, y=10)
#tk.Entry(app, bg='#fdffc7').place(x=90, y=10)
name_entry = tk.Entry(app, bg='#fdffc7')
name_entry.place(x=90, y=10)

tk.Label(app, text="Password: ", bg='#d3ffc7').place(x=10, y=40)
tk.Entry(app, bg='#fdffc7').place(x=90, y=40)

tk.Button(app, text="Login", command=lambda: btclic(name_entry) ).place(x=90, y=70)

app.mainloop()