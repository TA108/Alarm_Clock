import tkinter as tk
from tkinter import messagebox
import threading
from alarm import start_alarm

def set_alarm():
    alarm_time = f"{hour_var.get()}:{minute_var.get()}"
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    threading.Thread(target=start_alarm, args=(alarm_time,), daemon=True).start()

root = tk.Tk()
root.title("Simple Alarm Clock")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Enter time in 24-hour format:").pack(pady=5)
tk.Label(root, text="Hour   Minute").pack()

hour_var = tk.StringVar()
minute_var = tk.StringVar()

hour_entry = tk.Entry(root, textvariable=hour_var, width=5)
hour_entry.pack(side=tk.LEFT, padx=10)
minute_entry = tk.Entry(root, textvariable=minute_var, width=5)
minute_entry.pack(side=tk.LEFT)

set_button = tk.Button(root, text="Set Alarm", command=set_alarm, fg="red")
set_button.pack(pady=20)

root.mainloop()
