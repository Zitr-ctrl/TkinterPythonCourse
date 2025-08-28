import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("My Tkinter Window")
window.geometry("500x200")

# Mensaje informativo
#messagebox.showinfo("Información Importante", "Este es un mensaje de información.")
#messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")
#messagebox.showerror("Error", "Este es un mensaje de error.")

response = messagebox.askyesno("Pregunta", "¿Quieres continuar?")

if response:
    print("Se pulso el boton Si")
    print(response)
else:
    print("Se pulso el boton No")
    print(response)

window.mainloop()