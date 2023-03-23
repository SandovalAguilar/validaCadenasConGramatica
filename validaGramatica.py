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
nombrePredeterminado = "Yozedh Jahday Guerrero Ceja"
matriculaPredeterminada = "0123456"

# Funciones para generar conjuntos e iniciales
def generaIniciales(apellidos):
    palabras = apellidos.lower().split(' ')
    inicialesApellidos = ''

    for i in palabras:
        inicialesApellidos += i[0]
    
    return inicialesApellidos

def generaDigitos(matricula):
    matriculaConjunto = list(set(matricula))
    digitos = ''

    for i in matriculaConjunto:
        digitos += (i)

    return digitos

def inicialesInversa(inicialesApellidos):
    return inicialesApellidos[::-1]

def primerNombre(nombreCompleto):
    return nombreCompleto.split(' ')[0]

def analizaCadenas():
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

# Por hacer: comprobar apellidos

def imprimeConjuntos(nombre, matricula, apellidos):
    print("--------------------------------------------------")
    print("Nombre ingresado: " + nombre)
    print("Matricula ingresada: " + matricula)
    print("Conjuntos generados a partir del nombre y matricula:")
    print("w = " + generaIniciales(apellidos))
    print("i = " + generaDigitos(matricula))
    print("w^i = " + inicialesInversa(generaIniciales(apellidos)))
    print("j = " + primerNombre(nombre))
    print("--------------------------------------------------")

# Programa principal
def main():
    imprimeConjuntos(nombrePredeterminado, matriculaPredeterminada, apellidos = "Guerrero Ceja")
    
if __name__=="__main__":
    main()

