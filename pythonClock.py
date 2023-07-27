import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    root.after(1000, update_time) 

def open_clock_window():
    clock_window = tk.Toplevel(root)
    clock_window.title("Clock")
    
    global clock_label
    clock_label = tk.Label(clock_window, font=("Helvetica", 50))
    clock_label.pack()
    
    update_time()

root = tk.Tk()
root.title("Openable Clock")

open_clock_button = tk.Button(root, text="Open Clock", command=open_clock_window)
open_clock_button.pack(pady=20)

root.mainloop()
