import tkinter as tk
import time
from threading import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("No thread")
        self.geometry("300x200")

        self.button = tk.Button(self, text="Start")
        self.button["command"] = self.doWork
        self.button.pack()

        self.txt = tk.Label(self)
        self.txt.pack()

    def doWork(self):
        self.button["state"] = 'disabled'
        t1 = Thread(target=self.work)
        t1.setDaemon(True)
        t1.start()

    def work(self):
        for i in range(10):
            self.txt["text"] = str(i)
            time.sleep(1)
        self.txt["text"] = "Finito"
        self.button["state"] = 'active'



if __name__ == "__main__":
    app = App()
    app.mainloop()
