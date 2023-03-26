'''
-----------------------------
Evidencia de Aprendizaje II
Teoria de Automatas
Equipo III
-----------------------------
'''

# Librerias
import re 
import os
from itertools import count

# Variables Globales
nombresPredeterminados = "Mauricio Leonardo"
apellidosPredeterminados = "Ponce Barragan"
matriculaPredeterminada = "2003929"

# Variables Globales de prueba
'''
nombresPredeterminados = "Yozedh Jahday"
apellidosPredeterminados = "Guerrero Ceja"
matriculaPredeterminada = "0123456"
'''

# Funciones para generar conjuntos e iniciales
def generaIniciales(apellidos):
    palabras = apellidos.lower().split(' ')
    inicialesApellidos = ''

    for i in palabras:
        inicialesApellidos += i[0]
    
    return inicialesApellidos

def generaInicialesInversa(inicialesApellidos):
    return inicialesApellidos[::-1]

def encuentraPrimerNombre(nombreCompleto):
    return nombreCompleto.split(' ')[0]

def validaCadenas(inicialesApellidos, inicialesInversa, matricula, primerNombre, cadena):
    patron = re.compile('\A(' + matricula + ')(' + inicialesApellidos + ')+(' + matricula + ')((' + inicialesInversa + '){2})+((' + primerNombre * 2 + ')\Z)')    
    patronIniciales = re.compile('\A(' + matricula + ')(' + inicialesApellidos + ')+(' + matricula + ')')
    patronInicialesInversa = re.compile('(' + matricula + ')((' + inicialesInversa + '){2})*((' + primerNombre * 2 + ')\Z)')
    buscaCadena = patron.search(cadena)
    matchIniciales = str(patronIniciales.match(cadena))
    matchInicialesInversa = str(patronInicialesInversa.search(cadena))

    contarIniciales = matchIniciales.count(inicialesApellidos)
    contarInicialesInversa = matchInicialesInversa.count(inicialesInversa)

    if (contarIniciales >= 1) and (buscaCadena != None) and (contarInicialesInversa >= 1) and (contarIniciales * 2 == contarInicialesInversa):
        print("La cadena es valida.")
    else:
        print("La cadena es invalida.")

# Programa principal
def main():
    inicialesApellidos = generaIniciales(apellidosPredeterminados)
    inicialesInversa = generaInicialesInversa(inicialesApellidos)
    matricula = matriculaPredeterminada
    primerNombre = encuentraPrimerNombre(nombresPredeterminados).lower()
    
    centinela = True

    while(centinela):
        os.system('cls||clear')

        print("======   Teoria de Automatas: Evidencia II   ======")
        print("======               Equipo III              ======")
        print("---------------------------------------------------")
        print("Nombre completo: " + nombresPredeterminados + " " + apellidosPredeterminados)
        print("Matricula: " + matriculaPredeterminada)
        print("Gramatica: L = { i (w)^n i (w ^ I)^(2n) j^2 }")
        print("w = " + inicialesApellidos)
        print("i = " + matriculaPredeterminada)
        print("w^I = " + inicialesInversa)
        print("j = " + primerNombre)
        print("---------------------------------------------------")
        print("Ingrese una cadena para ser validada:")

        cadena = input()

        print("---------------------------------------------------")
        validaCadenas(inicialesApellidos,
                      inicialesInversa,
                      matricula,
                      primerNombre,
                      cadena)
        print("---------------------------------------------------")
        
        print("¿Desea ingresar otra cadena? [S/N]:")
        opcion = input()
        if opcion.upper() == 'S':
            centinela = True
        elif opcion.upper() == 'N':
            centinela = False
        else:
            print("Opcion incorrecta. Ingrese una opcion valida.")
            input("Presione cualquier tecla para continuar...")

if __name__=="__main__":
    main()

