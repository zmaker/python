import tkinter as tk
from datetime import datetime

tm = datetime.now()
print(tm.hour)
#tm.minute
#tm.second
#tm.day
#tm.month
#tm.year


def btclic():
    txt = msg.get()
    lb["text"] = "Ciao, " + txt

def btclear():
    msg.delete(0, tk.END)

app = tk.Tk()
app.title("Saluto personalizzato")
app.geometry("300x200")

bt = tk.Button(text="Vuoi un saluto?", command=btclic)
bt.pack()

msg = tk.Entry()
msg.pack()

lb = tk.Label(text="...")
lb.pack()

btc = tk.Button(text="Clear", command=btclear)
btc.pack()


app.mainloop()