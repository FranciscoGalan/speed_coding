from mensaje_inicial import mensaje_inicial
from cuenta_regresiva import *
from temporizador import *
from arrojar_pregunta import *

puntos=0

if __name__ == "__main__":
    if mensaje_inicial() == True: #Si el usuario quiere jugar.  
        
        # Mantener el juego activo.
        juego_activo = True
        while juego_activo:
            
            # Mensaje: cuenta regresiva para iniciar.
            cuenta_regresiva()
                    
            # Iniciar temporizador.
            thread_temporizador = threading.Thread(target = temporizador, args=(20, ))
            thread_temporizador.start()

            # Iniciar contadores de preguntas restantes y puntaje
            preguntas_restantes = [1, 2, 3, 4, 5]

            # Mostrar preguntas mientras siga activo el temporizador.
            while thread_temporizador.is_alive():
                puntos+=arrojar_pregunta(thread_temporizador, preguntas_restantes)

            # Mostrar puntaje 
            print(f'TU SCORE:{puntos}')

            # Preguntar si quiere volver a jugar
            respuesta_activa = True

            while respuesta_activa:
                respuesta = input("\n¿Quieres jugar de nuevo?\n>>>")

                if respuesta == ('si' or 'sí' or 'Si' or 'Sí' or 'SI' or 'sI'):
                    respuesta_activa = False
                    puntos=0

                elif respuesta == ('no' or 'No' or 'NO' or 'nO'):
                    juego_activo = False
                    respuesta_activa = False

                else: 
                    mensaje_error = '\nNo te entendí. ¿Qué quisiste decir?\n'
                
                    for char in mensaje_error:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.02)
                    time.sleep(0.5)

    else: 
        pass

    # Mensaje cuando la persona ya se va a salir
    print("\n¡Regresa pronto!\n")
    time.sleep(0.1)
