# importamos modulo.
import sqlite3
# conectamos con la base de datos.
conn = sqlite3.connect("Agenda.db")
# cursor encargado de ejecutar consultas SQL.
cursor = conn.cursor()
# se crea la tabla.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contactos(
        id INTEGER PRIMARY KEY  AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono  TEXT NOT NULL,
        email TEXT NOT NULL,
        ciudad TEXT NOT NULL,
        puesto TEXT NOT NULL           
    )
""")
# se crea funcion para añadir un contacto.
def añadir_contacto():
    nombre = input("Escribe el nombre: ")
    telefono = (input("Escribe el numero: "))
    email = input("Escribe el emael: ")
    ciudad = input("Escribe la ciudad: ")
    puesto = input("Escribe el puesto que realiza: ")
    print("Contacto creado!!!!")
    cursor.execute(
        "INSERT INTO contactos(nombre, telefono, email, ciudad, puesto) VALUES(?, ?, ?, ?, ?)", (nombre, telefono, email, ciudad, puesto)
)
    conn.commit()

def ver_contactos():
    cursor.execute( "SELECT * FROM contactos")
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

def buscar_contacto():
    usuario = input("¿Que contacto quieres buscar?: ")
    cursor.execute("SELECT * FROM contactos WHERE nombre=?", (usuario,))
    buscar = cursor.fetchall()
    for x in buscar:
        print(x)

def actualizar_contacto():
    id_contacto = input("¿Que contacto quieres actualizar?: ")
    nuevo_nombre = input("Nuevo nombre: ")
    cursor.execute("UPDATE contactos SET nombre=? WHERE id=?", (nuevo_nombre, id_contacto))
    conn.commit()

def borrar_contacto():
    borr = input("Escriba el --id-- correspondiente para borrar el contacto: ")
    cursor.execute("DELETE FROM contactos WHERE id=?", (borr, ))
    print("Contacto borrado!!!!")
    conn.commit()

def menu():
    while True:
        print("============================================")
        print("------AGENDA DE CONTACTOS PERSONAL---------")
        print("============================================")
        print("1. Añadir Contacto")
        print("2. Ver Contactos")
        print("3. Buscar Contacto")
        print("4. Actualizar Contacto")
        print("5. Borrar Contacto")
        print("6. Salir")
        opcion = int(input("Eliga una opcion para empezar!!!!!"))
        if opcion == 1:
            añadir_contacto()
        elif opcion == 2:
            ver_contactos()
        elif opcion == 3:
            buscar_contacto()
        elif opcion == 4:
            actualizar_contacto()
        elif opcion == 5:
            borrar_contacto()
        else:
            break
menu()
conn.close()