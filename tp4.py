#!Consigna: crear un programa el cual le permita al usuario:
#!1. ingresar nombre y apellido.
#!2. ingresar su n° de DNI.
#!3. elegir a que partido politico desea votar:
#!  opcion A partido politico pro.
#!  opcion B partido politico K.
#!   opcion C partido politico de izq.
#!  opcion D otro partido politico.
#!4. mostrar los datos ingresado y el voto realizado.
#!5. en el caso de no haber elegido bien indicar " opcion mal ingresada

a = int(input("Ingrese 1 para continuar:"))
while a==1:        
    print("Bienvenid@") 
    N = input("ingrese nombre y apellido:  ")
    D = input("ingrese numero de DNI:  ")
    print("""
    Opciones a elegir:
    A. partido politico pro
    B. partido politico K
    C. partido politico de izquierda
    D. otro partido politico
    """)
    C= input("ingrese que partido desea votar:  ")
    if C.upper()=="A":
        print("el usuario", N, ",DNI: ", D,",ha votado al pro")
        print("gracias por su voto")
    elif C.upper()=="B":
        print("el usuario", N, ",DNI: ", D,",ha votado a los k")
        print("gracias por su voto")
    elif C.upper()=="C":
        print("el usuario", N, ",DNI: ", D,",ha votado por el partido de izquierda")
        print("gracias por su voto")
    elif C.upper()=="D":
        print("el usuario", N, ",DNI: ", D,",ha votado por otro partido politico")
    else:
        print("opcion equivocada")
        print("Gracias por su voto")
    a= int(input("Ingrese 1 para continuar:"))
