import tkinter
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("snomed.db")

# Crear la ventana
window = tkinter.Tk()
window.title("Lector de SNOMED CT")
window.geometry("800x600")

# Crear el OptionMenu
options = ["Otro", "Medicación ANMAT", "Medicación Genérica", "Observación", "Diagnóstico", "Alergia", "Intolerancia", "Alergia/Intolerancia (Sustancia)", "Procedimiento"]
option = tkinter.StringVar(window)
option.set(options[0])
option_menu = tkinter.OptionMenu(window, option, *options)
option_menu.pack()

# Crear el entry
entry = tkinter.Entry(window)
entry.pack()

# Crear el botón
def button_click():
    print("Botón presionado")
    print("Opción elegida:", option.get())
    print("Texto ingresado:", entry.get())
    return None

button = tkinter.Button(window, text="Buscar", command=button_click)
button.pack()


# mostrar ventana
window.mainloop()