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
'''
nombrePredeterminado = "Alejandro Isai Avila"
matriculaPredeterminada = "1943548"
'''

# Variables Globales de prueba
nombresPredeterminados = "Yozedh Jahday"
apellidosPredeterminados = "Guerrero Ceja"
matriculaPredeterminada = "0123456"

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

def validaCadenas(inicialesApellidos, inicialesInversa, matricula, primerNombre):
    patron = re.compile('\A(' + matricula + ')(' + inicialesApellidos + ')+(' + matricula + ')((' + inicialesInversa + '){2})+((' + primerNombre * 2 + ')\Z)')    
    patrongm = re.compile('\A(' + matricula + ')(' + inicialesApellidos + ')+(' + matricula + ')')
    patronmg = re.compile('(' + matricula + ')((' + inicialesInversa + '){2})*((' + primerNombre * 2 + ')\Z)')
    cadena = input("\nTeclea una cadena= ")
    encocadena= patron.search(cadena)
    encols= str(patrongm.match(cadena))
    encosl= str(patronmg.search(cadena))

    contarls= encols.count(inicialesApellidos)
    contarsl= encosl.count(inicialesInversa)

    if (contarls >= 1) and (encocadena != None) and ( contarsl >= 1) and (contarls*2 == contarsl):
        print("\nCadena válida")
    else:
        print("\nCádena inválida")

# Programa principal
def main():
    
    inicialesApellidos = generaIniciales(apellidosPredeterminados)
    inicialesInversa = generaInicialesInversa(inicialesApellidos)
    matricula = matriculaPredeterminada
    primerNombre = encuentraPrimerNombre(nombresPredeterminados).lower()

    print(inicialesApellidos,
          inicialesInversa,
          matricula,
          primerNombre)
 
    validaCadenas(inicialesApellidos,
                   inicialesInversa,
                   matricula,
                   primerNombre)

if __name__=="__main__":
    main()

