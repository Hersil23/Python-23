# Programa de Gestión de Tareas

# Creamos una lista vacía donde almacenaremos todas las tareas
tareas = []

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n=== BIENVENID@ AL GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")
    print("========================")

# Función para agregar una nueva tarea
def agregar_tarea():
    # Solicitamos al usuario que ingrese la descripción de la tarea
    tarea = input("Ingresa la nueva tarea: ")
    
    # Agregamos la tarea a la lista usando el método append()
    tareas.append(tarea)
    
    # Mostramos un mensaje de confirmación
    print(f"✓ Tarea '{tarea}' agregada exitosamente")

# Función para eliminar una tarea existente
def eliminar_tarea():
    # Verificamos si hay tareas en la lista
    if len(tareas) == 0:
        print("No hay tareas para eliminar")
        return  # Salimos de la función si la lista está vacía
    
    # Mostramos todas las tareas con su índice
    print("\nTareas actuales:")
    for i in range(len(tareas)):
        # i+1 para mostrar números desde 1 en lugar de 0
        print(f"{i + 1}. {tareas[i]}")
    
    # Pedimos al usuario que elija qué tarea eliminar
    try:
        # Convertimos la entrada del usuario a entero
        numero = int(input("\n¿Qué tarea deseas eliminar? (número): "))
        
        # Verificamos que el número esté en el rango válido
        if 1 <= numero <= len(tareas):
            # Eliminamos la tarea (restamos 1 porque los índices empiezan en 0)
            tarea_eliminada = tareas.pop(numero - 1)
            print(f"✓ Tarea '{tarea_eliminada}' eliminada exitosamente")
        else:
            # Si el número está fuera del rango
            print("Número de tarea inválido")
    
    # Capturamos errores si el usuario no ingresa un número
    except ValueError:
        print("Por favor, ingresa un número válido")

# Función para mostrar todas las tareas
def mostrar_tareas():
    # Verificamos si hay tareas en la lista
    if len(tareas) == 0:
        print("\nNo hay tareas pendientes. ¡Estás al día!")
        return  # Salimos de la función
    
    # Si hay tareas, las mostramos
    print("\n=== TUS TAREAS ===")
    for i in range(len(tareas)):
        # Mostramos cada tarea con su número
        print(f"{i + 1}. {tareas[i]}")
    print("==================")

# Función principal que ejecuta el programa
def main():
    # Creamos un bucle infinito que se ejecutará hasta que el usuario elija salir
    while True:
        # Mostramos el menú
        mostrar_menu()
        
        # Solicitamos al usuario que elija una opción
        opcion = input("\nElige una opción (1-4): ")
        
        # Evaluamos la opción elegida
        if opcion == "1":
            # Llamamos a la función para agregar tarea
            agregar_tarea()
        
        elif opcion == "2":
            # Llamamos a la función para eliminar tarea
            eliminar_tarea()
        
        elif opcion == "3":
            # Llamamos a la función para mostrar tareas
            mostrar_tareas()
        
        elif opcion == "4":
            # Mostramos mensaje de despedida
            print("\n¡Hasta luego! 👋")
            # Salimos del bucle y terminamos el programa
            break
        
        else:
            # Si la opción no es válida
            print("\nOpción inválida. Por favor, elige una opción del 1 al 4")

# Esta línea verifica si el archivo se está ejecutando directamente
# (no importado como módulo)
if __name__ == "__main__":
    # Ejecutamos la función principal
    main()