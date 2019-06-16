

unidad1P = {1:["Que es una variable?", "a) Una funcion", "b) Un modulo (como math)","c) Una manera de almacenar valores", "d) Un script"]}
#Unida1Preguntas 
def Unidad1Preguntas():
    print("Cual de estas opciones son correctas? ")
    print("La gracia de esto es que te des cuenta que es cada cosa.")
    print()
    for i in range(5):
        print(unidad1P[1][i])
    
    respuesta1 = input("Ingresa la letra correcta : ")
    if respuesta1 == "c":
        print("Correcto!")
        print("Las variables son objetos donde puedes almacenar cualquier tipo de valor (int: entero, float: decimal, bool : true o false, string : texto o caracteres. ")
    else: print("Respuesta incorrecta!")#Hacer que alguien pueda ingresar de nuevo la variable.
    input()