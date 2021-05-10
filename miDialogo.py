from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title = "Open", initialdir="C:", filetype=(("Archivos de Excel","*.xlsx"), ("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")))
    
    print(fichero)

Button (root, text = "Abrir Archivos", command = abreFichero).pack()

root.mainloop()