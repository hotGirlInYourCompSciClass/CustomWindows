import tkinter as tk

def run_good_girl(master_root):
    winWidth = 900
    winHeight = 150

    m = tk.Toplevel(master_root)
    m.title("good girl!!")
    m.geometry(f"{winWidth}x{winHeight}+{int((master_root.winfo_screenwidth() - winWidth) / 2)}+{int((master_root.winfo_screenheight() - winHeight) / 2)}")
    m.configure(bg="orchid3")
    m.attributes("-topmost", True)
    m.overrideredirect(True)

    lbl = tk.Label(m, text="Good girl!!!!!!", font=("Arial", 100, "bold"), bg="orchid3", fg="black")
    lbl.pack()

root = tk.Tk()
root.withdraw()
run_good_girl(root)