import tkinter as tk
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.withdraw()
        splash = Splash(self)
        time.sleep(2)
        splash.destroy()
        self.deiconify()

        self.title("Python Paint")
        self.geometry('300x200')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=20)
        self.rowconfigure(1, weight=80)

        toolbar = tk.Frame(self)
        toolbar.grid(row=0, column=0, sticky='nsew')
        tk.Button(toolbar, text="+", command=self.plusSize).pack(side=tk.LEFT, padx=1)
        tk.Button(toolbar, text="-", command=self.minusSize).pack(side=tk.LEFT, padx=1)

        self.canva = tk.Canvas(self, bg='white')
        self.canva.grid(row=1, column=0, sticky='nsew')

        self.canva.bind('<B1-Motion>', self.draw)
        self.canva.bind('<ButtonRelease-1>', self.stopDraw)

        self.px = None
        self.py = None

        self.size = 2


    def plusSize(self):
        self.size += 1

    def minusSize(self):
        self.size -= 1
        if self.size < 1:
            self.size = 1

    def draw(self, event):
        if self.px and self.py:
            self.canva.create_line(event.x, event.y, self.px, self.py, fill='black', width=self.size)
        self.px = event.x
        self.py = event.y

    def stopDraw(self, event):
        self.px = None
        self.py = None


class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.geometry("200x200")
        img = tk.PhotoImage(file="splash.png")
        lab = tk.Label(self, image=img)
        lab.pack()
        self.update()


if __name__ == '__main__':
    app = App()
    app.mainloop()