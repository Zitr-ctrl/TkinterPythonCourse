import tkinter as tk

window = tk.Tk()
window.title("Mouse Events")
window.geometry("500x100")

# Event
def mouse_movements(event):
    print("Mouse moved to", event.x, event.y)
    
window.bind("<Motion>", mouse_movements)

# Label to display mouse position
label = tk.Label(window, text="Move the mouse over the window")
label.pack()

window.mainloop()
