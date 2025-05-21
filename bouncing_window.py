import tkinter as tk
from screeninfo import get_monitors
import sounddevice as sd
import soundfile as sf
import os
from random import randint
import time

def run_bouncing_window(master_root):
    # AUDIO
    cornerpath = 'sounds/airhorn.wav'
    booppath = 'sounds/boop.wav'

    if not os.path.isfile(booppath):
        raise FileNotFoundError(f"Audio file not found: {booppath}")
    boopdata, boopsamplerate = sf.read(booppath)
    if not os.path.isfile(cornerpath):
        raise FileNotFoundError(f"Audio file not found: {cornerpath}")
    cornerdata, cornersamplerate = sf.read(cornerpath)

    device = 67

    # MONITOR
    monitor = get_monitors()[0]
    monitor_x = monitor.x
    monitor_y = monitor.y
    screen_width = monitor.width
    screen_height = monitor.height

    # CONFIG
    wh = 100
    startx = randint(monitor_x + 2 * wh, monitor_x + screen_width - 2 * wh)
    starty = randint(monitor_y + 2 * wh, monitor_y + screen_height - 2 * wh)
    possx = startx
    possy = starty
    move_x = 2
    move_y = 2

    # NEW WINDOW
    m = tk.Toplevel(master_root)  # instead of Tk(), we create a child window
    m.title("freddy")
    m.geometry(f"{wh}x{wh}")
    m.configure(bg="black")
    m.attributes("-topmost", True)

    # Load image and make sure it persists
    photo = tk.PhotoImage(file="images/freddyPlush.png", master=master_root)
    m.photo = photo  # Store image ref on the window

    def cornerhit():
        sd.play(cornerdata, cornersamplerate, device=device)

    def buttonpress():
        sd.play(boopdata, boopsamplerate, device=device)

    speed = 100  # pixels per second
    last_time = time.time()

    def move_window():
        nonlocal possx, possy, move_x, move_y, last_time

        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        dx = move_x * speed * dt
        dy = move_y * speed * dt

        possx += int(dx)
        possy += int(dy)

        # Corner hit detection
        if (
            (possx <= monitor_x and possy <= monitor_y) or
            (possx + wh >= monitor_x + screen_width and possy <= monitor_y) or
            (possx <= monitor_x and possy + wh >= monitor_y + screen_height) or
            (possx + wh >= monitor_x + screen_width and possy + wh >= monitor_y + screen_height)
        ):
            cornerhit()

        # Bounce logic
        if possx + 7 <= monitor_x or possx + wh + 22 >= monitor_x + screen_width:
            move_x = -move_x
        if possy <= monitor_y or possy + wh + 70 >= monitor_y + screen_height:
            move_y = -move_y

        m.geometry(f"{wh}x{wh}+{possx}+{possy}")
        m.after(10, move_window)


    move_window()

    # Create the button with the persistent image
    cornerBtn = tk.Button(m, image=photo, command=buttonpress, width=int(wh * 1.2), height=wh)
    cornerBtn.pack()
