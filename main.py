import tkinter as tk
from train_window import run_train
from bouncing_window import run_bouncing_window

root = tk.Tk()
root.withdraw()

run_bouncing_window(root)
run_train(root)
#periodic good girl

root.mainloop()


