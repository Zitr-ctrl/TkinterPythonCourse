import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Redimensionar ventana")
window.geometry("300x200")

sizegrip = ttk.Sizegrip(window)
sizegrip.place(relx=1.0, rely=1.0, anchor="se")

window.mainloop()