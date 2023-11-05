 #  calculadora IMC
p = input("ingresa tu peso en kg:")
a = input("ingresa tu altura en metros")

peso = p
altura = a
imc = p / a * a



if imc < 18.9:
   print(f"{imc},peso bajo")
elif 18.50<= imc <= 24.99:
   print(f"{imc},normal")
elif 25.00 <= imc <= 29.99:
   print(f"{imc},sobrepeso")
elif 30.00 <= imc<= 34.99:
    print(f"{imc},obesidad leve")
elif 35.00 <= imc <= 39.00:
    print(f"{imc},obesidad media")
elif 40 <= imc <= 60:
    print(f"{imc},obesidad morbida")



