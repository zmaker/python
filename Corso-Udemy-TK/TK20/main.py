import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

for rw in range(3):
    app.rowconfigure(rw, weight=1, minsize=50)
    for cl in range(3):
        app.columnconfigure(cl, weight=1, minsize=50)

        fr = tk.Frame(app)
        fr.grid(row=rw, column=cl, sticky='nsew', padx=3, pady=3)

        bt = tk.Button(fr, text=f"R:{rw} \nC:{cl}")
        bt.pack(expand=True, fill=tk.BOTH)

app.mainloop()