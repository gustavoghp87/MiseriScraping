import tkinter as tk
from tkinter import *

root = tk.Tk()

#myLabel = Label(root, text="Hello world!")
#myLabel.pack()            # tamaño mínimo necesario

#myLabel1 = Label(root, text="Ancho de columna se ajusta").grid(row=0, column=0)      # pack Vs grid
#myLabel2 = Label(root, text="Siempre centrado")
#myLabel2.grid(row=1, column=0)       # para separar columnas se crea una columna intermedia con texto de espacios


e = Entry(root, width=50, bg="white", fg="black", borderwidth=5)
#e.pack()
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.get()
e.insert(0, "Ingresa algo")
#e.delete(0, END)   borra todo

def myClick(param):
	variable = "! " + param
	#myLabel = Label(root, text="Se van a rastrillar 100 direcciones")
	myLabel = Label(root, text="Ingresado: " + e.get() + " " + variable)   # la etiqueta desplegada muestra el texto ingresado en el input e
	#myLabel.pack()
	myLabel.grid(row=3,column=1)

var2 = "ggg"
#myButton = Button(root, text="Botoncito", padx=50)
#myButton = Button(root, text="Botoncito", padx=50, pady=20, command=myClick, fg="red")    # también hexadecimales
myButton = Button(root, text="Botoncito", padx=50, pady=20, command=lambda: myClick(var2))
#myButton.pack()
myButton.grid(row=2, column=2)

# columnspan=n° hace que el elemento ocupe varias columnas
# boton.grid(row=5, column=3, columnspan=2)  significa que este botón va en la fila 5 y columnas 3 y 4

# pasar parámetros: no se usa command:función sino  command=lambda:función(params)

root.mainloop()

# sigue 1:18



#root = tk.Tk()
#root.config(width=350, height=330)
#root.title("MiseriScraping")
#frame = tk.Frame(root)
#frame.place(x=8, y=8, width=340, height=330)


#textbox = tk.Entry(frame)
#textbox.insert(0, "Calle")
#textbox.place(x=50, y=20)

#textbox = tk.Entry(frame)
#textbox.insert(0, "Altura mín")
#textbox.place(x=50, y=60)

#textbox = tk.Entry(frame)
#textbox.insert(0, "Altura máx")
#textbox.place(x=50, y=100)

#checkbox = ttk.Checkbutton(frame, text="Pares")
#checkbox.place(x=220, y=40)
#checkbox = ttk.Checkbutton(frame, text="Impares")
#checkbox.place(x=220, y=80)

#textbox = tk.Entry(frame)
#textbox.insert(0, "Jurisdicción")
#textbox.place(x=50, y=140)

#textbox = tk.Entry(frame)
#textbox.insert(0, "CP (opcional)")
#textbox.place(x=50, y=180)

#button = tk.Button(frame, text="Scrapear!")
#button.place(x=220, y=140)

#root.mainloop()
