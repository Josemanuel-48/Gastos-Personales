# importamos modulo
import sqlite3
# conectamos con la base.
conn = sqlite3.connect("Gastos_Personales.db")
# se crea un cursor, objeto encargado de ejecutar consultas sql.
cursor = conn.cursor()
# se crea la tabla, sino exixte la crea.
cursor.execute("""
        CREATE TABLE IF NOT EXISTS Gastos_Personales(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            fecha TEXT NOT NULL, 
            sitio TEXT NOT NULL,  
            categoria TEXT NOT NULL,
            cantidad REAL  
    )
""")
# creamos funcion datos.
def datos():
    fecha = (input("Fecha: "))
    sitio = input("lugar de gasto: ")
    categoria = input("Escribe la categoria: ")
    cantidad = float(input("Cuánto ha costado (€): "))
    print("Gasto Añadido!!!")
    # insertamos registros en la tabla.
    cursor.execute(
        "INSERT INTO Gastos_Personales(fecha, sitio, categoria, cantidad) VALUES(?, ?, ?, ?)", (fecha, sitio, categoria, cantidad)
    )
    # confirmamos cambios.
    conn.commit()
   
# se crea funcion.
def ver_gastos():
    # "SELECT * Selecciona todas las columnas de la tabla. FROM Gastos_Personales: Indica que los datos provienen de la tabla de gastos personales. 
    cursor.execute("SELECT * FROM Gastos_Personales")
    # fetchall() recoge todos los resultados que devuelve la consulta SQL anterior y los guarda como una lista de tuplas.
    resultado = cursor.fetchall()
    # recorremos la lista.
    for r in resultado:
        print(r)
# se crea funcion.
def categoria_gasto():
    # GROUP BY categoria agrupa todos los registros que tengan la misma categoría y SUM(cantidad) suma el dinero de cada grupo.
    cursor.execute("SELECT categoria, SUM(cantidad) FROM Gastos_Personales GROUP BY categoria")
    # recogemos los resultados de la consulta y los guardamos como una tupla.
    total = cursor.fetchall()
    # recorremos la lista
    for i in total:
        print(i)
# se crea funcion.
def ver_total():
    # se suma la cantidad a los gastos personales. 
    cursor.execute("SELECT SUM(cantidad)  FROM Gastos_Personales")
    # recogemos los resultados de la consulta y los guardamos como una tupla.
    total = cursor.fetchall()
    # recorremos lista.
    for x in total:
        print(x)
# se crea funcion
def borrar_gasto():
    # ceamos variable para preguntar.
    usuario = input("Que id quiere borrar: ")
    # borramos el id que pida el usuario de la tabla y WHERE id=?(pero solo la fila cuyo id coincida con el ?)
    cursor.execute("DELETE FROM Gastos_Personales WHERE id=?", (usuario,))
    # confirmamos cambios.
    conn.commit()
    print("Registro Eliminado!!!!")

# se crea funcion.
def menu():
    # hacenos un bucle.
    while True:
        # se crea menu.
        print("==========================")
        print("---GASTOS PERSONALES---")
        print("==========================")
        print("1. Añadir gasto: ")
        print("2. Ver Gastos: ")
        print("3. Categoria Gastos: ")
        print("4. Ver Total: ")
        print("5. Borrar Gasto: ")
        print("6. Salir")
        # se crea variable para pedir las opciones.
        opcion = int(input("Escoge una opcion: "))
        # le decimos lo que tiene que hacer cundo pongas la opcion correspondiente.
        if opcion == 1:
            datos()
        elif opcion == 2:
            ver_gastos()
        elif opcion == 3:
            categoria_gasto()
        elif opcion == 4:
            ver_total()
        elif opcion == 5:
            borrar_gasto()
        else:
            break  # ---> se para el bucle.
# llamamos al menu.
menu()
# cerramos la conexion.
conn.close()
