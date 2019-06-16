#Moreno dime por whatsapp si puedes ver este comentario.

#Mira dejemos este archivo como el principal. 
#Pero organizemonos que vamos haciendo por Discord otro dia
#Y hacemos cada uno una parte y se la vamos agregando aca
#y cuando lo agreguemos lo vamos provando para ver como va.
# pta y cualquier idea o cosa vamos tambien hablando por wsp.
#Y ultimo, no programemos mucho aca, pq manana voy a
#subir este archivo a servidor privado para que este
#24 horas activo.

import unidades 
#variables publicas:
seleccion = 0


def Opcion():
   
    if(seleccion == 1):
        print("Unidad 1")
        unidades.Unidad1Preguntas()
    elif(seleccion == 2):
        print("Unidad 2")
    elif(seleccion == 3):
        print("Unidad 3")
    elif(seleccion == 4):
        print("Unidad 4")
    elif(seleccion == 5):
        print("Unidad 5")
    elif(seleccion == 6):
        print("Unidad 6")
    else:
        print("Has ingresado un numero incorrecto, seras redirigido al menu principal.")
        


while True:
    print("Bienvenido a tu guia para Python3 en el Electivo del Colegio Tabancura")
    print("Elige una de las proximas opciones!")
    print("1 : Unidad 1  // variables, print, etc")
    print("2 : Unidad 2  // control de flujo (if, elif, else) ")
    print("3 : Unidad 3  // Bucles o siglos (for, while)")
    print("4 : Unidad 4  // listas, diccionarios")
    print("5 : Unidad 6  // funciones")
    print("6 : Logica    // Aprende logica basica")
    print("Que es esto?")
    print()
    seleccion = int(input("Elige un numero : "))
    Opcion()
    

#Para almacenar el valor ingresado por el usuario en Menu()


#Para saber que opcion eligio el usuario



