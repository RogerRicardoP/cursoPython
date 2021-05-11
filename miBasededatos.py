import sqlite3
miConexion = sqlite3.connect("primeraBase")
miCursor = miConexion.cursor()
miCursor.execute("create table productos(nombreArticulos varchar(50), precio integer, seccion varchar(20))")
#
# 
muchosProductos=[
    ("camisetas", 20, "ropa"),
    ("canicas", 30, "juguetes"),
    ("guantes", 50, "boxeo"),
    ("copas", 32, "vajilla")
    
]
miCursor.executemany("insert into productos values (?, ?, ?)", muchosProductos)






miConexion.close()
