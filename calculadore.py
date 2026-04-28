#Calculadore funcional con operaciones basicas como suma, resta, multiplicacion, division
from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from division import division   

mensaje = '''
|-----------------|
|   Calculadora   |
|1.suma           |
|2.resta          |
|3.multiplicacion |
|4.division       |
|_________________|
''' 
def init():
    print(mensaje)

    opcion = int(input("Eliga una de las opciones de la calculadora: "))

    operando = True

    while operando == True:
        if opcion == 1:
            suma()
            break
        elif opcion == 2:
            resta()
            break
        elif opcion == 3:
            multiplicacion()
            break
        elif opcion == 4:
            division()
            break
        else:
            print("Opcion incorrecta")

init()