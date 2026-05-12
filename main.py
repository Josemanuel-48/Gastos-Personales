# importamos modulo
import sqlite3
 
# conectamos con la base de datos
conn = sqlite3.connect("Gastos_Personales.db")
 
# se crea un cursor, objeto encargado de ejecutar consultas SQL
cursor = conn.cursor()
 
# se crea la tabla si no existe
cursor.execute("""
        CREATE TABLE IF NOT EXISTS Gastos_Personales(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            fecha TEXT NOT NULL, 
            sitio TEXT NOT NULL,  
            categoria TEXT NOT NULL,
            cantidad REAL  
    )
""")
 
 
# MEJORA 2: función para pedir y validar la cantidad
def pedir_cantidad():
    while True:
        try:
            cantidad = float(input("Cuánto ha costado (€): "))
            return cantidad
        except ValueError:
            print("Introduce una cantidad válida, por ejemplo: 12.50")
 
 
# MEJORA 1: función para pedir y validar la opción del menú
def pedir_opcion():
    try:
        return int(input("Escoge una opción: "))
    except ValueError:
        print("Debes introducir un número.")
        return None
 
 
def datos():
    fecha = input("Fecha (ej: 2025-05-12): ")
    sitio = input("Lugar de gasto: ")
    categoria = input("Escribe la categoría: ")
    cantidad = pedir_cantidad()  # MEJORA 2: usamos la función validada
 
    # insertamos el registro en la tabla
    cursor.execute(
        "INSERT INTO Gastos_Personales(fecha, sitio, categoria, cantidad) VALUES(?, ?, ?, ?)",
        (fecha, sitio, categoria, cantidad)
    )
    # confirmamos cambios
    conn.commit()
    print("¡Gasto añadido!")
 
 
# MEJORA 4: mostrar gastos con formato legible
def ver_gastos():
    cursor.execute("SELECT * FROM Gastos_Personales ORDER BY fecha")  # MEJORA 6: ordenado por fecha
    resultado = cursor.fetchall()
 
    if not resultado:
        print("No hay gastos registrados.")
    else:
        print(f"\n{'ID':<5} {'Fecha':<12} {'Sitio':<20} {'Categoría':<15} {'Cantidad':>10}")
        print("-" * 65)
        for gasto in resultado:
            id_gasto, fecha, sitio, categoria, cantidad = gasto
            print(f"{id_gasto:<5} {fecha:<12} {sitio:<20} {categoria:<15} {cantidad:>9.2f} €")
        print()
 
 
def categoria_gasto():
    cursor.execute("SELECT categoria, SUM(cantidad) FROM Gastos_Personales GROUP BY categoria")
    total = cursor.fetchall()
 
    if not total:
        print("No hay gastos registrados.")
    else:
        print(f"\n{'Categoría':<20} {'Total':>10}")
        print("-" * 32)
        for categoria, suma in total:
            print(f"{categoria:<20} {suma:>9.2f} €")
        print()
 
 
# MEJORA 3: ver_total() corregida con fetchone() y sin el for incorrecto
def ver_total():
    cursor.execute("SELECT SUM(cantidad) FROM Gastos_Personales")
    total = cursor.fetchone()[0]
 
    if total is None:
        print("Todavía no hay gastos registrados.")
    else:
        print(f"Total gastado: {total:.2f} €")
 
 
# MEJORA 5: borrar_gasto() comprueba si el id existe antes de borrar
def borrar_gasto():
    try:
        usuario = int(input("Qué id quieres borrar: "))
    except ValueError:
        print("Debes introducir un id válido.")
        return
 
    cursor.execute("DELETE FROM Gastos_Personales WHERE id=?", (usuario,))
    conn.commit()
 
    if cursor.rowcount > 0:
        print("Registro eliminado.")
    else:
        print("No existe ningún gasto con ese id.")
 
 
def menu():
    while True:
        print("\n==========================")
        print("   GASTOS PERSONALES")
        print("==========================")
        print("1. Añadir gasto")
        print("2. Ver gastos")
        print("3. Gastos por categoría")
        print("4. Ver total")
        print("5. Borrar gasto")
        print("6. Salir")
 
        opcion = pedir_opcion()  # MEJORA 1: usamos la función validada
 
        if opcion is None:
            continue  # si pedir_opcion() devuelve None, volvemos al menú
        elif opcion == 1:
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
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
 
 
# llamamos al menú
menu()
 
# cerramos la conexión
conn.close()