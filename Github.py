
#DECLARACIÓ DE LES FUNCIONS

def MenuOpcions():
    print("MENÚ D'OPCIONS:")
    print("0- SORTIR DEL PROGRAMA")
    print("1- VERIFICAR NOMBRES PRIMERS ")
    print("2- DIBUIXAR UN TAULELL D'ESCACS")
    print("3- ARRIBARÀS AL DESTÍ?")


def NombresPrimers():
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
    consum = (float(input("Introdueix el consum mitjà del teu vehicle: ")))
    dipòsit = (float(input("Introdueix els litres restants dins el teu dipòsit: ")))
    distanciaDestí = (float(input("Introdueix la distància entre el punt d'inici i el destí: ")))

    r = dipòsit / consum

    if r > distanciaDestí:
        print("No arribaràs al teu destí")

    else:
        print("Arribaràs al teu destí")

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
    else: 
        print("ERROR, torna a intentar;")
    print("TORNANT AL MENÚ")
    tria = input("ESCULL UNA OPCIÓ: ")

    
    
