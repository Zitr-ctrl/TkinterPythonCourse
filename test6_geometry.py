import tkinter as tk

window = tk.Tk()
window.title("Hola Mundo XD")

# Configurar dimensiones de ventana

width = 400
height = 75

width1 = window.winfo_screenwidth()
height1 = window.winfo_screenheight()

print(f"Ancho de la pantalla: {width1}")
print(f"Alto de la pantalla: {height1}")

#Posicion de la ventana
position_x = 400
position_y = 700

position_x1 = round((width1 // 2) - (width // 2))
position_y1 = round((height1 // 2) - (height // 2))

window.geometry(f"{width}x{height}+{position_x1}+{position_y1}")

# Impide la redimensión de la ventana
window.resizable(False, False)

# Estado de la ventana
# normal, iconic, zoomed, withdrawn
window.wm_state("iconic")

window.mainloop()