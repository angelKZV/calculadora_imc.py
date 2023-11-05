Nombre = input("Introduce tu nombre: ")
Apellido = input("Introduce tu apellido: ")
Edad = input(f"{Nombre}, Introduce tu edad: ")
entrada = 0
 
if Edad.isdigit() :
   entrada = int(Edad)
else :
 print("Dato incorrecto. Debes introducir un numero")
 Edad = input(f"{Nombre}, Introduce tu edad: ")
if entrada <= 0 :
    print("WOOOWWW!! Que joven eres. pero, lo siento, eso no es posible")
    Edad = input(f"{Nombre}, Introduce tu edad: ")
elif entrada > 115 : 
    print("VAYA!!! ¿como le haces para vivir tanto? No te creo, mejor intenta de nuevo")
    Edad = input(f"{Nombre}, Introduce tu edad: ")

while True:
   try:
     peso = float(int(input(f'{Nombre} introduce tu peso¨[kg]: ')))
     break
   except ValueError:
       print(f"Error, {Nombre} solo esta permitido introducir numeros enteros")

while True:
   try:
     estatura = float(input(f'{Nombre} ahora introduce tu estatura[m]: '))
     break
   except ValueError:
      print(f"Error, {Nombre} solo esta permitido introducir numeros decimales o enteros")

IMC = peso / (estatura**2)
if IMC <= 18.5:
    print("nombre: " + Nombre)
    print("apellido: " + Apellido)
    print("edad: " + str(Edad) + " años")
    print(f'{Nombre}, Estas en bajo de peso y tu IMC es:{IMC}')
elif 18.5 <= IMC <= 24.99:
     print("nombre: " + Nombre)
     print("apellido: " + Apellido)
     print("edad: " + str(Edad) + " años")
     print(f'{Nombre}, Estas en un peso normal y tu IMC es:{IMC}')
elif 25 <= IMC <= 29.99:
    print("nombre: " + Nombre)
    print("apellido " + Apellido)
    print("edad: " + str(Edad) + " años")
    print(f'{Nombre}, Tienes sobre peso y tu IMC es:{IMC}')
elif 30 <= IMC <= 34.99:
    print("nombre: " + Nombre)
    print("apellido: " + Apellido)
    print("edad: " + str(Edad) + " años")
    print(f'{Nombre}, Tienes obesidad leve y tu IMC es:{IMC}')
elif 35 <= IMC <= 39.99:
    print("nombre: " + Nombre)
    print("apellido: " + Apellido)
    print("edad: " + str(Edad) + " años")
    print(f'{Nombre}, Tienes obesidad media y tu IMC es:{IMC}')
elif IMC >= 40:
    print("nombre: " + Nombre)
    print("apellido: " + Apellido)
    print("edad: " + str(Edad) + " años")
    print(f'{Nombre}, Tienes obesidad morbida y tu IMC es:{IMC}')