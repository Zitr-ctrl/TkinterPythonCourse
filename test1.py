import tkinter as tk

window = tk.Tk()

# Titulo de la ventana
window.title("Este es mi titutlo de ventana")
# Tamaño de la ventana
window.geometry("500x300+600+350")

#label = tk.Label(text= "Hola mundo¡", background="red", foreground="white", font=("Arial", 20, "bold"), cursor="hand2")
#label.pack()

# widget text
#text = tk.Text(window);
#text.config(width=25, height=10, background="black", foreground="white", font=("Arial", 12, "bold"), padx=10, pady=10, selectbackground="blue", selectforeground="white", cursor="arrow");
#text.pack();

# Función para insertar texto en el widget Text

text = tk.Text(window, width=50, height=15)
text.pack();

count = 1

def insert_text():
    global count
    text.insert(tk.END, f"¡Linea {count}¡\n")
    count += 1
    
# Botón para insertar texto
insert_button = tk.Button(window, text="Insertar texto", command=insert_text)
insert_button.pack()

window.mainloop()