import texto_preguntas as tx
import sistema as ss
import juego as j

# Inicio del juego

ss.arranque()
print(tx.tx0)
input("\n***** ([]) ****")
usua_resp = ss.menu()
if usua_resp[0] == "1":
    j.juego_play(usua_resp)
