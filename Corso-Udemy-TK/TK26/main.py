import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OOP Template2")
        self.geometry("300x200")

        f = MainFrame(self)

class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self["background"] = "yellow"
        self.label = tk.Label(self, text="Frame")
        self.label.pack()

        self.pack(fill=tk.BOTH, expand=True)



if __name__ == "__main__":
    app = App()
    app.mainloop()