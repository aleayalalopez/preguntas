from datetime import datetime
import texto_comodin as tc
import guardado as gd


comodin_disponibles = {
    "50": "Elimina 2 alternativas incorrectas",
    "22": "Dobla el puntaje que saques en esta pregunta",
    "PS": "Avanzas a la sguiente preguntas, obtienes 2 puntos",
}


def arranque():
    print("Iniciando el juego, por favor espere...")
    print(
        "\n \n \n Cada vez que veas este simbolo  ([])  significa que debes presionar enter para continuar"
    )
    input("\n([])")


def menu():
    a = []
    print("""
*****************************************************************
*                 ¿CUANTO CONOCES A ALEJANDRO?                  *
*****************************************************************          
                1 = INICIAR   >>>
                2 = PUNTAJES  + -
                3 = INSTRUCCIONES [] 
                4 = MENSAJES  <3
                5 = Apagar juego     <-[
    
    """)
    resp = input("¿Qué quieres hacer?----->")
    a.append(resp)
    while resp not in ["1", "2", "3", "4", "5"]:
        print("\n ERROR - Opción no válida. Intenta de nuevo.")
        resp = input("¿Qué quieres hacer?----->")
        a[0] = resp
    if resp == "1":
        nombre_usuario = input("Elije un nombre: ")
        a.append(nombre_usuario)
        input("\n([])")
    elif resp in ["2", "3", "4"]:
        pass

    return a


# respuesta, tipo de pregunta, puntajes
def validacion(rd, t, p):
    r = rd[0]
    multiplicador = rd[1]
    puntaje = 0
    if r == "PS":
        return 2
    elif t in ("sm", "rg"):
        try:
            puntaje = int(p[int(r)])  # p debe ser un int, porque debe ser un índice
        except (ValueError, IndexError, TypeError):
            print("ERROR - Respuesta no válida")
    elif t == "uc":
        c = 0
        if r[0:2] in p:
            c += 1
        if r[3:5] in p:
            c += 1
        if r[6:8] in p:
            c += 1
        if c == 0:
            puntaje = -2
        elif c == 1:
            puntaje = 0
        elif c == 2:
            puntaje = 1
        elif c == 3:
            puntaje = 4
    elif t == "vf":
        c = 0
        if r[0] == p[0]:
            c += 1
        if r[1] == p[1]:
            c += 1
        if r[2] == p[2]:
            c += 1
        if c == 0:
            puntaje = -2
        elif c == 1:
            puntaje = 0
        elif c == 2:
            puntaje = 1
        elif c == 3:
            puntaje = 4
    elif t == "cc":
        c = 0
        if r[0] in p:
            c += 1
        if r[1] in p:
            c += 1
        if r[2] in p:
            c += 1
        if c == 0:
            puntaje = -2
        elif c == 1:
            puntaje = 0
        elif c == 2:
            puntaje = 1
        elif c == 3:
            puntaje = 4
    if multiplicador == 2:  # si se usó el comodín de 22, se dobla el puntaje
        puntaje *= 2
    return puntaje


def usar_comodin(id_pregunta, tipo):
    print(f"::::: Has Usadao el Comidín {tipo} :::::")
    tc.comodin(id_pregunta, tipo)
    if tipo in comodin_disponibles:
        del comodin_disponibles[tipo]


def resp(id_pregunta, tipo_pregunta):
    print("\nComodines Disponibles:")
    for a, b in comodin_disponibles.items():
        print(f"[{a}] : {b}")
    respuesta_ok = False
    data_retorno = ["", 1]
    while not respuesta_ok:
        resp_i = input("\nSeleccione su respuesta o use un comodín---->").upper()
        if resp_i in comodin_disponibles:
            usar_comodin(id_pregunta, resp_i)
            if resp_i == "PS":
                data_retorno[0] = "PS"
                return data_retorno
            if resp_i == "22":
                data_retorno[1] = 2
        else:
            if tipo_pregunta == "sm" and resp_i in [str(n) for n in range(1, 11)]:
                respuesta_ok = True
            elif tipo_pregunta == "rg" and resp_i in "ABCDEFGHIJ":
                respuesta_ok = True
            elif tipo_pregunta == "uc" and len(resp_i) == 8:
                respuesta_ok = True
            elif tipo_pregunta == "vf" or tipo_pregunta == "cc" and len(resp_i) == 3:
                respuesta_ok = True
            else:
                print(
                    "\n ERROR - Formato no válido o comodín ya usado. Intenta de nuevo."
                )
    data_retorno[0] = resp_i
    return data_retorno


def finalizar_juego(usua_resp, puntaje_total):
    fecha_jeugo = datetime.now().strftime("%d/%m/%Y")
    gd.guarda_puntaje(usua_resp, puntaje_total, fecha_jeugo)
    print(
        f"\nGracias por jugar ~~ {usua_resp[1]} ~~\nTu puntaje final es: {puntaje_total}"
    )
    input("\n([])")


def escribir_mensaje(nombre_usuario, puntaje_total):
    print("\nEscribe un mensaje para Alejandro:")
    nombre = nombre_usuario
    puntaje = puntaje_total
    mensaje = input("\nQuerido Alejandro: ")
    fecha_mensaje = datetime.now().strftime("%d/%m/%Y")
    info_mensaje = {nombre: [mensaje, puntaje, fecha_mensaje]}
    gd.guardar_mensaje(info_mensaje)
