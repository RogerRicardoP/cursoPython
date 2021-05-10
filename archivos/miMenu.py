from tkinter import *
root = Tk()
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
archivoHelp = Menu(barraMenu)

barraMenu.add_cascade(label="Archivo", menu = archivoMenu)
barraMenu.add_cascade(label="Edicion", menu = archivoEdicion)
barraMenu.add_cascade(label="Tools", menu = archivoTools)
barraMenu.add_cascade(label="Help", menu = archivoHelp)




root.mainloop()