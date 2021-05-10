from tkinter import *
root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miImagen=PhotoImage("new-testcase.gif")
miLabel=Label(miFrame, image=miImagen)
miLabel.place(x=50 , y=60)
root.mainloop()      