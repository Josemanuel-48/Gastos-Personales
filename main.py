# importamos modulo
import sqlite3
# conectamos con la base.
conn = sqlite3.connect("Gastos_Personales.db")
# cursor encargado de ejecutar consultas SQL.
cursor = conn.cursor()
# se crea la tabla, sino existe la crea.
cursor.execute("""
        CREATE TABLE IF NOT EXISTS Gastos_Personales(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            fecha TEXT NOT NULL, 
            sitio TEXT NOT NULL,  
            categoria TEXT NOT NULL,
            cantidad REAL  
    )
""")
# creamos funcion.
def datos():
    # se crean variables.
    fecha = (input("Fecha: "))  #  --> lo que escribe el usuario como fecha.
    sitio = input("lugar de gasto: ")   # ---> el lugar de donde se ha gastado.
    categoria = input("Escribe la categoria: ")  # ---> la categoria del gasto.
    #~lo que devuelve pedir_cantidad() ya validado como float
    cantidad = pedir_cantidad()
    print("Gasto Añadido!!!")
    # insertamos registro con los datos introducidos.
    cursor.execute(
        "INSERT INTO Gastos_Personales(fecha, sitio, categoria, cantidad) VALUES(?, ?, ?, ?)", (fecha, sitio, categoria, cantidad)
    )
    # confirmamos cambios.
    conn.commit()

def ver_gastos():
    # que seleccione todos los gastos y los ordene de menor a mayor.
    cursor.execute("SELECT * FROM Gastos_Personales ORDER BY fecha")
    # que nos devuelva el resultado en una tupla.
    resultado = cursor.fetchall()
    # si no hay resultados lo comunica.
    if not resultado:
        print("No hay gastos registrados. ")
    else:
        # si hay resultados los imprime.
        for gasto in resultado:
            id_gasto, fecha, sitio, categoria, cantidad = gasto
            print(f"ID: {id_gasto} | Fecha: {fecha} | Sitio: {sitio} | Categoria: {categoria} | Cantidad: {cantidad:.2f} €")
  

def categoria_gasto():
    # seleccionamos categoria, se suma con SUM y con GROUPY BY que los agrupe por categoria.
    cursor.execute("SELECT categoria, SUM(cantidad) FROM Gastos_Personales GROUP BY categoria")
    # devuelve resultado en tupla.
    total = cursor.fetchall()
    # recorremos total
    for i in total:
        print(i)

def ver_total():
    # se suma la cantidad de todos los gastos.
    cursor.execute("SELECT SUM(cantidad) FROM Gastos_Personales")
    # recoge un solo resultado de la suma y al especificar [0], lo saca de la tupla.
    total = cursor.fetchone()[0]
    # si no hay gastos metidos.
    if total is None:
        print("Todavía no hay gastos registrados.")
    else:
        print(f"Total gastado: {total:.2f} €")  # ---> que nos de el resultado en decimales.
    
def borrar_gasto():
    # se crea un try para evitar errores.
    try:
        usuario = input("Que id quiere borrar: ")
    except ValueError:
        # lse pide como tiene que ser.
        print("Debes introducir un id valido. ")
    # borra la tabla, where id=? pero solo la fila cuyo id coincida, y con usuario se dice que le valor ? lo escribio el.   
    cursor.execute("DELETE FROM Gastos_Personales WHERE id=?", (usuario,))
    conn.commit()
    # contamos cuantas filas se vieron afectadas por la ultima operacion, si > 0(se borro algo), si es 0(no se borro nada). saber si delete funciono.
    if cursor.rowcount > 0:
        print("Registro eliminado. ")
    else:
        print("No existe ningun gasto con ese registro eliminado. ")

def pedir_opcion():
    # se crea un try para evitar que no ponga un numero en la opcion.
    try:
        return int(input("Escoge una opcion: "))
    
    except ValueError:
        print("Debes introducir un numero: ")
        return None
    
def pedir_cantidad():
    # repite hasta que el usuario introduzca algo valido.
    while True:
        # que convierta lo que escribe a float.
        try:
            cantidad = float(input("Cuanto a costado (€) "))
            return cantidad
        except ValueError:
            print("Introduce una cantidad valida por ejemplo: 12.50")
def menu():
    # se crea menu y se hace un bucle, que al poner salir termina.
    while True:
        print("==========================")
        print("---GASTOS PERSONALES---")
        print("==========================")
        print("1. Añadir gasto")
        print("2. Ver todos los gastos")
        print("3. Ver por categoría")
        print("4. Ver total")
        print("5. Borrar gasto")
        print("6. Salir")
        # se llama a la funcion.
        opcion = pedir_opcion()
        # los bucles determinan lo que hace cada opcion.
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
        elif opcion == 6:
            break     # --> fin del bucle.
        else:
            print("Opcion no valida!!!")
# llamamos al menu
menu()
# cerramos conexion.
conn.close()