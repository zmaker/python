import  tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text editor")
        self.geometry("300x200")

        menubar = tk.Menu(self)

        filemenu = tk.Menu(menubar)
        filemenu.add_command(label="New", command=self.onNew)
        filemenu.add_command(label="Open", command=self.onOpen)
        filemenu.add_command(label="Save", command=self.onSave)
        filemenu.add_command(label="Exit", command=self.onExit)

        aboutmenu = tk.Menu(menubar)
        aboutmenu.add_command(label="About", command=self.onAbout)

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="About", menu=aboutmenu)

        self.config(menu=menubar)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)

        self.txtField = tk.Text(self)
        self.txtField.grid(column=0, row=0)
        self.txtField.focus()

    def onNew(self):
        self.txtField.delete('1.0', tk.END)

    def onOpen(self):
        fname = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All", "*.*")])
        if not fname:
            return
        self.txtField.delete('1.0', tk.END)
        with open(fname, "r") as f:
            text = f.read()
            self.txtField.insert(tk.END, text)

    def onSave(self):
        fname = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All", "*.*")])
        if not fname:
            return
        with open(fname, "w") as f:
            text = self.txtField.get('1.0', tk.END)
            f.write(text)

    def onExit(self):
        self.destroy()

    def onAbout(self):
        showinfo("simple editor", "Semplice Editor in Python")


if __name__ == '__main__':
    app = App()
    app.mainloop()