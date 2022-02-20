#DECLARACIÓ DE FUNCIONS
from os import *
from time import sleep

def MenuOpcions():
    print("MENÚ D'OPCIONS:")
    print("0- SORTIR DEL PROGRAMA")
    print("1- VERIFICAR NOMBRES PRIMERS ")
    print("2- DIBUIXAR UN TAULELL D'ESCACS")
    print("3- CÀLCUL CONSUM")
    print("7- JOC D'ENDEVINA EL NUMERO")
    print("8- CONVERSOR FARENHEIT-CELCIUS")
    print("9- VALIDADOR DE DATA")

#MAIN
MenuOpcions()
tria = input("ESCULL UNA OPCIÓ: ")
while (tria != '0'):
    if (tria == '1'):
        NombresPrimers()
    elif (tria == '2'):
        TaulellEscacs()
    elif (tria == '3'):
        CalculConsum()
    elif (tria == '4'):
        DiesPassats()
    elif (tria == '5'):
        OrdenarNumeros()
    elif (tria == '6'):
        CalculadorsBasica()
    elif (tria == '7'):
        JocEndevinaNumero()
    elif (tria == '8'):
        ConversorFarenheitCelcius()
    elif (tria == '9'):
        ValidaData()
    else: 
        print("ERROR")
        sleep(1)
        
    #RETORN AL MENÚ
    print("TORNANT AL MENÚ PRINCIPAL")
    #NETEJA DE PANTALLA
    sleep(0.7)
    system('cls')
    #TRIA D'OPCIÓ
    tria = input("ESCULL UNA OPCIÓ: ")
