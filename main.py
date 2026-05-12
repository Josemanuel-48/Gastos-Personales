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
    
def datos():
    fecha = (input("Fecha: "))
    sitio = input("lugar de gasto: ")
    categoria = input("Escribe la categoria: ")
    cantidad = float(input("Cuánto ha costado (€): "))
    print("Gasto Añadido!!!")
    cursor.execute(
        "INSERT INTO Gastos_Personales(fecha, sitio, categoria, cantidad) VALUES(?, ?, ?, ?)", (fecha, sitio, categoria, cantidad)
    )
    conn.commit()

def ver_gastos():
    cursor.execute("SELECT * FROM Gastos_Personales")
    resultado = cursor.fetchall()
    for r in resultado:
        print(r)

def categoria_gasto():
    cursor.execute("SELECT categoria, SUM(cantidad) FROM Gastos_Personales GROUP BY categoria")
    total = cursor.fetchall()
    for i in total:
        print(i)

def ver_total():
    cursor.execute("SELECT SUM(cantidad) FROM Gastos_Personales")
    total = cursor.fetchall()
    for x in total:
        print(x)

def borrar_gasto():
    usuario = input("Que id quiere borrar: ")
    cursor.execute("DELETE FROM Gastos_Personales WHERE id=?", (usuario,))
    conn.commit()
    print("Registro Eliminado!!!!")

def menu():
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
        opcion = int(input("Escoge una opcion: "))
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
            break

menu()
conn.close()