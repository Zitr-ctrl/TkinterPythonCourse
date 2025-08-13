import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Window")
window.geometry("500x200")

# def double_click_left():
#     print("Left button double clicked")

# button = tk.Button(window, text="Click me", command=double_click_left)
# button.pack()

def show_info(event):
    print(f"Event type: {event.type}")
    print(f"Widget: {event.widget}")
    print(f"Char: {event.char}")
    #print(f"Keysym: {event.keysym}")
    print(f"Keycode: {event.keycode}")
    print(f"state: {event.state}")
    print(f"mouse x, y: {event.x}, {event.y}")
    print(f"screen x, y: {event.x_root}, {event.y_root}")
    print(f"Time: {event.time}")
    print(f"Number of buttons: {event.num}")
    print(f"Delta: {event.delta}")
    print("_" * 20)

window.bind("<KeyPress>", show_info)
window.bind("<ButtonPress>", show_info)
window.bind("<Motion>", show_info)
window.bind("<MouseWheel>", show_info)

window.mainloop()