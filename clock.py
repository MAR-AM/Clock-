import tkinter as tk
from time import strftime

def Updat_time() :
    time = strftime("%H:%M:%S %p")
    lbl.config(text=time)
    lbl.after(1000, Updat_time)


Time =tk.Tk()

Time.title("WHAT TIME IS IT ?")

lbl = tk.Label(Time,font=("lcd Solid",75),background="purple",foreground="white")
lbl.pack(anchor="center")
Updat_time()
Time.mainloop()