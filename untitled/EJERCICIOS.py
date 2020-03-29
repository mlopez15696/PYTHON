#PRIMER EJERCICIO
print("\nEJERCICIO 1: DE SUMA DE 2 NUMEROS")
n1=float(input("Ingrese numero uno: "))
n2=float(input("Ingrese numero dos: "))
suma=n1+n2

print("La suma es: ",suma)




print("\n\nEJERCICIO 3: DE NUMERO MAYOR")
mayor = 0
maximo = int(input("introduce la cantidad de datos: "))  # Cantidad de numeros, puede variar

for i in range(maximo):
    num = int(input('Dame un numero:'))
    if num > mayor:
        mayor = num

print("el dato mayor es : ",mayor)




print("\n\nEJERCICIO 4: Cantidad de numeros N de la serie FIBONACCI")
def fibonacci(contador,n,p1,p2):
 var = ""
 if(contador!=n):
  var=fibonacci(contador+1,n,p2,p1+p2)
  var=str(p2)+" "+var
 return var
n = int(input("Ingrese un numero entero\n"))
if(n>0):
 a=fibonacci(0,(n-1),0,1)
 print ("0 "+a)


print("\n\nEJERCICIO 5: Leer una secuencia de números y sumar solo los pares")
def numpares():
    numero= int(input("Ingrese el tamaño de la secuencia de numeros: "))
    primero = 0
    cont = 0
    suma = 0
    while cont < numero:
        primero = float(input("Ingrese el numero: "))
        cont = cont + 1
        if primero % 2 == 0:
            suma = suma + primero
        else:
            suma = suma
    print("La suma total de numeros pares es: " + str(suma))
numpares()


#EJERCICIO 6
print("\n\nEJERCICIO 6: FACTORIAL DE UN NUMERO N")
import math

num = input("Introduce un numero: ")
x = int(num)
factorial = math.factorial(x)
print("El factorial es: " , factorial)


#EJERCICIO 2
print("\n\nEJERCICIO 2: F")
def f():
    num1=1
    num2=1
    i = ord('d')
    while not i == 10:

        num2 = int(input("Ingrese un numero"))
        i = ord(input("Presione f para salir"))
        print(num2)
        num1 = num1 * num2
    print(num1)
f()



#EJERCICIO 7
print("\n\nEJERCICIO 7: SECUENCIA DE 30 NUMEROS Y SUMA DE PRIMOS")
def Sec_primos():
    num1=0
    num2=0
    for x in range(0, 50):
        num1 = int(input("El numero"))
        divisor = 2
        while num1>divisor:
             if num1%divisor==0:
              break
             elif num1%divisor != 0:
              divisor=divisor+1

             if num1==divisor:
              num2 = num2 + num1

    print("La suma es"+str(num2))
sec_primos()

