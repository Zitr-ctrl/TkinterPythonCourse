import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Window")
window.geometry("700x400")

paned_window = tk.PanedWindow(window, orient="horizontal")
paned_window.pack(fill=tk.BOTH, expand=True)

frame1 = tk.Frame(paned_window, bd=2, relief="solid", padx=5, pady=5)
frame2 = tk.Frame(paned_window, bd=2, relief="solid", padx=5, pady=5)

paned_window.add(frame1)
paned_window.add(frame2)

# Dividir el espacio de forma equitativa
paned_window.paneconfig(frame1, minsize=350)
paned_window.paneconfig(frame2, minsize=350)

# Etiquetas dentro del primer marco
element1 = tk.Label(frame1, text="Etiqueta 1", bg="gold")
element2 = tk.Label(frame1, text="Etiqueta 2", bg="lightblue")
element3 = tk.Label(frame1, text="Etiqueta 3", bg="lightgreen")
element4 = tk.Label(frame1, text="Etiqueta 4", bg="lightcoral")

# Etiqueta dentro del segundo marco
element5 = tk.Label(frame2, text="Etiqueta 5", bg="lightblue")
element6 = tk.Label(frame2, text="Etiqueta 6", bg="lightpink")
element7 = tk.Label(frame2, text="Etiqueta 7", bg="lightyellow")
element8 = tk.Label(frame2, text="Etiqueta 8", bg="lightgray")

# Colocar las etiquetas en el primer marco usando grid
element1.grid(row=0, column=0, sticky="nsew")
element2.grid(row=0, column=1, sticky="nsew")
element3.grid(row=1, column=0, sticky="nsew")
element4.grid(row=1, column=1, sticky="nsew")

# Configurar el grid del primer marco
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_rowconfigure(1, weight=1)
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)

# Colocar las etiquetas en el segundo marco usando pack
element5.pack(fill='both', expand=True)
element6.pack(fill='both', expand=True)
element7.pack(fill='both', expand=True)
element8.pack(fill='both', expand=True)

window.mainloop()