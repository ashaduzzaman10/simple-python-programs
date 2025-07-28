# utils 
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Simple Digital Clock")

# setup clock 
def showTime():
    current_time = strftime("%H:%M:%S %p\n%D")
    label.config(text=current_time)
    label.after(1000, showTime)


label = tk.Label(
    root,
    font=("Cascadia Code", 50, "bold"),
    background="Gray",
    foreground="white",
)
label.pack(anchor="center")

showTime()
root.mainloop()
