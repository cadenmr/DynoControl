import tkinter as tk
import threading, queue
from time import sleep

class UpdaterThread(threading.Thread):

    def __init__(self, q):
        super().__init__()

        self.q = q
        self.counter = 0

    def run(self):
        while True:
            self.q.put(self.counter)
            self.counter += 1
            sleep(1)

transportQueue = queue.Queue()
updater = UpdaterThread(transportQueue)

root = tk.Tk()
txt = tk.StringVar()
txt.set("none yet")
lbl = tk.Label(root, textvariable=txt)
lbl.pack()

def updateLabel(q):
    global txt

    if not q.empty():
        txt.set(q.get_nowait())

    root.after(1000, updateLabel(q))

root.after(1000, updateLabel(transportQueue))

updater.start()
root.mainloop()