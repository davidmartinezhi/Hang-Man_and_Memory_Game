import random
import time

def ahorcado():
    '''Juego de ahorcado donde tienes que adivinar, letra por letra
    una palabra, antes de que se complete la imagen de alguien ahorcado'''

    '''Definimos variables y listas que usaremos en el juego'''
    #Lista de etapas del juego, para actualizarel juego mas sencillo.
    ahorcado = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        o   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        o   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        o   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        o   |
       /|\\  |
            |
            |
        =========''', '''
        +---+
        |   |
        o   |
       /|\\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        o   |
       /|\\  |
       / \\  |
            |
        =========''']


    #Lista con las palabras que podemos a usar en el juego.
    palabras = [ "GUADALUPE", "ASTRONAUTA", "ESPEJISMO", "EXHAUSTIVAMENTE",
                "COMUNICACION", "REFLEJO", "ALABANZA", "PAISAJE" ]
    
    palabra = random.choice(palabras)   #Agarramos una palabra alazar de la lista de palabras.

    car_validos = 'QWERTYUIOPÑLKJHGFDSAZXCVBNM' #Simbolos validos para ingresar en el juego.
    errores = 0     #Contador que actualiza los errores y la etapa del juego.
    atinados = []   #Recibe letras que el jugador atina.
    intentos_fallidos = []   #Guarda las letras intentadas que no son parte de la palabra.
    por_atinar = []

    '''Juego en marcha'''
    while True: #Iniciador del juego

        '''Display del juego'''
        print(palabra + ahorcado[errores])  #Muestra la etapa del juego y la palabra elegida (para probar programa).

        #En la palabra imprimimos las letras descubiertas y escondemos las que siguen sin ser descubiertas
        for l in palabra:  
            if l in atinados:
                por_atinar.append(l)
                print(' ' + l + ' ', end='')       
            else:
                print(' _ ', end='')
        print('\n')
        #Checa el numero de coincidencias entre las letras descubiertas y la palabra
        coincidencia = 0    #Cuenta el numero de letras que coinciden entre las atinadas y las totales de la palabra.
        for l in palabra:
            if l in por_atinar:
                coincidencia += 1
   
        if coincidencia == len(palabra):    #Checa si jugador gana
            print('LO LOGRASTE\n')
            break

        elif len(ahorcado)-1 == errores:    #Checa si jugador pierde
            print('Haz perdido.\n')
            print('La palabra era: ' + palabra + '\n')
            break

        #Muestra las letras ya probadas, que no coinciden con la palabra cuando hay error
        if errores > 0:
            print('Letras intentadas que no coinciden:', set(intentos_fallidos))


        letra = input('\nLetra: ') #Le pide al usuario que ingrese una letra
        letra = letra.strip().upper() #Limpia la letra de espacios y la hace mayuscula
        
        print('------------------\n') #Divide un intento del otro


        '''Flow Control'''
        #Checa si se ingreso una letra valida 
        #Si es valida, lo toma y prosigue con el juego
        #De no ser valida imprime un mensaje de aviso y te regresa a la selección de letra (se agregan errores)
        if (letra not in car_validos) or (letra == '') or (len(letra) > 1): 
            print('*****PORFAVOR INGRESA UNA LETRA Y SOLO UNA*****\n') 
            errores += 1
            continue
        
        
        #Checa si la letra esta en la palabra y lo agrega a la lista atinados y avisa
        if (letra in palabra) and (letra not in atinados) and (letra != ''):
            atinados.append(letra)
            print('*La letra [' + letra + '] SI esta en la palabra. SIUUUUU*\n')
        
        #Si ya habias descubierto esa letra te manda un mensaje de aviso (no se agregan errores)
        elif letra in atinados:
            print('*Esa letra ya esta descubierta*\n')

        #Si no esta en la palabra lo agrega a la lista intentos_fallidos y avisa (se agrega error)
        elif (letra not in palabra):
            print('*La letra [' + letra + '], No esta en la palabra.*\n')
            errores += 1
            intentos_fallidos.append(letra)

def memoria():
    '''Juego de memorización, aparece secuencia aleatroa de puntos y guiones'''
    '''Empieza con 5 simbolos la secuencia y se le agrega 1 cada ronda'''
    '''Empieza con 2 segundos para ver secuancia y se le suma 1 cada 2 rondas'''

    '''Variables por usar en el juego'''
    opciones = '.-' #Caracteres que van a ser desplegados de forma aleatoria
    num_caract = 5  #Numero de caracteres en la secuencia inicial
    segundos = 2    #Tiempo inicial para memorizar la secuencia
    rondas = 0    #Contador de rondas 
    memoriza = ''   #String vacio al que se le agregara la secuencia
    
    '''Iniciador de Juego'''
    while True:  
        '''Display del juego'''
        #Crea la secuencia aleatoria según el numero de caracteres
        while len(memoriza) < num_caract:   
            memoriza += random.choice(opciones)
        
        print('\nMemoriza: ' + memoriza) #Imprime secuencia que sera memorizada
        time.sleep(segundos) #Detiene el programa unos segundos

        #Desaparece la secuencia por memorizar al saltar renglon 50 veces 
        #(Comentado para checar el funcionamiento del programa)
        #print('\n' * 50) 

        print('¿Cual fue la secuencia?') 
        recuerda = input('Secuancia: ') #Pregunta por la secuencia

        '''Flow control'''
        if recuerda == memoriza:    #Checa si el jugador acerto
            rondas += 1 #Cuenta las rondas
            num_caract += 1  #Agrega un simbolo a la secuencia
            memoriza = ''  #Reinicia la secuencia, para que no se convine con otras
            if (rondas % 2 == 0) and (rondas != 0):  #Agrega 1 segundo cada 2 rodas
                segundos += 1  
            print('Lo hiciste')
            continue
    
        else:   #Checa si jugador pierde
            print('\nTe quivocaste, Rondas: ' + str(rondas))
            break

def main():

    while True:
        menu = '''
                Menú de juegos

        *Ingresa el numero 1 para jugar Ahorcado
        *Ingresa el numero 2 para probar tu Memoria
        *Ingresa el numero 0 para salir del juego
        
        1) Ahorcado 
            -Letra por letra, adivina la palabra (Con 6 errores pierdes)
            
        2) Memoria
            -Memoriza la secuencia que te aparecera (Cada ronda te aparece 1 simbolo mas)
            -La secuencia es aleatoria de 5 simbolos conformada por puntos(.) y guiones(-)
            -Cada 2 rondas se te agrega 1 segundo para memorizar
        '''
        print(menu)
        juego = input('Jugar: ')
        print('\n--------------------')

        if juego == '1':
            ahorcado()
        elif juego == '2':
            memoria()
        elif juego == '0':
            break
        else:
            print('ELIGE UNA OPCIÓN VALIDA')

        print('--------------------')
        menu = input('Presiona enter para continuar')

main()


    





