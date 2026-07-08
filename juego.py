# import json
import sistema as ss
from preguntas import lista_dic_preguntas

# list_dic_pre = tp.lista_dic_preguntas
# p = list_dic_pre[2]


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


"""

info_usuario = {}


# info_usuario.setdefault(nombre_usuario, puntaje)

with open("puntajes.json", "r") as archivo:
    puntajes = json.load(archivo)

puntajes.update(info_usuario)

with open("puntajes.json", "w") as jason_dic:
    json.dump(puntajes, jason_dic)

print(" ")
for a, b in puntajes.items():
    print(f"Usuario: {a}={b} puntos ")

"""
