LINEA = "-"*30
TRATAMIENTO1 = 250_000
TRATAMIENTO2 = 475_000
TRATAMIENTO3 = 800_000
NUMEROCUOTAS = 12
CONT1 = 0
CONT2 = 0
CONT3 = 0
TRATAMIENTO1PAGO = 0
TRATAMIENTO2PAGO = 0
TRATAMIENTO3PAGO = 0
DESC1 = 0,15
DESC2 = 0.10
DESC3 = 0.05
totalpago = 0
predescuento = 0
op1 = 0
op2 = 0

while op1 != 3:
    print("MENU")
    print("1) Cotizacion.")
    print("2) Renunciar.")
    print("3) Salir")
    while True:
        try:
            op1 = int(input("Ingrese la opcion: "))
            if op1 == 1 or op1 == 2:
                break
            else:
                raise ValueError()
        except ValueError:
            print("La opcion ingresada es invalida...")
                
    while True:
        if op1 == 1:
            while op2 != 5:
                print("Indique que tratamiento necesita: ")
                print("1) Carillas Porcelana $250.000")
                print("2) Implantes Dentales $475.000")
                print("3) Ortodoncia Brackets $800.000")
                print("4) Realizar cotizacion.")
                print("5) Salir.")
                try:
                    op2 = int(input("Ingrese la opcion: "))
                    if 1 <= op1 <= 4:
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    print("opcion ingresada es invalida....")

            if op2 == 1:
                CONT1 += 1
            elif op2 == 2:
                 CONT2 += 1
            elif op2 == 3:
                op2 += CONT3
            elif op2 == 4:
                print("Que tipo de descuento tiene?")
                print("1) Trabajador Auxiliar.")
                print("2) Trabajador Administrativo.")
                print("3) Trabajador Docente.")
                
                while predescuento != 5:
                    try:
                        predescuento = int(input("Ingrese la opcion: "))
                        TRATAMIENTO1PAGO = TRATAMIENTO1 * CONT1
                        TRATAMIENTO2PAGO = TRATAMIENTO2 * CONT2
                        TRATAMIENTO3PAGO = TRATAMIENTO3 * CONT3
                        totalpago = TRATAMIENTO1PAGO + TRATAMIENTO2PAGO + TRATAMIENTO3PAGO
                        totaldescuento = 0
                        descuento3 = totalpago * DESC3
                        if predescuento < 0:
                            raise ValueError()
                        elif predescuento == 1:
                            print(LINEA)
                            print("\t\tCotizacion")
                            print(LINEA)
                            print(f"--> {CONT1} tratamiento(s) Carillas porcelana {TRATAMIENTO1PAGO}")
                            print(f"--> {CONT2} tratamiento(s) Carillas porcelana {TRATAMIENTO2PAGO}")
                            print(f"--> {CONT3} tratamiento(s) Carillas porcelana {TRATAMIENTO3PAGO}")
                            print(LINEA)
                            print(f"Subtotal: {totalpago}")
                            descuento2 = totalpago * DESC1
                            print(f"Descuento 10%: {descuento2}")
                            print(LINEA)
                            totaldescuento = totalpago - descuento2
                            print(f"Total = {totaldescuento}")
                            print(LINEA)
                            cuotas = totaldescuento / NUMEROCUOTAS
                            print(f"Son en 12 cuotas: {cuotas}")
                            print("")
                            print("Sonria bonitoooo!!!")
                        elif predescuento == 2:
                            print(LINEA)
                            print("\t\tCotizacion")
                            print(LINEA)
                            print(f"--> {CONT1} tratamiento(s) Carillas porcelana {TRATAMIENTO1PAGO}")
                            print(f"--> {CONT2} tratamiento(s) Carillas porcelana {TRATAMIENTO2PAGO}")
                            print(f"--> {CONT3} tratamiento(s) Carillas porcelana {TRATAMIENTO3PAGO}")
                            print(LINEA)
                            print(f"Subtotal: {totalpago}")
                            descuento2 = totalpago * DESC2
                            print(f"Descuento 10%: {descuento2}")
                            print(LINEA)
                            totaldescuento = totalpago - descuento2
                            print(f"Total = {totaldescuento}")
                            print(LINEA)
                            cuotas = totaldescuento / NUMEROCUOTAS
                            print(f"Son en 12 cuotas: {cuotas}")
                            print("")
                            print("Sonria bonitoooo!!!")
                            break
                        elif predescuento == 3:
                            print(LINEA)
                            print("\t\tCotizacion")
                            print(LINEA)
                            print(f"--> {CONT1} tratamiento(s) Carillas porcelana {TRATAMIENTO1PAGO}")
                            print(f"--> {CONT2} tratamiento(s) Carillas porcelana {TRATAMIENTO2PAGO}")
                            print(f"--> {CONT3} tratamiento(s) Carillas porcelana {TRATAMIENTO3PAGO}")
                            print(LINEA)
                            print(f"Subtotal: {totalpago}")
                            descuento2 = totalpago * DESC3
                            print(f"Descuento 5%: {descuento2}")
                            print(LINEA)
                            totaldescuento = totalpago - descuento2
                            print(f"Total = {totaldescuento}")
                            print(LINEA)
                            cuotas = totaldescuento / NUMEROCUOTAS
                            print(f"Son en 12 cuotas: {cuotas}")
                            print("")
                            print("Sonria bonitoooo!!!")
                            break
                    except ValueError:
                        print("Opcion ingresada es ivalida...")
                            
        elif op1 == 2:    
            totaldescuento = 0  
            break
        else:
            print("Adios.")
