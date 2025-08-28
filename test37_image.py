import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Mostrar imagen con tkinter")

# Con la biblioteca Pillow podemos usar imagenes en fromato jpg, sino en tkinter solo se puede usar imagenes en png

pil_imagen = Image.open("img/r7_azul-7.jpg")
pil_imagen = ImageTk.PhotoImage(pil_imagen)

label = tk.Label(window, image=pil_imagen)
label.pack()

window.mainloop()