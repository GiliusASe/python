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
