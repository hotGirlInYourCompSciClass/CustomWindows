import tkinter as tk

def run_good_girl():
    winWidth = 300
    winHeight = 300

    m = tk.Toplevel(master_root)
    m.title("good girl!!")
    m.geometry(f"winWidthxwinHeight")
    m.configure(bg="orchid3")
    m.attributes("-topmost", True)



run_good_girl()