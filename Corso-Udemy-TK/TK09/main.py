import tkinter as tk

app = tk.Tk()
app.geometry("400x300")
app.title("app con immagine")

photo = tk.PhotoImage(file="cat.png")

label = tk.Label(app)
label["image"] = photo
label["text"] = "un gatto"
label["compound"] = "top"
label.pack()

app.mainloop()