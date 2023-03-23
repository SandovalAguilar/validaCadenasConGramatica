from itertools import count
import re
alfabeto= []
nombre= "yozedh gc"
matricula= "0123456"

def analizar():
    patron = re.compile('\A(0123456)(gc)+(0123456)((cg){2})+((yozedhyozedh)\Z)')
    patrongm = re.compile('\A(0123456)(gc)+(0123456)')
    patronmg = re.compile('(0123456)((cg){2})*((yozedhyozedh)\Z)')
    cadena = input("\nTeclea una cadena= ")
    encocadena= patron.search(cadena)
    encols= str(patrongm.match(cadena))
    encosl= str(patronmg.search(cadena))

    contarls= encols.count('gc')
    contarsl= encosl.count("cg")


    if (contarls >= 1) and (encocadena != None) and ( contarsl >= 1) and (contarls*2 == contarsl):
        print("\nCadena válida")
    else:
        print("\nCádena inválida")

def alfab():
    for i in nombre:
        num= alfabeto.count(i)
        if num == 0:
            alfabeto.append(i)

    for i in matricula:
        num= alfabeto.count(i)
        if num == 0:
            alfabeto.append(i)
    a= alfabeto.count(" ")
    if a != 0:
        alfabeto.remove(" ")
    print("El abecedario completo es:",alfabeto)

romper = 1

while (romper != 2):
    alfab()
    analizar()
    romper = int(input("\n¿Desea ingresar otra cadena?\n\n    Teclea 1 si quiere ingresar más cadenas:\n\n    Teclea cualquier cadena o dígito para finalizar el programa:    "))
    if (romper == 2) or (romper == 1):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    else:
        break 
    