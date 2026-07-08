mensajes = {
    1: {
        "50": "Ale dice >>> Me encanta la pizza, pero no me gustan todas.",
        "22": "Ale dice >>> No me sorpende, es muy fácil esta respuesta.",
        "PS": "Ale dice >>> No lo puedo creer :( ",
    },
    2: {
        "50": "Ale dice >>> No me encanta ni lo odio, estoy entre el 2 y el 6.",
        "22": "Ale dice >>> Me gusta tu confianza.",
        "PS": "Ale dice >>> ¿En serio? Esperaba más de ti.",
    },
    3: {
        "50": "Ale dice >>> Lo mio no es lo dulce. Descarta el manjar y la miel.",
        "22": "Ale dice >>> ¡JA! al parecer me conoces muy bien.",
        "PS": "Ale dice >>> Si pasas en esta, tendrás problemas más adelante.",
    },
    4: {
        "50": "Ale dice >>> Mi color favorito es el rojo y no me gusta el vino.",
        "22": "Ale dice >>> Bien jugado, esta es la oportunidad de sumar",
        "PS": "Ale dice >>> ¡Uff! Que mal",
    },
    5: {
        "50": "Ale dice >>> V. Jara, B. Eilish, Dire Straits, D Lipa y La oreja de Van Gogh me Encantan",
        "22": "Ale dice >>> Espero que sepas lo que haces",
        "PS": "Ale dice >>> Vamos, esto no era dificil.",
    },
    6: {"50": "Ale dice >>>", "22": "Ale dice >>>", "PS": "Ale dice >>>"},
    7: {"50": "Ale dice >>>", "22": "Ale dice >>>", "PS": "Ale dice >>>"},
    8: {"50": "Ale dice >>>", "22": "Ale dice >>>", "PS": "Ale dice >>>"},
    9: {"50": "Ale dice >>>", "22": "Ale dice >>>", "PS": "Ale dice >>>"},
    10: {"50": "Ale dice >>>", "22": "Ale dice >>>", "PS": "Ale dice >>>"},
}


# p= id_pregunta (int), c= tipo comodin (str)
def comodin(p, c):
    try:
        mensaje = mensajes[p][c]
        print(f"\n{mensaje}")
    except KeyError:
        print("\nAle dice >>> No tengo nada que deicir")
