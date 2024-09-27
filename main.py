from pystyle import Colors, Colorate
titulo = fr"""
 ██████  █████  ██       ██████ ██    ██ ██       █████  ██████   ██████  ██████   █████  
██      ██   ██ ██      ██      ██    ██ ██      ██   ██ ██   ██ ██    ██ ██   ██ ██   ██ 
██      ███████ ██      ██      ██    ██ ██      ███████ ██   ██ ██    ██ ██████  ███████ 
██      ██   ██ ██      ██      ██    ██ ██      ██   ██ ██   ██ ██    ██ ██   ██ ██   ██ 
 ██████ ██   ██ ███████  ██████  ██████  ███████ ██   ██ ██████   ██████  ██   ██ ██   ██ 
                                                                                                                                                                                  
"""
print(Colorate.Vertical(Colors.red_to_purple, titulo))
print(Colorate.Vertical(Colors.purple_to_blue, """
┌═════════════════════════════════════════════════════════════════════════════════════════════════════════┐
█ Operaciones [ 1 ] Sumar [ 2 ] Resta [ 3 ] Multiplicacion [ 4 ] Division [ 5 ] Potencia [ 6 ] Porcentaje █
└═════════════════════════════════════════════════════════════════════════════════════════════════════════┘""",3))

seleccion = int(input(Colorate.Vertical(Colors.purple_to_blue, "└═>>> ")))

valor1 = float(input("Ingresa el primer digito: "))
valor2 = float(input("Ingresa el segundo digito: "))
match seleccion:
    case 1:
        resultado = valor1 + valor2
    case 2:
        resultado = valor1 - valor2
    case 3:
        resultado = valor1 * valor2
    case 4:
        if valor2 == 0:
            print("No se puede dividir por cero")
            exit()
        else:
            resultado = valor1 / valor2
    case 5:
        resultado = valor1 ** valor2
    case 6:
        resultado = (valor1 * valor2) / 100
    case _:
        print(f"Operacion no encontrada")
        exit()

print(Colorate.Vertical(Colors.purple_to_blue, f"""
┌════════════════════════┐
█    Resultado: {resultado}     █
└════════════════════════┘"""))



