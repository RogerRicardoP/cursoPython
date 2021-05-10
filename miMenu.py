from tkinter import messagebox
from tkinter import *


root = Tk()

def infoAbout():
    messagebox.showinfo("Word processor", "Text Processor, RPKSystms INC, version 2.21.1")

def infoLicencia():
    messagebox.showwarning("LICENCIA", "Producto bajo licencia GNU")
barraMenu = Menu(root)
root.config(menu = barraMenu, width=300, height = 300)


archivoMenu = Menu(barraMenu,tearoff = 0)
archivoMenu.add_command(label = "Nuevo")
archivoMenu.add_command(label = "Abrir")
archivoMenu.add_command(label = "Guardar")
archivoMenu.add_command(label = "Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir")





archivoEdicion = Menu(barraMenu, tearoff = 0)
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Pegar")
archivoEdicion.add_command(label = "Cortar")
archivoTools = Menu(barraMenu)
archivoHelp = Menu(barraMenu, tearoff = 0)

barraMenu.add_cascade(label="Archivo", menu = archivoMenu)
barraMenu.add_cascade(label="Edicion", menu = archivoEdicion)
barraMenu.add_cascade(label="Tools", menu = archivoTools)
barraMenu.add_cascade(label="Help", menu = archivoHelp)
archivoHelp.add_command(label = "Licencia", command = infoLicencia)
archivoHelp.add_command(label = "Abuot..", command = infoAbout)



root.mainloop()