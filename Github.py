def AreaTriangle():

    base= float(input("Introdueix la base del triangle: "))
    altura= float(input("Introdueix l'alçada del triangle: "))

    area= base*altura
    area2= area/2

    perimetre= ((base+altura)*2)/2

    print("L'àrea del triangle es ", area2, "i el seu perimetre es ", perimetre)

def DiesPassats():
    
    import datetime
    datanaixementdia = int(input("Dia en el que vas nèixer:"))
    datanaixementmes = int(input("Mes de naixement:"))
    datanaixementany = int(input("Any de naixement:"))

    dataActual = datetime.date.today()
    #print(dataActual)
    #print(type.dataActual)

    print("dia", dataActual.day, "mes", dataActual.month, "any", dataActual.year)

    diespassats = dataActual.day - datanaixementdia
    mesospassats = dataActual.month - datanaixementmes
    anyspassats = dataActual.year - datanaixementany

    resultatfinal = diespassats + mesospassats*30 + anyspassats*360

    print("des de que vas nèixer, han passat", resultatfinal, "dies.")
    
def CalculOperacio():
    
    operand1 = float(input("Introdueix el primer número: "))
    operand2 = float(input("Introdueix el segon número: "))
    operador = input("Introdueix un operador: ")

    if operador == "+" or operador == "-" or operador == "" or operador == "/" :

        if operador == "+":
            print(operand1 + operand2)

        if operador == "-":
            print(operand1 - operand2)

        if operador == "":
            print(operand1 * operand2)

        if operador == "/":
            print(operand1 / operand2)

    else :
        print("El caràcter introduït no és un operador")
