import time
import sys

def mensaje_inicial(): 

    # Aparece el banner inicial
    mensaje1 = u"""\u001b[1m
----------------------------------------------------------
 ____                      _   ____                      
/ ___| _ __   ___  ___  __| | |  _ \ ___  __ _  _____  __
\___ \| '_ \ / _ \/ _ \/ _` | | |_) / _ \/ _` |/ _ \ \/ /
 ___) | |_) |  __/  __/ (_| | |  _ <  __/ (_| |  __/>  < 
|____/| .__/ \___|\___|\__,_| |_| \_\___|\__, |\___/_/\_\ 
      |_|                                |___/           

----------------------------------------------------------
\u001b[0m"""
    for char in mensaje1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)

    time.sleep(1)

    ##Aparece el saludo
    mensaje2 = "¡Bienvenido a Speed Regex! En este juego podrás practicar tu "\
    "velocidad al hacer búsquedas con regex."

    for char in mensaje2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

    time.sleep(1)

    # Continúan las instrucciones
    mensaje3 = u"\n\nTienes \u001b[1mdos minutos\u001b[0m para responder la mayor cantidad de "\
    "desafíos que puedas. Entre más preguntas contestes, ¡mayor será la "\
    "envidia de los demás programadores!"

    for char in mensaje3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)

    time.sleep(1)

    # Mensaje para input del usuario
    respuesta = """\n
Para iniciar el juego, escribe "dame regex".
Para salir, escribe "exit".\n
>>> """ 

    while True: 
        iniciar = input(respuesta)

        if iniciar == 'exit':
            return 'salir'

        elif iniciar == 'dame regex':
            return True

        else: 
            mensaje_error = '\nNo te entendí. ¿Qué quisiste decir?'
            
            for char in mensaje_error:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.02)
            time.sleep(0.5)