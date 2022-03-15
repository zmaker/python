import tkinter as tk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OOP App")
        self.geometry("300x200")

        self.label = tk.Label(self, text="OOP App!")
        self.label.pack()

        self.bt = tk.Button(self, text="Clic")
        self.bt["command"] = self.button_clicked
        self.bt.pack()

    def button_clicked(self):
        showinfo(title="Info", message="Hello!")

if __name__ == "__main__":
    app = App()
    app.mainloop()