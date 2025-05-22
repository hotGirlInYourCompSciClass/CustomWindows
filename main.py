import tkinter as tk
from train_window import run_train
from bouncing_window import run_bouncing_window
from good_girl import run_good_girl

root = tk.Tk()
root.withdraw()


run_bouncing_window(root)
run_train(root)
run_good_girl(root)

root.mainloop()



