import texto_preguntas as tx
import sistema as ss
import juego as j

# Inicio del juego

ss.arranque()
print(tx.tx0)
input("\n***** ([]) ****")
encenddio = True
while encenddio:
    usua_resp = ss.menu()
    if usua_resp[0] == "1":
        j.juego_play(usua_resp)
    elif usua_resp[0] == "2":
        j.puntajes()
    elif usua_resp[0] == "3":
        j.instrucciones()
    elif usua_resp[0] == "4":
        j.mensajes()
    else:
        encenddio = False
