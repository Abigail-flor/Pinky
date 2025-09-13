#Bienveida
print("¡Bienvenido al programa para crear tu propia lista!")
#Ciclo infinito hata que el usuario decida salir manualmente
while True:
    x = str(input("¿Desea crear una lista?: "))
    if x.lower()=="si":
        print("\n***OPCIONES***")
        print("1.-Números\n2.-Texto\n3.-Salir")
        y = int(input("¿De que tipo? (seleccionar  1 - 3): "))
        if y==1:
           numerica = []
           while True:
               numero = float(input("Ingrese un número"))
               numerica.append(numero)
               agregar = str(input("¿Desea agregar otro número?: "))
               if agregar.lower()!="si":
                    print(numerica)
                    print("\n***Opciones de lista NUMERICAS***")
                    print("1.-Agregar valores a la lista.")
                    print("2.-Eliminar valor (sea or índice o por valor)")
                    print("3.-Ordenar la lista modificándola directamente.")
                    print("4.-Ordenar la lista generando una nueva lista ordenada.")
                    print("5.-Verificar si un elemento específico se encuentra en la lista.")
                    print("6.-Calcular el valor máximo, mínimo, suma y promedio.")
                    print("7.-NO, quiero salir.")
                    z = int(input("\nSeleccione su siguiente acción"))
                    if z==1:
                        while True:
                            numero = float(input("Ingrese un número"))
                            numerica.append(numero)
                            agregar = str(input("¿Desea agregar otro número?: "))
                            if agregar.lower()!="si":
                                print(numerica)
                                print("Ha acabado su lista")
                                break
                    elif z==2:
                        print(numerica)
                        while True:
                            print("\n***Opciónes***")
                            print("1.-Eliminar por Índice.")
                            print("2.-Eliminar por Valor.")
                            print("3.-Salir.")
                            op = int(input("Ingrese la opcion que desee (1 - 3): "))
                            while True:
                                if op==1:
                                    print(numerica)
                                    while True:
                                        indice = int(input("Ingrese el índice del número que quiere eliminar: "))
                                        numerica.pop(indice)
                                        print(numerica)
                                        opcion = str(input("¿Desea eliminar otro número?: "))
                                        if opcion.lower()!="si":
                                            print(numerica)
                                            print("Así termino su lista")
                                            break
                                elif op==2:
                                    valor = float(input("Ingrese el índice que desea eliminar: "))
                                    numerica.remove(valor)
                                    print(numerica)
                                    eliminar = str(input("¿Desea eliminar otro número?: "))
                                    if eliminar.lower()!="si":
                                        print(numerica)
                                        print("Su lista esta terminada")
                                        break
                                else:
                                    print(numerica)
                                    print("Usted ha terminado su lista")
                                    break
                                break
                            print(numerica)
                            print("Usted ha terminado su lista")
                            break
                    elif z==3:
                        print(f"Lista vieja:\n{numerica}")
                        numerica.sort()
                        print(f"Su nueva lista es:\n{numerica}")
                    elif z==4:
                        print(f"Lista vieja:\n{numerica}")
                        numerica.sort(reverse=True)
                        print(f"Lista nueva:\n{numerica}")
                    elif z==5:
                        num = float(input("Ingrese el número que quiere buscar: "))
                        if num in numerica:
                            indices = [i for i, val in enumerate(numerica) if val == num]
                            print(f"El elemento {num} está en la lista en el/los índice(s): {indices}")
                        else:
                            print("No se encuentra ese elemento en la lista")
                    elif z==6:
                        print(f"Valor máximo: {max(numerica)}")
                        print(f"Valor mínimo: {min(numerica)}")
                        print(f"Suma de la lista: {sum(numerica)}")
                        print(f"Promedio: {sum(numerica)}/{len(numerica)}")
                    else:
                        print("Usted ha terminado su lista")
                        print(numerica)
                        break
           else:
                   print("Su lista terminada")
                   break
        elif y==2:
            textual = []
            while True:
               texto = input("Ingrese una palabra")
               textual.append(texto)
               agregar = str(input("¿Desea agregar otra palabra?: "))
               if agregar.lower()!="si":
                    print(textual)
                    print("\n***Opciones de lista TEXTUALES***")
                    print("1.-Agregar valores a la lista.")
                    print("2.-Eliminar valor (sea or índice o por valor)")
                    print("3.-Ordenar la lista modificándola directamente.")
                    print("4.-Ordenar la lista generando una nueva lista ordenada.")
                    print("5.-Verificar si un elemento específico se encuentra en la lista.")
                    print("6.-NO, quiero salir.")
                    z = int(input("\nSeleccione su siguiente acción"))
                    if z==1:
                        while True:
                            texto = input("Ingrese una palabra: ")
                            textual.append(texto)
                            agregar = str(input("¿Desea agregar otra palabra?: "))
                            if agregar.lower()!="si":
                                print(textual)
                                print("Ha acabado su lista")
                                break
                    elif z==2:
                        print(textual)
                        while True:
                            print("\n***Opciónes***")
                            print("1.-Eliminar por Índice.")
                            print("2.-Eliminar por Valor.")
                            print("3.-Salir.")
                            op = int(input("Ingrese la opcion que desee (1 - 3): "))
                            while True:
                                if op==1:
                                    print(textual)
                                    while True:
                                        indice = int(input("Ingrese el índice de la palabra que quiere eliminar: "))
                                        textual.pop(indice)
                                        print(textual)
                                        opcion = str(input("¿Desea eliminar otra palabra?: "))
                                        if opcion.lower()!="si":
                                            print(textual)
                                            print("Así termino su lista")
                                            break
                                elif op==2:
                                    valor = int(input("Ingrese el índice que desea eliminar: "))
                                    textual.remove(valor)
                                    print(textual)
                                    eliminar = str(input("¿Desea eliminar otra palabra?: "))
                                    if eliminar.lower()!="si":
                                        print(textual)
                                        print("Su lista esta terminada")
                                        break
                                else:
                                    print(textual)
                                    print("Usted ha terminado su lista")
                                    break
                                break
                            print(textual)
                            print("Usted ha terminado su lista")
                            break
                    elif z==3:
                        print(f"Lista vieja:\n{textual}")
                        textual.sort()
                        print(f"Su nueva lista es:\n{textual}")
                    elif z==4:
                        print(f"Lista vieja:\n{textual}")
                        textual.sort(reverse=True)
                        print(f"Lista nueva:\n{textual}")
                    elif z==5:
                        tex = input("Ingrese la palabra que quiere buscar: ")
                        if tex in textual:
                            indices = [i for i, val in enumerate(textual) if val == tex]
                            if indices:
                                print(f"El elemento '{tex}' está en la lista en el/los índice(s): {indices}")
                            else:
                                print("No se encuentra ese elemento en la lista")
                        else:
                            print("No se encuentra ese elemento en la lista")
                    else:
                        print("Usted ha terminado su lista")
                        print(textual)
                        break
    else:
        print("Usted ha salido del programa")
        break
