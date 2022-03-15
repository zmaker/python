import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('inch converter App')
        self.geometry('300x200')
        frame = MainFrame(self)

class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=2)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        tk.Label(self, text="Convertitore inch/cm").grid(row=0, column=0, columnspan=4)

        tk.Label(self, text="inch:").grid(row=1, column=0)
        tk.Label(self, text="cm:").grid(row=1, column=2)

        self.vInch = tk.StringVar()
        self.eInch = tk.Entry(self, width=5)
        self.eInch.grid(row=1, column=1)
        self.eInch['textvariable'] = self.vInch
        self.eInch.focus()

        self.vCm = tk.StringVar()
        self.eCm = tk.Entry(self, width=5)
        self.eCm.grid(row=1, column=3)
        self.eCm['textvariable'] = self.vCm

        self.bt1 = tk.Button(self, text="inch->cm")
        self.bt1['command'] = self.inch2cm
        self.bt1.grid(row=2, column=0, columnspan=2)

        self.bt2 = tk.Button(self, text="cm->inch")
        self.bt2['command'] = self.cm2inch
        self.bt2.grid(row=2, column=2, columnspan=2)


        self.pack()
        self.logic = Logic()

    def inch2cm(self):
        self.vCm.set(self.logic.inch2cm(self.vInch.get()))

    def cm2inch(self):
        self.vInch.set(self.logic.cm2inch(self.vCm.get()))

class Logic():
    def inch2cm(self, inch):
        n = 0
        try:
            n = float(inch) * 2.54
        except:
            n = 0

        return "{:.1f}".format(n)

    def cm2inch(self, cm):
        n = 0
        try:
            n = float(cm) / 2.54
        except:
            n = 0

        return "{:.1f}".format(n)



if __name__ == "__main__":
    app = App()
    app.mainloop()