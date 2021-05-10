from tkinter import *
root=Tk()
root.title("mi CheckButton")
playa=IntVar()
montana=IntVar()
cataratas=IntVar()

def opcionesViaje():
        opcionEscogida=""
        if (playa.get()==1):
            opcionEscogida+=" Playa"   
        if (montana.get()==1):
            opcionEscogida+=" Montaña"  
        if (cataratas.get()==1):
            opcionEscogida+=" Cataratas"  
            textoFinal.config(text=opcionEscogida)     
    

foto=PhotoImage(file="archivos/claro.png")
Label(root, image=foto).pack()
frame=Frame(root)
frame.pack()
Label(frame, text="Elige un Destino de viaje", width=80).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Cataratas", variable=cataratas, onvalue=1, offvalue=0, command=opcionesViaje).pack()
textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()




