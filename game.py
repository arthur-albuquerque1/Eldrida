import random
import time
import keyboard 


exit = False
while not exit:

    phrase = None
    choice_game = None
    continue_game = None

    def typing_effect():
        for letter in phrase:
            print(letter, end='', flush=True)
            time.sleep(0.05)   
            



    def game_intro():
            global phrase
            global choice_game
            phrase = '''Na terra de Eldrida, há muito tempo atrás, vivia um reino próspero e pacífico governado pelo justo Rei Harold. No entanto, um mal ancestral, conhecido como o Dragão Negro, foi despertado e começou a destruir tudo em seu caminho. \n A fumaça de suas chamas cobria o céu, e as cidades foram destruídas, deixando muitos mortos e feridos. \nO rei Harold chamou todos os guerreiros valentes, magos poderosos e ladrões astutos para lutar contra o Dragão Negro \n e restaurar a paz no reino. Ele ofereceu uma recompensa para aqueles que conseguirem matar o Dragão Negro e trazer de volta a tranquilidade para o seu povo. \nVocê é um desses aventureiros, pronto para enfrentar desafios e perigos para salvar o reino de Eldrida e ganhar a recompensa do rei. Sua jornada começa agora, e a sorte estará ao seu lado. \n\n\n\n\n'''
            typing_effect()

            frase = ''' .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
                        | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
                        | |  _________   | || |   _____      | || |  ________    | || |  _______     | || |     _____    | || |  ________    | || |      __      | |
                        | | |_   ___  |  | || |  |_   _|     | || | |_   ___ `.  | || | |_   __ \    | || |    |_   _|   | || | |_   ___ `.  | || |     /  \     | |
                        | |   | |_  \_|  | || |    | |       | || |   | |   `. \ | || |   | |__) |   | || |      | |     | || |   | |   `. \ | || |    / /\ \    | |
                        | |   |  _|  _   | || |    | |   _   | || |   | |    | | | || |   |  __ /    | || |      | |     | || |   | |    | | | || |   / ____ \   | |
                        | |  _| |___/ |  | || |   _| |__/ |  | || |  _| |___.' / | || |  _| |  \ \_  | || |     _| |_    | || |  _| |___.' / | || | _/ /    \ \_ | |
                        | | |_________|  | || |  |________|  | || | |________.'  | || | |____| |___| | || |    |_____|   | || | |________.'  | || ||____|  |____|| |
                        | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
                        | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
                        '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' '''
            print(frase)

            phrase = '''\n\n\n\nVocê está andando por um caminho em uma floresta, até que se depara com uma pequena cabana que aparenta estar abandonada, o que você faz? \n\n\n'''
            typing_effect()

            print('1. Me aproximo da cabana')
            print('2. Continuo meu caminho')
            choice_game = int(input('')) 
            if choice_game == 1:
                 phrase = '''A cabana realmente está abandonada e a porta não está trancada, o que você faz? \n\n\n'''
                 typing_effect()
                 print('1. Abro a porta e entro na cabana')
                 print('2. Vou embora')
                 choice_game = int(input(''))
                 if choice_game == 1:
                      phrase = 'Você entra na cabana'
                      typing_effect()
                 if choice_game == 2:
                      phrase = 'Você continua sua jornada'
                      typing_effect

            elif choice_game == 2:
                 print('Você continua sua jornada')
                            

    print('The Untold History: Eldrida')
    print('1. Iniciar')
    print('2. Sair')
    choice_menu = int(input('Selecione: '))
    if choice_menu == 1:
        game_intro()
    elif choice_menu == 2:
        exit = True





