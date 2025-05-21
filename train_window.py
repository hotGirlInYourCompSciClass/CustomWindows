import tkinter as tk
import sounddevice as sd
import soundfile as sf
import os
from random import randint
from PIL import Image, ImageTk
import time
import numpy as np
import numpy as np
import threading

def play_sound(hornpath):
    if not os.path.isfile(hornpath):
        raise FileNotFoundError(f"Audio file not found: {hornpath}")
    
    horndata, hornsamplerate = sf.read(hornpath)
    horndata = horndata.astype(np.float32)

    def play():
        try:
            with sd.OutputStream(
                samplerate=hornsamplerate,
                channels=horndata.shape[1] if horndata.ndim > 1 else 1,
                dtype='float32',
                device=67
            ) as stream:
                stream.write(horndata)
        except Exception as e:
            print(f"Error playing sound stream: {e}")

    threading.Thread(target=play, daemon=True).start()




def run_train(master_root):
    hornpath = 'sounds/trainhorn.wav'
    screen_width = master_root.winfo_screenwidth()
    screen_height = master_root.winfo_screenheight()

    window_width = int(screen_width * 2)
    window_height = int(screen_height * 0.5)
    y_offset = int(screen_height * 0.25)

    # Load and scale images
    def load_scaled_image(path):
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Image not found: {path}")
        img = Image.open(path)
        img = img.resize((window_width, window_height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    train_front_img = load_scaled_image("images/trainFront.png")
    train_back_img = load_scaled_image("images/trainBack.png")

    # Front window
    frontWin = tk.Toplevel(master_root)
    frontWin.attributes("-topmost", True)
    frontWin.overrideredirect(True)
    frontWin.configure(bg="black")
    frontWin.geometry(f"{window_width}x{window_height}+-1000+{y_offset}")
    frontWin.withdraw()
    front_label = tk.Label(frontWin, image=train_front_img, bg="white")
    front_label.pack()

    # Back window
    backWin = tk.Toplevel(master_root)
    backWin.attributes("-topmost", True)
    backWin.overrideredirect(True)
    backWin.configure(bg="black")
    backWin.geometry(f"{window_width}x{window_height}+-1000+{y_offset}")
    backWin.withdraw()
    back_label = tk.Label(backWin, image=train_back_img, bg="white")
    back_label.pack()

    speed = 1500
    last_time = time.time()
    x_pos = -window_width - 4000

    def move_windows():
        nonlocal x_pos, last_time

        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        dx = speed * dt
        x_pos += dx

        if x_pos < 2.2 * screen_width + window_width:
            # show and move
            frontWin.deiconify()
            backWin.deiconify()
            frontWin.geometry(f"{window_width}x{window_height}+{int(x_pos)}+{y_offset}")
            backWin.geometry(f"{window_width}x{window_height}+{int(x_pos) - window_width - 100}+{y_offset}")
            master_root.after(10, move_windows)
        else:
            frontWin.withdraw()
            backWin.withdraw()
            schedule_next_run()


    def trigger_crossing():
        nonlocal x_pos, last_time
        x_pos = -window_width - 4000
        last_time = time.time()
        frontWin.withdraw()
        backWin.withdraw()
        play_sound(hornpath)
        master_root.after(3000, move_windows)



    def schedule_next_run():
        delay_minutes = randint(10, 60)
        delay_ms = delay_minutes * 60 * 1000
        master_root.after(delay_ms, trigger_crossing)
    
    trigger_crossing()

    # Prevent image GC
    frontWin.image = train_front_img
    backWin.image = train_back_img

    schedule_next_run()

    
