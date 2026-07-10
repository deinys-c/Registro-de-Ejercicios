from datetime import datetime,timedelta
import json

def total_semana(ejercicios):
    if not ejercicios:
        return 0
    
    # Conseguimos la fecha de hoy limpia (a las 00:00:00) para evitar bugs con las horas
    hoy = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    hace_siete_dias = hoy - timedelta(days=7)
    
    total_minutos = 0
    
    for ejercicio in ejercicios:
        fecha_ejercicio = datetime.strptime(ejercicio["fecha"], "%d/%m/%Y")
        
        # Filtramos los que estén en el rango de los últimos 7 días hasta hoy inclusive
        if hace_siete_dias <= fecha_ejercicio <= hoy:
            total_minutos += ejercicio["duracion"]
            
    return total_minutos
def añadir_ejercicio(ejercicios):
    tipo = input("Tipo: ")
    try:
        duracion = int(input("Duración (minutos): " ))
    except ValueError:
        print("La Duración debe ser un número")
        return
    fecha = input("Fecha (DD/MM/YYYY): ")
    if not fecha:
        print("La fecha no puede estar vacía")
        return
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha incorrecto. Usa DD/MM/AAAA")
        return
    ejercicio = {"tipo": tipo, "duracion": duracion, "fecha": fecha}
    
    ejercicios.append(ejercicio)
    print(f"Ejercicio Añadido: Tipo:{ejercicio['tipo']}-Duracion:{ejercicio['duracion']}min-Fecha:{ejercicio['fecha']}")

def ver_historial(ejercicios):
    if not ejercicios:
        print("No hay ejercicios registrados")
        return
    else:
        ejercicios_ordenados = sorted(
        ejercicios,
        key=lambda e: datetime.strptime(e["fecha"], "%d/%m/%Y"),
        reverse=True
    )
        for i,ejercicio in enumerate(ejercicios_ordenados, 1):
            print(f"{i}. Tipo:{ejercicio['tipo']}-Duracion:{ejercicio['duracion']}min-Fecha:{ejercicio['fecha']}")
def cargar_ejercicios():
    try:
        with open("ejercicios.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Archivo no existe")
        return []
    except json.JSONDecodeError:
        print("Archivo corrupto o vacio")
        return []
def guardar_ejercicios(ejercicios):
    with open("ejercicios.json", "w") as archivo:
        json.dump(ejercicios,archivo)
ejercicios = cargar_ejercicios()

while True:
    try:
        print("   Registro de Ejercicios   ")
        print("1. Añadir Ejercicio")
        print("2. Ver Historial")
        print("3. Total Semanal")
        print("4. Salir")
    
        opcion = input("> ")
    
        if opcion == "4":
            print("Gracias por usar la aplicación")
            guardar_ejercicios(ejercicios)
            break
        elif opcion == "1":
            añadir_ejercicio(ejercicios)
        elif opcion == "2":
            ver_historial(ejercicios)
        elif opcion == "3":
            print(total_semana(ejercicios))
    except ValueError:
        print("Opción no Válida")