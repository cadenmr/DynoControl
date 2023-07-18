import tkinter as tk

class MainWindow(tk.Tk):

    def __init__(self, dataQueue):
        super().__init__()

        self.dataQueue = dataQueue

        self.title("Caden's Super Awesome And Totally Not Dangerous Engine Dyno")
        self.geometry('800x600')

        self.text = tk.StringVar()
        self.text.set("no data")

        self.lbl = tk.Label(self, textvariable=self.text)
        self.lbl.pack()

    def start(self):
        self.after(0, self.updater)
        self.mainloop()

    def updater(self):
        self.text.set(self.dataQueue.get())
        self.after(0, self.updater)