import os
import random
import time
puntos = 0

def elegir_palabra():
    palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            palabras.append(line)
    palabra_random = random.choice(palabras)
    return palabra_random

def adivinar_palabra():
    global puntos
    palabra_a_adivinar = elegir_palabra()
    palabra_a_adivinar = palabra_a_adivinar.replace("í", "i").replace("é", "e").replace("á", "a").replace("ó", "o").replace("ú", "u")
    palabra_a_adivinar = palabra_a_adivinar.upper()
    palabra_a_adivinar = palabra_a_adivinar.strip()
    palabra = list(palabra_a_adivinar)
    palabra_escondida = ["_ " for i in palabra]
    vidas = len(palabra) * 3
    letras_usadas = []

    while palabra != palabra_escondida and vidas > 0:
        os.system("clear")
        print("Adivina la palabra")
        print("""
Cada palabra que adivines suma un punto 
puntos: """ + str(puntos))
        print(""" 
Podes arriesgarte a escribir toda la palabra """)
        print(""" 
Tenes: """  + str(vidas) + " intentos")
        print("".join(palabra_escondida))
        print(""" 
Letras usadas: """  + str(letras_usadas))
        letra = input("""
Ingresa una letra o la palabra: """).upper()

        if letra.isalpha() == False:
            print("Desbes ingresar solo letras o la palabra")
            time.sleep(1.5)
            continue
        elif len(letra)>1 and letra == palabra_a_adivinar:
            os.system("clear")
            print(palabra_a_adivinar)
            print("Ganaste un viaje a Qatar!!")
            puntos += 2
            print("puntos: " + str(puntos))
            volver_a_jugar = input("presiona a para volver a jugar o culaquier letra para salir: ").upper()
            if volver_a_jugar == "A":
                adivinar_palabra()
            else:
                break

        vidas -=1
        if vidas == 0:
            os.system("clear")
            print("Game Over")
            print("La palabra es: " + palabra_a_adivinar)
            break

        if palabra.count(letra) == 1:
            posicion = palabra.index(letra)
            palabra_escondida.pop(posicion)
            palabra_escondida.insert(posicion,letra)

        elif palabra.count(letra) > 1:
            repetida = []
            for l in range(len(palabra)):
                if palabra[l] == letra:
                    repetida.append(l)
            for i in range(len(repetida)):
                posicion = repetida[i]
                palabra_escondida.pop(posicion)
                palabra_escondida.insert(posicion,letra)
            
        else:
            letras_usadas.append(letra)
            
        if palabra == palabra_escondida:
            os.system("clear")
            print(palabra_a_adivinar)
            print("Ganaste un viaje a Qatar!!")
            puntos += 1
            print("puntos: " + str(puntos))
            volver_a_jugar = input("presiona a para volver a jugar o culaquier letra para salir: ").upper()
            if volver_a_jugar == "A":
                adivinar_palabra()
            else:
                break

        
def run():
    adivinar_palabra()


if __name__ == '__main__':
    run()