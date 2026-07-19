while True:
    nom_us=input("Introduzca su nombre: ").title().strip()
    con_num=False
    for numero in "0123456789":
        if nom_us.find(numero)!=-1:
            con_num=True
            break
    if con_num:
        print("Nombre no válido porque contiene números.")
        continue
    else:
        break

saldo=1000
while True:
    print("=".center(20,"="))
    print("MENÚ".center(20,"="))
    print("=".center(20,"="))

    print(f"\nHola usurio {nom_us}. Bienvenido al menú de opciones.\n")
    try:
        op_1=int(input("""Elija el número de una de las opciones siquientes:\n
    \t1-Ver saldo
    \t2-Depositar dinero
    \t3-Retirar dinero
    \t4-Salir\n"""))
        
        if op_1==1:
            print(f"\nSu saldo actual es de {saldo}\n")
            continue
        elif op_1==2:
            deposito=int(input("¿Cuánto quieres depositar?: "))
            if deposito<=0:
                print("El depósito tiene que ser mayor a 0")
                continue
            else:
                saldo+=deposito
                print(f"Tu saldo actual es de {saldo}")
        elif op_1==3:
            print(f"Tu saldo actual es de {saldo}.",end="")
            retiro=int(input("¿Cuánto dinero desea retirar? "))
            if retiro>saldo:
                print("Saldo insuficiente.")
                continue
            elif retiro<1:
                print("Retiro debe de ser mayor a 0")
                continue
            else:
                saldo-=retiro
                print(f"Tu saldo actual es de {saldo}")
        elif op_1==4:
            nom_us=nom_us[:2]+nom_us[-1]
            print(f"Gracias por usar nuestro cajero usuario {nom_us}. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
    except ValueError:
        print("Elección inválida.")
        continue
    
