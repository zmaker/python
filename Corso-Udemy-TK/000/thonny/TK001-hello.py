import tkinter as tk

app = tk.Tk()
app.title("La mia prima App")
app.geometry("300x200")

label = tk.Label(text="hello!")
label.pack()

app.mainloop()
print("fine")