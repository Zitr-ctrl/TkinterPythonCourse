import tkinter as tk 

window = tk.Tk()
window.title("Hola Mundo")
window.geometry("500x500")

window_second = tk.Toplevel()
window_second.title("Ventana Secundaria")
window_second.geometry("300x200")

window_second.configure(bg="lightblue")

tk.Label(window, text="Etiqueta Principal").pack()

tk.Label(window_second, text="Etiqueta Secundaria", bg="lightblue").pack()

btn_close = tk.Button(window, text="Cerrar", command=window_second.destroy)
btn_close.pack()

window.mainloop()