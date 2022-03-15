import tkinter as tk

app = tk.Tk()
app.geometry("300x200")

fr1 = tk.Frame(app, background="yellow")
fr1.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

b1 = tk.Button(fr1, text="BT1").pack(side=tk.LEFT)
b2 = tk.Button(fr1, text="BT2").pack(side=tk.LEFT)
b3 = tk.Button(fr1, text="BT3").pack(side=tk.LEFT)

fr2 = tk.Frame(app, background='#c7f9ff')
fr2.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

b4 = tk.Button(fr2, text="BT4").pack(side=tk.LEFT)




app.mainloop()