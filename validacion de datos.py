entrada = input("¡HOLA! Introduce tu edad: ")

edad = 0

if entrada.isnumeric() :
    edad = int(entrada)
else :
    print("Dato incorrecto. Debes introducir un numero")
    exit()

if edad <= 0 :
    print("WOOOWWW!! Que joven eres. pero, lo siento, eso no es posible")
elif edad > 115 : 
    print("VAYA!!! ¿como le haces para vivir tanto? No te creo, mejor intenta de nuevo")
elif edad < 18 :
    print("Eres menor de edad no puedes comprar tu cigarro")
else : 
    print("Eres mayo de edad. aqui tienes tu cigarro")
    