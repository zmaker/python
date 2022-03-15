import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

label = [['7','8','9'],['5','6','7'],['1','2','3'],['0','+','=']]

display = tk.Entry(app)
display.grid(row = 0, column = 0, columnspan=3)

for rw in range(4):
    app.rowconfigure(rw+1, weight=1)
    for cl in range(3):
        app.columnconfigure(cl, weight=1)
        f = tk.Frame(app)
        f.grid(row=rw+1, column=cl)
        bt = tk.Button(f, text=label[rw][cl])
        bt.pack()


app.mainloop()