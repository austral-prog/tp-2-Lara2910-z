def change():
    expense = 23.75
    money = 100
    #Ejercicio 3
    vuelto = (money - expense)
    pesos = int(vuelto)
    cents = (vuelto - pesos)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    vuelto_salto = f"\nVuelto"
    print(vuelto_salto)
    pesos_salto = f"\nPesos:"
    print(pesos_salto)
    print(pesos)
    print("Centavos:")
    centavos = int(cents * 100)
    print(centavos)
