# importar tkinter
import tkinter as tk

window = tk.Tk()
window.title("Mi ventaana en tkinter") 
window.geometry("500x300+600+350")

# Widget Text
text = tk.Text(window, width=50, height=15)
text.pack()

def modify_selection():
    new_text = "Texto modificado"
    text.replace("sel.first", "sel.last", new_text)
    
# Botón para llamar a la función de obtención de texto
button_modify_selection = tk.Button(window, text="Modificar Seleccion", command=modify_selection)
button_modify_selection.pack()

window.mainloop()