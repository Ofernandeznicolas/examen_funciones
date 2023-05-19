# Parcial de programación Python

# El parcial consta de 3 ejercicios, los cuales deben cumplir con la consigna para poder ser aprobados, aunque llegado el caso puntual que no se complete en su totalidad se dará la oportunidad de defender la logica aplicada de forma verbal en la proxima clase.

# Se deberá entregar el parcial eligiendo algunas de las siguientes opciones:
# 1- Enviando el link de su repositorio
# 2- Enviar los archivos al correo lozanorichard32@gmail.com

#Nombre Completo:

# ------------------------------ EJERCICIOS -----------------------------------------

# 1- contador_vocales: Escribir una funciona que reciba una cadena de texto por teclado y que cuente la cantidad de vocales que contiene.
#Ejemplo: cadena = "Hoy es el parcial"    ==> Esto me devolvera que en la cadena hay 6 vocales

# 2- area_triangulo: Escribir una funcion que tome por teclado la base y altura de un triangulo y calcule su aréa. La funcion debe retornar el resultado.




## Ejerciocio 1 

def contador_vocales(Cadena_texto):
    contador = 0
    Cadena_texto.lower()

    for i in Cadena_texto:
        if i == "a" or i == "e" or i == "i" or i == "u" or i == "o":
             contador += 1

    print(f"En la cadena de texto ingresada hay {contador} vocales")


Cadena_texto = input("Ingrese su cadena de texto para saber la cantidad de vocales que tiene: ")
contador_vocales(Cadena_texto)

## Ejercicio 2

def area_triangulo(base, altura):
    print (f"La superficie del triangulo es {base * altura / 2}")

base= int(input("Ingrese el valor de la base de su triangulo: "))
altura= int(input("Ingrese el valor de la altura de su triangulo: "))

area_triangulo(base,altura)


## Ejercicio 3 

contador = 0

while contador < 101:
    
    if contador %5 == 0 and contador %3 == 0:
        print("FizzBuzz")
    elif contador %5 == 0:
        print("Buzz")
    elif contador %3 ==0:
        print("Fizz")
    else:
        print(contador)
    
    contador += 1
