'''
-----------------------------
Evidencia de Aprendizaje I
Teoria de Automatas
Equipo III
-----------------------------
'''

# Librerias
import re 
import os

# Variables Globales
nombrePredeterminado = "Alejandro Isai Avila"
matriculaPredeterminada = "1943548"

# Variables Globales de prueba
'''
nombrePredeterminado = "yazmany jahaziel guerrero ceja"
matriculaPredeterminada = "1339767"
'''

# Funciones para validar la matricula y el nombre ingresados por el usuario
def validaMatriculaIngresada():
    while(True):
        print("Ingrese una matricula: ")
        matriculaIngresada = input()

        if len(matriculaIngresada) == 7 and matriculaIngresada.isnumeric():
            return matriculaIngresada
        else:
            print(" - La matricula ingresada contiene al menos una letra o tiene menos de 7 elementos o mas.")
            False

def validaNombreIngresado():
    while(True):
        print("Ingrese un nombre: ")
        nombreIngresado = input()

        if nombreIngresado.replace(" ", "").isalpha():
            return nombreIngresado
        else:
            print("- El nombre ingresado contiene numeros o caracteres invalidos (*, ., /, etc.).")
            False

# Funciones para generar conjuntos e iniciales
def generaIniciales(nombre):
    palabras = nombre.lower().split(' ')
    iniciales = ''

    for i in palabras:
        iniciales += i[0]
    
    return iniciales

def generaAlfabeto(nombre, matricula):
    nombreConjunto = list(set(nombre.replace(" ", "").lower()))
    matriculaConjunto = list(set(matricula))
    alfabeto = ''

    for i in nombreConjunto + matriculaConjunto:
        alfabeto += (i + ",")

    return alfabeto

def generaDigitos(matricula):
    matriculaConjunto = list(set(matricula))
    digitos = ''

    for i in matriculaConjunto:
        digitos += (i + "|")

    return digitos

# Funcion para validar la cadena ingresada
def validaCadenas(cadena, digitos, alfabeto, iniciales, matricula):
    expresionRegular = "^(" + digitos[:-1] + ")([" + alfabeto + ".]*)((" + iniciales + "){1,})([" + alfabeto + ".]*)(\.)(" + matricula + "$)"
    # expresionRegular = "^(" + digitos[:-1] + ")([" + alfabeto + ".]*)((" + iniciales + "){1,})([" + alfabeto + "]*)\." + matricula
    # print(expresionRegular)
    validaCadena = re.search(expresionRegular, cadena)
    validaPuntosConsecutivos = re.search("\.{2,}", cadena)

    if validaCadena and not(validaPuntosConsecutivos):
        print("La cadena es valida.")
    else:
        print("La cadena es invalida.")

# Funciones para generar el menu de opciones
def imprimeMenu():
    os.system('cls||clear')
    
    print("====== Teoria de Automatas: Evidencia I ======")
    print("======            Equipo III            ======")
    print("\n")
    print("[1] -- Validar cadena a partir de la matricula\n y el nombre por defecto.")
    print("[2] -- Validar cadena a partir de la matricula\n y el nombre ingresados por el usuario.")
    print("[3] -- Salir del programa.")

def primerOpcion():
    centinela = True
    
    while(centinela):
        os.system('cls||clear')
        print("- Nombre por defecto: Alejandro Isai Avila")
        print("- Matricula por defecto: 1943548")
        print("- Alfabeto generado a partir del nombre\ny matricula:")
        print("Σ = {" + generaAlfabeto(nombrePredeterminado, matriculaPredeterminada)[:-1] + "}")
        print("----------------------------------------")
        print("Ingrese una cadena para validar:")
        cadena = input()
                
        alfabeto = generaAlfabeto(nombrePredeterminado, matriculaPredeterminada)
        digitos = generaDigitos(matriculaPredeterminada) 
        iniciales = generaIniciales(nombrePredeterminado)
        print("----------------------------------------")
        validaCadenas(cadena, digitos, alfabeto, iniciales, matriculaPredeterminada)

        print("----------------------------------------")
        print("¿Desea ingresar otra cadena? [S/N]:")
        opcion = input()
        
        if opcion.upper() == 'S':
            centinela = True
        elif opcion.upper() == 'N':
            centinela = False
        else:
            print("Opcion incorrecta. Ingrese una opcion valida.")
            input("Presione cualquier tecla para continuar...")

def segundaOpcion():
    centinela = True
    os.system('cls||clear')
    matricula = validaMatriculaIngresada()
    nombre = validaNombreIngresado()

    while(centinela):
        print("----------------------------------------")
        print("Nombre ingresado: " + nombre)
        print("Matricula ingresada: " + matricula)
        print("Alfabeto generado a partir del nombre\ny matricula:")
        print("Σ = {" + generaAlfabeto(nombre, matricula)[:-1] + ",.}")
        print("----------------------------------------")
        print("Ingrese una cadena para validar:")
        cadena = input()

        alfabeto = generaAlfabeto(nombre, matricula)
        digitos = generaDigitos(matricula) 
        iniciales = generaIniciales(nombre)
        validaCadenas(cadena, digitos, alfabeto, iniciales, matricula)

        print("----------------------------------------")
        print("¿Desea ingresar otra cadena? [S/N]:")
        opcion = input()
        
        if opcion.upper() == 'S':
            centinela = True
            os.system('cls||clear')
        elif opcion.upper() == 'N':
            centinela = False
        else:
            print("Opcion incorrecta. Ingrese una opcion valida.")
            input("Presione cualquier tecla para continuar...")
            os.system('cls||clear')

def menuDeOpciones():
    while(True):
        imprimeMenu()
        
        opcion = ''
        try:
            opcion = int(input('Elige una opcion: '))
        except:
            print("Opcion incorrecta. Ingrese un numero valido.")
        
        if opcion == 1:
            primerOpcion()
        elif opcion == 2:
            segundaOpcion()
        elif opcion == 3:
            exit()
        else:
            print("Opcion incorrecta. Ingrese un numero valido.")

# Programa principal
def main():
    menuDeOpciones()
    
if __name__=="__main__":
    main()

