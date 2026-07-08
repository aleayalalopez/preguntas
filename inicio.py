import texto_preguntas as tx
import sistema as ss
import juego as j

# Inicio del juego
print(tx.tx0)
input("\n       ***** Presiona cualquier tecla para comenzar ****")
usua_resp = ss.menu()
if usua_resp[0] == "1":
    j.juego_play(usua_resp)
