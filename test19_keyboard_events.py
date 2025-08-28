import tkinter as tk

window = tk.Tk()
window.title("Keyboard Events")
window.geometry("500x100")

def key_press(event):
    print("Key pressed:", event.keysym)
    
def shortcut(event):
    print("Shortcut detected")

window.bind("<KeyPress>", key_press)
window.bind("<Alt-F4>", shortcut)

label = tk.Label(window, text="Press any key")
label.pack()

window.mainloop()
