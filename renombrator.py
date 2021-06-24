import os


def renombrar(arch_renombrados=0):
    resguardo = open("resguardo.txt", "a+")
    for archivo in os.listdir("."):
        print("Analizando " + archivo)
        cant = 0
        for i in range(len(archivo)):
            if archivo[i] in " 0123456789-" and archivo[-3:].lower() == "mp3":
                cant += 1
                continue
            else:
                if cant > 0:
                    print("Encontrado " + archivo + " renombrando " + archivo[cant:len(archivo)])
                    resguardo.write(archivo + "%" + archivo[cant:len(archivo)] + "\r")
                    os.rename(archivo, archivo[cant:len(archivo)])
                    arch_renombrados += 1
                    break
                else:
                    break
    resguardo.close()
    return arch_renombrados


def revertir():
    revierto = open("resguardo.txt", "r")
    linea = True
    while linea:
        linea = revierto.readline()
        comando = linea.split("%")
        if len(comando) > 1:
            os.rename(comando[1][0:len(comando[1])-1], comando[0])
    revierto.close()
    return "Se revirtio el cambio de nombre"


opcion = ""
while opcion != "03":
    print("RENOMBRATOR")
    print("01-Renombrar")
    print("02-Volver Atras")
    print("03-Salir")
    opcion = input("Elija una Opcion:")
    if opcion not in ["01", "02", "03"]:
        print("Elija entre 01 y 03")
        continue
    elif int(opcion) == 1:
        if "resguardo.txt" in os.listdir("."):
            print("Ya existe un archivo de resguardo!!!")
            respuesta = input("Debe borrar el archivo antes de hacer un cambio? borra? si/no:")
            while respuesta in ["si", "no"]:
                if respuesta == "si":
                    os.remove("resguardo.txt")
                    break
                elif respuesta == "no":
                    break
            else:
                respuesta = input("La respuesta debe ser si o no:")
                continue
        renombrados = renombrar()
        print("Se renombraron " + str(renombrados) + " archivos")
        input("Presione Enter para continuar.......")
    elif int(opcion) == 2:
        print(revertir())
    else:
        continue
