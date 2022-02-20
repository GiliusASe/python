#DECLARACIÓ DE FUNCIONS
import random as rnd
from os import *
from time import sleep
from tkinter import *
import sys
from tkinter.constants import PROJECTING


def MenuOpcions():
    print("MENÚ D'OPCIONS:")
    print("0- SORTIR DEL PROGRAMA")
    print("1- VERIFICAR NOMBRES PRIMERS ")
    print("2- DIBUIXAR UN TAULELL D'ESCACS")
    print("3- CÀLCUL CONSUM")
    print("4- DIES PASSATS")
    print("5- ORDENADOR DE NÚMEROS")
    print("6- CALCULADORA BÀSICA")
    print("7- JOC D'ENDEVINA EL NUMERO")
    print("8- CONVERSOR FARENHEIT-CELCIUS")
    print("9- VALIDADOR DE DATA")
    print("10- AREA D'UN TRIANGLE")
    print("11- DIES QUE VAN PASSAR DESDE QUE VAS NEIXER")
    print("12- CALCUL D'OPERACIONS")

#Joc d'endevinar un numero amb pistes de si es mes alt o mes baix
def JocEndevinaNumero():
    numeroAleatori= rnd.randint(0, 10)

    numeroIntroduit = int(input("Introdueix un número: "))

    while numeroIntroduit != numeroAleatori:
        if numeroIntroduit > numeroAleatori:
            print("Intenta amb un nombre MÉS PETIT")
            numeroIntroduit= int(input("Introdueix un altre número: "))
        else :
            print("Intenta amb un nombre MÉS GRAN")
            numeroIntroduit= int(input("Introdueix un altre número: ")) 
    if numeroIntroduit == numeroAleatori:
        print("Has endevinat el número")

#Conversor Celcius-Farenheit
def ConversorFarenheitCelcius():
    tipus = input("Introdueixi si introduira Farenheit(f) o Celcius(c) > ")
    temperatura = int(input("introdueix la tempreratura"))
    if tipus == "f":
        temperatura = (temperatura - 32) / 1.8000
        print("La tempreratura anterior en celcius es ", temperatura)
    elif tipus == "c":
        temperatura = (temperatura * 1.8000) + 32
        print("La tempreratura anterior en farenheit es ", temperatura)
    else:
        print("Error parametre no valid")


#Funcio que valida una data format dd/mm/yyyy
def ValidaData():
    data = input("Entri una data format dd/mm/aaaa    ")
    dia = int(data[0] + data[1])
    mes = int(data[3] + data[4])
    any = int(data[6] + data[7] + data[8] + data[9])
    anyPart1 = any / 100
    anyPart2 = any % 100
    if ((anyPart1 % 4 == 0 or anyPart2 % 4 == 0) and anyPart2 != 0) and mes == 2 and dia > 29:
        print("l'any es errori")
    elif  mes == 2 and dia > 28:
        print("l'any es erroni")
    elif mes >= 4 and mes % 2 == 0 and dia > 30:
        print("l'any es erroni")
    elif mes % 2 != 0 and dia > 31:
        print("l'any es erroni")
    elif mes > 12 and mes < 1:
        print("l'any es erroni")
    else:
        print("l'any es correcte")


def NombresPrimers():
    system('cls')
    print("EXECUTANT VERIFICADOR DE NOBRES PRIMERS:")
    primer = True
    divisor = 2

            
    numero = int(input("ENTRA UN NOMBRE"))
    numero = int(numero)
    while divisor < numero:
        if ((numero % divisor) == 0):primer = False
        divisor = divisor + 1

    if primer == True:print("EL NOMBRE ",numero," ÉS PRIMER")
    else:print("EL NOMBRE ",numero," NO ÉS PRIMER")

def TaulellEscacs():
    system('cls')
    from tkinter import Tk, Canvas

    fin = Tk()


    c=Canvas(fin,bg="white",height=500,width=500) 
    c.pack()


    c.create_rectangle(3,3,400,400,width=3)

    c.create_rectangle(100,0,50,50, fill="black")
    c.create_rectangle(50,50,0,100, fill="black")

    c.create_rectangle(200,0,150,50, fill="black")
    c.create_rectangle(150,50,100,100, fill="black")
    c.create_rectangle(100,100,50,150, fill="black")
    c.create_rectangle(50,150,0,200, fill="black")

    c.create_rectangle(300,0,250,50, fill="black")
    c.create_rectangle(250,50,200,100, fill="black")
    c.create_rectangle(200,100,150,150, fill="black")
    c.create_rectangle(150,150,100,200, fill="black")
    c.create_rectangle(100,200,50,250, fill="black")
    c.create_rectangle(50,250,0,300, fill="black")


    c.create_rectangle(400,0,350,50,fill="black")
    c.create_rectangle(350,50,300,100, fill="black")
    c.create_rectangle(300,100,250,150, fill="black")
    c.create_rectangle(250,150,200,200, fill="black")
    c.create_rectangle(200,200,150,250, fill="black")
    c.create_rectangle(150,250,100,300, fill="black")
    c.create_rectangle(100,300,50,350, fill="black")
    c.create_rectangle(50,350,0,400, fill="black")

    c.create_rectangle(400,100,350,150, fill="black")
    c.create_rectangle(350,150,300,200, fill="black")
    c.create_rectangle(300,200,250,250, fill="black")
    c.create_rectangle(250,250,200,300, fill="black")
    c.create_rectangle(200,300,150,350, fill="black")
    c.create_rectangle(150,350,100,400, fill="black")

    c.create_rectangle(400,200,350,250, fill="black")
    c.create_rectangle(350,250,300,300, fill="black")
    c.create_rectangle(300,300,250,350, fill="black")
    c.create_rectangle(250,350,200,400, fill="black")

    c.create_rectangle(350,350,300,400, fill="black")
    c.create_rectangle(400,350,350,300, fill="black")



    fin.mainloop()

def CalculConsum():
    system('cls')
    consum = (float(input("Introdueix el consum mitjà del teu vehicle: ")))
    dipòsit = (float(input("Introdueix els litres restants dins el teu dipòsit: ")))
    distanciaDestí = (float(input("Introdueix la distància entre el punt d'inici i el destí: ")))

    r = dipòsit / consum

    if r > distanciaDestí:
        print("No arribaràs al teu destí")

    else:
        print("Arribaràs al teu destí")


def DiesPassats():

    import datetime
    
    diaN = int(input("Dia de Naixament:"))
    mesN = int(input("Mes de Naixament:"))
    anyN = int(input("Any de Naixament:"))

    dActual = datetime.date.today()

    print(
    "dia" , dActual.day,
    "mes" , dActual.month,
    "any" , dActual.year)

    diesPassats = dActual.day - diaN
    mesosPassats = (dActual.month - mesN)*30
    anysPassats = (dActual.year - anyN)*365

    diesTotals = diesPassats + mesosPassats + anysPassats
    print ("Han passat:", diesTotals, "dies")
    
def OrdenarNumeros():
    
    num1 = int(float(input("Intrdueix el primer numero:")))
    num2 = int(float(input("Intrdueix el segon numero:")))
    num3 = int(float(input("Intrdueix el tercer numero:")))

    num = num1,num2,num3

    print(sorted(num))

def CalculadoraBasica():
    
    num1 = float(input("Numero 1:"))
    print("Numero 2:")
    num2 = input()
    num2 = float(num2)
    operador = input("Tria l'operador:")

    if operador=="+":
        print(num1 + num2)
    elif operador=='-':
        print(num1 - num2)
    elif operador=='*':
        print(num1 * num2)
    elif operador=='/' and num2 != 0:
        print(num1 / num2)
    else:
        print ("Introdueix l'operador")

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
        CalculadoraBasica()
    elif (tria == '7'):
        JocEndevinaNumero()
    elif (tria == '8'):
        ConversorFarenheitCelcius()
    elif (tria == '9'):
        ValidaData()
    elif (tria == '10'):
        AreaTriangle()
    elif (tria == '11'):
        DiesPassats()
    elif (tria == '12'):
        CalculOperacio()
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


