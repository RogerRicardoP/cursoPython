from tkinter import *
miRoot=Tk()
miFrame=Frame(miRoot, width=1200, height=600)
miFrame.pack()
miEntry=Entry(miFrame)
miEntry.grid(row=0, column=1,sticky="w")
miLabel=Label(miFrame, text="Nombre : ")
miLabel.grid(row=0, column=0, sticky="e")
miEntry1=Entry(miFrame)
miEntry1.grid(row=1, column=1,sticky="w")
miLabel1=Label(miFrame, text="Apellido : ")
miLabel1.grid(row=1, column=0, sticky="e")
miEntry2=Entry(miFrame)
miEntry2.grid(row=2, column=1,sticky="w")
miLabe2=Label(miFrame, text="Dirección Real : ")
miLabe2.grid(row=2, column=0, sticky="e")
miText=Text(miFrame, width=35, height=10)
miText.grid(row=3, column=1,sticky="w")
miLabel3=Label(miFrame, text="Comentario : ")
miLabel3.grid(row=3, column=0, sticky="e")
miScrollVertical=Scrollbar(miFrame, command=miText.yview)
miScrollVertical.grid(row=3, column=2, sticky="nsew")
miText.config(yscrollcommand=miScrollVertical.set)

miRoot.mainloop()

//
//