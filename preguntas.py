import texto_preguntas as tp

# lista con los tipos de pregunta. Son 2 de cada tipo
# sm: se elije uno de 4 alternativas
# rg: se elije un número del 1 al 10
# uc: unes conceptos pares
# vf: escribes v o f en tres oraciones
# cc: Elijes tres alternativas entre 10 posibles
tip = ("sm", "rg", "uc", "vf", "cc")

# diccionarios {N° de las pregguntas: [texto de las preguntas,tipo de pregunta,puntaje según la respuesta]}
lista_dic_preguntas = [
    {1: [tp.tx1, tip[0], ("null", 4, 0, -2, 2)]},
    {2: [tp.tx2, tip[1], ("null", -2, 0, 1, 2, 4, 2, 1, 0, -2, -2)]},
    {3: [tp.tx3, tip[2], ("A1", "B4", "C3")]},
    {4: [tp.tx4, tip[3], ("V", "F", "F")]},
    {5: [tp.tx5, tip[4], ("B", "D", "J")]},
    {6: [tp.tx6, tip[0], ("null", 0, 4, 1, -2)]},
    {7: [tp.tx7, tip[1], ("null", 2, 4, 2, 1, 0, -2, -2, -2, -2, -2)]},
    {8: [tp.tx8, tip[2], ("A2", "B3", "C4")]},
    {9: [tp.tx9, tip[3], ("V", "V", "F")]},
    {10: [tp.tx10, tip[4], ("A", "H", "I")]},
]

if __name__ == "__main__":
    pregunta_data = lista_dic_preguntas[0][1]
    print(pregunta_data)
