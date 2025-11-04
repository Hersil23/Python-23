try:
    cake = 1
    n = int(input("¿Cuántas personas comerán pastel?: "))
    print(f"A cada persona le corresponde: {cake / n} piezas de pastel.")
except ZeroDivisionError:
    print("¡Entonces el cumpleañero se queda el pastel!")
except ValueError:
    print("No sé que número es ese :(")

# Pequeña práctica: Crear un campo que solicite nuevamente al usuario un valor en caso de errores
# Pistas: try... catch + Loops

while True:
    try:
        cake = 1
        n = int(input("¿Cuántas personas comerán pastel?: "))
        print(f"A cada persona le corresponde: {cake / n} piezas de pastel.")
        break
    except ZeroDivisionError:
        print("¡Entonces el cumpleañero se queda el pastel!")
    except ValueError:
        print("No sé que número es ese :(")