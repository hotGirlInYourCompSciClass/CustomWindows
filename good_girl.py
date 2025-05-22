import tkinter as tk
from random import randint

def run_good_girl(master_root):
    winWidth = 900
    winHeight = 150

    m = tk.Toplevel(master_root)
    m.title("good girl!!")
    m.geometry(f"{winWidth}x{winHeight}+{int((master_root.winfo_screenwidth() - winWidth) / 2)}+{int((master_root.winfo_screenheight() - winHeight) / 2)}")
    m.configure(bg="orchid3")
    m.attributes("-topmost", True)
    m.overrideredirect(True)
    m.withdraw()
    lbl = tk.Label(m, text="Good girl!!!!!!", font=("Arial", 100, "bold"), bg="orchid3", fg="black")
    lbl.pack()
    def loop():
        nonlocal m
        m.deiconify()
        wait = randint(300000, 600000)
        m.after(5000, lambda: m.withdraw())
        m.after(wait, loop)
    loop()

