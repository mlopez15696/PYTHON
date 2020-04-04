#EJERCICIO 1 - NUMERO PAR
def numPar():

    numero = 0
    numero = int(input("Ingrese un numero: "))
    if (numero%2 == 0):
        print("El numero ",numero, " es PAR")
        return numero
    else:
        print("El numero ", numero, "NO es PAR")
        return numero

#EJERCICIO 2 - LEER 2 NUMEROS Y MOSTRAR EL PRODUCTO DE ELLOS
def producto():
    primerNumero = float(input("Ingrese el primer numero: "))
    segundoNumero = float(input("Ingrese el segundo numero: "))
    resProducto = primerNumero*segundoNumero
    print("El producto de ",primerNumero," y ", segundoNumero," es: ", resProducto)
    return resProducto

#EJERCICIO 3 - LEER 2 NUMEROS Y DETERMINAR EL MAYOR DE ELLOS
def mayor():
    primerNumero = float(input("Ingrese el primer numero: "))
    segundoNumero = float(input("Ingrese el segundo numero: "))
    if  primerNumero<segundoNumero:
        print("El numero mayor entre", primerNumero, " y ", segundoNumero, " es ", segundoNumero)
    elif primerNumero>segundoNumero:
        print("El numero mayor entre", primerNumero, " y ", segundoNumero, " es ", primerNumero)
    else:
        print("Los numeros", primerNumero, " y ", segundoNumero, " son iguales")

#EJERCICIO 4 - LEER 3 NUMEROS Y MOSTRAR EL MAYOR DE ELLOS
def mayor_tres():
    primerNumero = float(input("Ingrese el primer numero: "))
    segundoNumero = float(input("Ingrese el segundo numero: "))
    tercerNumero = float(input("Ingrese el tercer numero: "))
    if primerNumero>segundoNumero and primerNumero>tercerNumero:
        print("El numero mayor es: ", primerNumero)
    elif segundoNumero>primerNumero and segundoNumero>tercerNumero:
        print("El numero mayor es: ", segundoNumero)
    elif tercerNumero>primerNumero and tercerNumero>segundoNumero:
        print("El numero mayor es: ", tercerNumero)

#EJERCICIO 5 - LEER UN NUMERO Y MOSTRAR SU TABLA DE MULTIPLICAR
def tab_multiplicar():
    numero = int(input("Ingrese el numero a evaluar: "))
    rango=range(1,11)

    for i in rango:
        resultado=numero*i
        print(numero, "*", i," = ", resultado)

#EJERCICIO 6- LEER UNA SECUENCIA DE 30 NUMEROS Y MOSTRAR LA SUMA Y PRODUCTO DE ELLOS
def sec_suma_producto(resultadoSuma=0, resultadoProducto=1):

    for i in range(1,31):
        numero = float(input("Ingrese el numero: "))
        resultadoSuma=numero+resultadoSuma
        resultadoProducto=numero*resultadoProducto

    print("La suma de la secuencia es: ", resultadoSuma)
    print("El producto de la secuencia es: ", resultadoProducto)


#EJERCICIO 7 - LEER UNA SECUENCIA DE NUMEROS HASTA QUE SE INTRODUCE UN NUMERO NEGATIVO Y MOSTRAR LA SUMA DE DICHOS NUMEROS

def sec_num_negativo(resultadoSuma=0):
   while True:
       numero = float(input("Ingrese el numero: "))
       resultadoSuma=numero+resultadoSuma
       if (numero<0):
           resultadoSuma=resultadoSuma-(numero)
           print("La suma es: ", resultadoSuma)
           break

#EJERCICIO 8 - LEER DOS NUMEROS Y REALIZAR EL PRODUCTO MEDIANTE SUMAS
def producto_sumas(suma_producto=0):
    primerNumero= int(input("Ingrese el primer numero: "))
    segundoNumero= int(input("Ingrese el segundo numero: "))

    for i in range(segundoNumero):
        suma_producto = suma_producto+primerNumero
        print(primerNumero, "+")

    print("---------------")
    print("El producto por medio de sumas es: ", suma_producto)

#EJERCICIO 9 - LEER DOS NUMEROS Y REALIZAR LA DIVISION MEDIANTE RESTAS MOSTRANDO EL COCIENTE Y EL RESTO
def restas_cociente():
    dividendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese divisor: "))
    contador = int(0)

    print(dividendo, "-", divisor)
    dividendo=dividendo-divisor

    while (dividendo>0):
        contador =contador + 1
        print(dividendo,"-", divisor)
        dividendo = dividendo - divisor


    print(dividendo)
    print("La division por restas es: ", str(contador +1))

#EJERCICIO 10 - LEER UNA SECUENCIA DE NUMEROS Y MOSTRAR SU PRODUCTO, EL PROCESO FINALIZARA AL INGRESAR "F"
#def sec_producto(resultado=1):
 #   while True:
  #      numero = float(input("Ingrese el numero: "))
   #     resultado = numero * resultado
    #    if numero == 'f':
     #       break
    #print("funciona")
#EN FALLO

#EJERCICIO 11 -  LEER UNA SECUENCIA DE NUMEROS Y DETERMINAR CUAL ES EL MAYOR DE ELLOS
def sec_mayor():
    numeroMayor = 0
    maximo = int(input("Coloque la cantidad de numeros a ingresar: "))

    for i in range(maximo):
        num = int(input("Ingresa un numero: "))
        if num > numeroMayor:
            numeroMayor = num

    print("El numero mayor es: ", numeroMayor)


#EJERCICIO 12 - DADO UN NUMERO, MOSTRAR SU VALOR BINARIO
def numero_binario():
    numero=int(input("Ingrese el numero a convertir: "))

    print("El numero binario de ", numero, " es = ", bin(numero)[2:])

#EJERCICIO 13 - GENERAR ENTEROS DE 3 EN 3 COMENZANDO POR 2 HASTA EL VALOR MAXIMO MENOR QUE 50, CALCULANDO LA SUMA DE LOS ENTEROS GENERADOS QUE SEAN DIVISIBLES ENTRE 5
def ejercicio(sumaEnteros=0):
    inicio=2
    entero = 3
    for i in range(16):
        print(inicio)
        inicio=inicio+entero
        prueba=inicio%5
        if (prueba == 0):
            sumaEnteros+=inicio
#EN FALLO

    print("La suma de los numeros divisibles entre 5 es: ", sumaEnteros)

#EJERCICIO 14 - CALCULAR LA MEDIA DE UNA SECUENCIA DE NUMEROS, EL PROCESO FINALIZARA CUANDO EL USUARIO PULSE F
#def sec_media(contador=0, resultadoSuma=0):
 #   while True:
  #      numero= int(input("Ingrese el numero: "))
   #     resultadoSuma=numero+resultadoSuma
    #    contador=contador+1
     #   letra=str(int(numero))
      #  if letra == 'f':
       #     resultado=resultadoSuma/contador
        #   print(resultado)
         #   break
#EN FALLO

#EJERCICIO 15- GENERAR LOS N PRIMEROS TERMINOS DE LA SERIE DE FIBONACCI Y MOSTRARLOS POR PANTALLA.
def Fibonacci():
    numero=int(input("Ingrese la cantidad de datos que desea visualizar: "))
    numero=numero-1
    fibs = [0, 1]
    for i in range(2, numero + 1):
        fibs.append(fibs[-1] + fibs[-2])
        print(fibs)
    return fibs

#EJERCICIO 16 - LEER UNA SECUENCIA DE NUMEROS Y MOSTRAR CUAL DE ELLOS ES EL MAYOR Y EL MENOR
def mayor_menor():
    numeroMayor=0
    numeroMenor=99999999999999999999999999999999999

    while True:
        numero = float(input("Ingrese el numero: "))
        if (numero %2 !=0):
            print("El numero es impar")
            break
        if numero > numeroMayor:
           numeroMayor = numero
        if numero<numeroMenor:
         numeroMenor = numero
    print("El numero mayor es: ", numeroMayor)
    print("El numero menor es: ", numeroMenor)

#EJERCICIO 17 - LEER UNA SECUENCIA DE NUMEROS Y SUMAR SOLO LOS PARES MOSTRANDO EL RESULTADO DEL PROCESO
def sec_pares(resultado=0):
    maximo = int(input("Coloque la cantidad de numeros a ingresar: "))

    for i in range(maximo):
        numero = int(input("Ingresa un numero: "))
        if (numero %2 ==0):
            resultado=resultado+numero

    print("El resultado de la suma de numeros pares es: ", resultado)


#EJERCICIO 18 - LEER UNA SECUENCIA DE NUMEROS Y MOSTRAR LOS PRIMEROS 30 PARES LEIDOS
def sec_pares_leidos(contador=0):
    while True:
        numero = int(input("Ingrese el numero: "))
        if (numero % 2 == 0 and contador<31):
            print("El numero es par")
            par=numero
            contador=contador+1
        elif (contador==31):
            print("30 numeros pares alcanzados")
            for i in range(1,31):
                if i%2 ==0:
                    print(i)
            break

#EJERCICIO 19 - LEER UNA SECUENCIA DE NUMEROS Y MOSTRAR LA SUMA DE LOS 30 NUMEROS QUE OCUPAN POSICIONES DE LECTURA PAR.
def sec_lectura_par(contador=0, j=0):
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]
    while True:
        numero = int(input("Ingrese el numero: "))

        if (numero % 2 == 0 and contador<31):
            print("El numero es par")
            par=numero
            contador=contador+1
        elif (contador == 31):
            print("30 espacios pares alcanzados")
#EN FALLO

#EJERCICIO 20 - LEER UN NUMERO Y DETERMINAR SU FACTORIAL
def factorial():
    import math
    numero=int(input("Ingrese el numero: "))
    factorial= math.factorial(numero)
    print("El factorial del numero ", numero, " es: ", factorial)

#EJERCICIO 21 - LEER UN NUMERO Y DETERMINAR SI ES PRIMO O NO
def num_primo():
    numero = int(input("Ingrese el numero: "))
    contador = 0
    for i in range(1, numero + 1):
        if (numero % i) == 0:
            contador = contador + 1

    if contador == 2:
        print("el numero es primo")
    else:
        print("el numero no es primo")

#EJERCICIO 22 - LEER UNA SECUENCIA DE 30 NUMEROS Y MOSTRAR LA SUMA DE LOS PRIMOS
def sec_suma_primos(resultado=0):
    for i in range(30):
        numero = int(input("Ingresa un numero: "))
        if (numero < 2):
            return False
        for i in range(2, numero):
            if numero % i == 0:
                return False
            resultado=resultado+numero
        return True

    print("El resultado de la suma de numeros primos es: ", resultado)

#PENDIENTE DE SEGUIR SI QUIERO, SINO PROSEGUIR, SE QUEDO EN SOLO INGRESA 1 NUMERO
#EJERCICIO 23 - LEER UNA SECUENCIA DE 30 NUMEROS Y MOSTRAR LA SUMA DE SU FACTORIAL
def sec_factorial(suma_factorial=0):
    for i in range(30):
        import math
        numero = int(input("Ingrese el numero: "))
        factorial = math.factorial(numero)
        suma_factorial= factorial+suma_factorial
        print("El factorial del numero ", numero, " es: ", factorial)

    print("La suma de los factoriales es: ", suma_factorial)


#EJERCICIO 24 - CALCULAR EL VALOR DEL NUMERO E (EULER) N(1/n!) Y MOSTRARLO EN PANTALLA
def num_euler(euler=0):
    import math
    numero=int(input("Ingrese el numero: "))
    euler=(numero*(1/(math.factorial(numero))))
    print("El numero de euler de ", numero," es: ", euler)
#TERMINADO, CON LA FORMULA SI DA LOS DATOS QUE SON, pero segun internet es otra formula, se suma en vez de multiplicar

#EJERCICIO 25 - IMPLEMENTAR UN PROGRAMA QUE SEA CAPAZ DE CALCULAR EL RESULTADO DE APLICAR LA SIGUIENTE FORMULA (n i)=n! / (i! * (n-i)!)

def formula_factorial(factorialN=0, factorialNI=0, factorialI=0, formula_completa=1):
    import math
    print("La formula es: n! / (i! * (n-i)!)")
    n= int(input("Ingrese numero N: "))
    i= int(input("Ingrese numero I: "))
    ni=n-i
    if ni<0:
        print("No se puede realizar la operacion ya que la resta de ambos da como resultado un negativo")

    else:
            factorialN=math.factorial(n)
            factorialI=math.factorial(i)
            factorialNI=math.factorial(ni)
            formula_completa=factorialN/(factorialI*factorialNI)
            print("La operacion es: ", factorialN,"/ (",factorialI,"*",factorialNI,")")
            print("El resultado de la operacion es: ", formula_completa)

while True:
    print("MENU")
    print("1. Leer un número y mostrar por la salida estándar si dicho número es o no es par.")
    print("2. Leer 2 números y mostrar el producto de ellos. ")
    print("3. Leer 2 números y determinar el mayor de ellos.")
    print("4. Leer 3 números y mostrar el mayor de ellos. ")
    print("5. Leer un número y mostrar su tabla de multiplicar.")
    print("6. Leer una secuencia de 30 números y mostrar la suma y el producto de ellos. ")
    print("7. Leer una secuencia de números, hasta que se introduce un número negativo y mostrar la suma de dichos números.")
    print("8. Leer dos números y realizar el producto mediante sumas. ")
    print("9. Leer dos números y realizar la división mediante restas mostrando el cociente y el resto. ")
    print("10. Leer una secuencia de números y mostrar su producto, el proceso finalizará  cuando el usuario pulse a la tecla F. ")
    print("11.  Lee una secuencia de números y determina cual es el mayor de ellos. ")
    print("12. Dado un número mostrar su valor en binario.")
    print("13. Generar enteros de 3 en 3 comenzando por 2 hasta el valor máximo menor que Calculando la suma de los enteros generados que sean divisibles por 5. ")
    print("14. Calcular la media de una secuencia de números, el proceso finalizará cuando el usuario pulse F. ")
    print("15. Generar los N primeros términos de la serie de Fibonacci y mostrarlos por pantalla.")
    print("16. Leer una secuencia se números y mostrar cuáles de ellos es el mayor y el menor, el proceso finalizará cuando se introduzca un número impar. ")
    print("17. Leer una secuencia de números y sumar solo los pares mostrando el resultado del proceso. ")
    print("18. Leer una secuencia de números y mostrar los 30 primeros pares leídos. ")
    print("19. Leer una secuencia de números y mostrar la suma de los 30 números que ocupan posiciones de lectura par. ")
    print("20. Leer un número y determinar su factorial. ")
    print("21. Leer un número y determinar si es o no es primo. ")
    print("22. Leer una secuencia de 30 números y mostrar la suma de los primos. ")
    print("23. Leer una secuencia de 30 números y mostrar la suma de su factorial. ")
    print("24. Calcular el valor del número E (Euler) =n(1/n!) y mostrarlo en pantalla.")
    print("25. Implementar un programa que sea capaz de calcular el resultado de aplicar la fórmula siguiente (n i)=n! / (i! * (n-i)!).")
    print("26. Salir del programa")
    opcion = int(input("Ingrese el numero de la opcion deseada: "))

    if opcion == 1:
        numPar()
        break
    elif opcion == 2:
        producto()
        break
    elif opcion == 3:
        mayor()
        break
    elif opcion == 4:
        mayor_tres()
        break
    elif opcion == 5:
        tab_multiplicar()
        break
    elif opcion == 6:
        sec_suma_producto()
        break
    elif opcion == 7:
        sec_num_negativo()
        break
    elif opcion == 8:
        producto_sumas()
        break
    elif opcion == 9:
        restas_cociente()
        break
    elif opcion == 10:
        print("Esta funcion se encuentra en mantenimiento")
        break
    elif opcion == 11:
        sec_mayor()
        break
    elif opcion == 12:
        numero_binario()
        break
    elif opcion == 13:
        ejercicio()
        break
    elif opcion == 14:
        print("Esta funcion se encuentra en mantenimiento")
        break
    elif opcion == 15:
        Fibonacci()
        break
    elif opcion == 16:
        mayor_menor()
        break
    elif opcion == 17:
        sec_pares()
        break
    elif opcion == 18:
        sec_pares_leidos()
        break
    elif opcion == 19:
        sec_lectura_par()
        break
    elif opcion == 20:
        factorial()
        break
    elif opcion == 21:
        num_primo()
        break
    elif opcion == 22:
        sec_suma_primos()
        break
    elif opcion == 23:
        sec_factorial()
        break
    elif opcion == 24:
        num_euler()
        break
    elif opcion == 25:
        formula_factorial()
        break

    if opcion==26:
        break

