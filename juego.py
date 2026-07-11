import json
import sistema as ss
from preguntas import lista_dic_preguntas


# Bucle principal del juego. Son 10 preguntas, dos de cada tipo.
def juego_play(
    usua_resp,
):  # usua_resp en una lista con info del jugador, por ahora solo ocupo su nombre.
    print(
        f"\nGracias por jugar ~~ {usua_resp[1]} ~~\nAhora veremos si realmente conoces al Ale:"
    )
    puntaje_total = 0
    for i in range(0, 10):
        id_pregunta = i + 1
        # [texto, tipo, puntos]
        pregunta_data = lista_dic_preguntas[i][id_pregunta]

        print(f"\n{pregunta_data[0]}")

        # mando tipo y respuesta
        resultado = ss.resp(id_pregunta, pregunta_data[1])

        pts = ss.validacion(resultado, pregunta_data[1], pregunta_data[2])

        print(f"\n--------> Ganas: {pts} puntos <--------")
        puntaje_total += pts
        print(f"\n******** Total: {puntaje_total} puntos ********")
        input("\n([])")

    ss.finalizar_juego(usua_resp, puntaje_total)
    ss.escribir_mensaje(usua_resp[1], puntaje_total)


def puntajes():
    with open("puntajes.json", "r") as archivo:
        puntajes = json.load(archivo)
    print("\n::::::::::¿Quién conoce mejor a Alejandro?:::::::::::")
    print("\nPuntajes máximos:")
    for a, b in puntajes.items():
        print(f"\n{a}: {b[0]} puntos - Jugado el {b[1]}).")
    print("\n---------------------------------------------")
    input("\n([])")


def instrucciones():
    print(
        """
        -------------------------------------------------------
        INSTRUCCIONES DEL JUEGO
        -------------------------------------------------------
        1. El juego consta de 10 preguntas, dos de cada tipo.
        2. Cada pregunta tiene un puntaje diferente según la respuesta.
        3. Puedes usar comodines para ayudarte en las preguntas.
        4. Al final del juego, tu puntaje será guardado.
        5. ¡Diviértete y buena suerte!
        -------------------------------------------------------
        """
    )
    input("\n([])")


def mensajes():
    with open("mensajes.json", "r") as archivo:
        mensajes = json.load(archivo)
    print("\n::::::::::Mensajes para Alejandro:::::::::::")
    for a, b in mensajes.items():
        print(f"\n{b[0]}")
        print(f"---------->Atentamente: {a}")
        print(f"(Puntaje: {b[1]}, Fecha: {b[2]})")
        print("\n---------------------------------------------")
    input("\n([])")
