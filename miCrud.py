import sqlite3
miConexion = sqlite3.connect("gestionProductos")
miCursor = miConexion.cursor()
miCursor.execute("select * from productos where seccion ='boxeo'")
dataProductos=miCursor.fetchall()
print(dataProductos)

#miCursor.execute('''
#create table productos(
#id integer primary key autoincrement,
#nombreArticulos varchar(50) unique, 
#precio integer, 
#seccion varchar(20))
#''')
#
# 
#muchosProductos=[
#    ("camisetas", 20, "ropa"),
#    ("canicas", 30, "juguetes"),
#    ("guantes", 50, "boxeo"),
#    ("copas", 32, "vajilla"),
#    ("Destornillador", 45, "Ferretria")
#    
#]
#miCursor.executemany("insert into productos values (null, ?, ?, ?)", muchosProductos)
miConexion.commit()




miConexion.close()
