#TRABAJO PRACTICO 1

#1-
print("Hola Mundo")

#2-
nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}!")

#3-
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su lugar de residencia: ")

print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4-
radio=input("Ingrese el radio de un circulo: ")
pi=3.14159
radio=int(radio)
pi=float(pi)
perimetro= (radio*2)*pi
area = (radio*radio)*pi

print(f"El area del circulo es {area} y el perimetro es {perimetro}")

#5-
segundo=input("Ingrese una cantidad de segundos: ")
segundo=int(segundo)
hora=segundo/3600

print(f"{segundo} segundos es equivalente a {hora} horas")

#6-
numUser=int(input("Ingrese un numero: "))

num0=(numUser*0)
num1=(numUser*1)
num2=(numUser*2)
num3=(numUser*3)
num4=(numUser*4)
num5=(numUser*5)
num6=(numUser*6)
num7=(numUser*7)
num8=(numUser*8)
num9=(numUser*9)

print(f"La tabla de multiplicar de {numUser} es: ")
print(num0)
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(num7)
print(num8)
print(num9)

#7-
numUser = int(input("Ingrese un numero entero "))
numUser2 = int(input("Ingrese otro numero entero "))

suma = numUser+numUser2
resta = numUser-numUser2
multi = numUser*numUser2
division = numUser/numUser2

print(f"La suma de ambos numeros es {suma}, la resta {resta}, la multiplicacion {multi} y la division {division}.")

#8-
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en M: "))

IMC = peso / (altura*altura)

print(f"Tu IMC (Indice Masa Corporal) es {IMC}. ")

#9-
celcius=float(input("Ingrese una temperatura en grados celcius: "))

Fahrenheit = (celcius*1.8) + 32

print(f"{celcius}° es equivalente a {Fahrenheit}°F ")

#10-
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un numero: "))
num3=int(input("Ingrese un numero: "))

suma= num1+num2+num3
promedio= suma/3

print(f"El promedio de los 3 numeros es {promedio}. ")