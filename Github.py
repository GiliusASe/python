def AreaTriangle():

    base= float(input("Introdueix la base del triangle: "))
    altura= float(input("Introdueix l'alçada del triangle: "))

    area= base*altura
    area2= area/2

    perimetre= ((base+altura)*2)/2

    print("L'àrea del triangle es ", area2, "i el seu perimetre es ", perimetre)

def TipusTriangle():
    
    costat1 = float(input("Inserta el primer costat del triangle: "))
    costat2 = float(input("Inserta el segon costat del triangle: "))
    costat3 = float(input("Inserta el tercer costat del triangle: "))

    if costat1 == costat2 and costat2 == costat3:
        print("Aquest triangle és equilàter")
    else:
        if costat1 == costat2 or costat2 == costat3 or costat1 == costat3:
            print("Aquest triangle és iscòceles")
        else:
            print("Aquest triangle és escalè") 
    
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
