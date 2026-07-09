import json


# guarda los tres puntajes más altos en un archivo json. Si el usuario ya existe, se actualiza su puntaje si es mayor al anterior.
def guarda_puntaje(usua_resp, puntaje_total):
    nombre_usuario = usua_resp[1]
    puntaje = puntaje_total
    with open("puntajes.json", "r") as archivo:
        datos_juego = json.load(archivo)

    datos_juego[nombre_usuario] = puntaje
    lista_ordenada = sorted(datos_juego.items(), key=lambda x: x[1], reverse=True)

    top_3_lista = lista_ordenada[:3]
    datos_juego = dict(top_3_lista)
    print(datos_juego)
    with open("puntajes.json", "w") as archivo:
        json.dump(datos_juego, archivo, indent=4)


def guardar_mensaje(info_mensaje):
    with open("mensajes.json", "r") as archivo:
        datos_mensajes = json.load(archivo)
    datos_mensajes.update(info_mensaje)
    with open("mensajes.json", "w") as archivo:
        json.dump(datos_mensajes, archivo, indent=4)
