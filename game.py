import random
import time
import keyboard 


exit = False
while not exit:

    # Principais variáveis globais
    phrase = ''
    choice_game = None

    # Itens do jogo
    swords = []
    sword_lvl_1 = ['Espada Enferrujada', 1]
    sword_lvl_2 = ['Espada Boa', 3]
    sword_lvl_3 = ['Espada Lendária', 7]
    swords.extend([sword_lvl_1, sword_lvl_2, sword_lvl_3])

    armor = []
    armor_lvl_1 = ['Armadura de couro', 1]
    armor_lvl_2 = ['Armadura de Ferro', 3]
    armor_lvl_3 = ['Armadura Lendária', 7]
    armor.extend([armor_lvl_1, armor_lvl_2, armor_lvl_3])

    # Inventário
    inventory = []
    
    # Monstros
    def monster_1():
         monster_1_life = 2
         print('Você encontrou um lobo')

    # Sistema de vida
    damage = 0
    life_initial = 2
    life = life_initial + inventory[4] - damage 

         

         
    
    # Sistema de combate
    def combat():
         combat = 2

    # Efeito visual de digitação
    def typing_effect():
          for letter in phrase:
               print(letter, end='', flush=True)
               time.sleep(0.05)  
    
    # Sistema de escolhas
    def choice_input():
         global choice_game
         choice_game = int(input(''))
    
    
    def next_intro():
         phrase = 'Você continua sua jornada'
         typing_effect()
         game_chapter2()
    
    # Segunda parte do jogo
    def game_chapter2():
         something = 1

    # Introdução do jogo        
    def game_intro():
            global phrase
            global choice_game
            global items
            global inventory
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
            print('2. Continuo meu caminho\n')
            choice_input()
            if choice_game == 1:
                 phrase = '''A cabana realmente está abandonada e a porta não está trancada, o que você faz? \n\n\n'''
                 typing_effect()
                 print('1. Abro a porta e entro na cabana')
                 print('2. Vou embora\n')
                 choice_input()
                 if choice_game == 1:
                      phrase = 'Você entra na cabana \n'
                      typing_effect()
                      print('1. Vasculhar')
                      print('2. Sair\n')
                      choice_input()
                      if choice_game == 1:
                           time.sleep(0.1)
                           print('Você encontrou uma espada enferrujada\n')
                           print('1. Pegar')
                           print('2. Sair da cabana')
                           choice_input()
                           if choice_game == 1:
                                inventory.append(swords[0])
                                next()
                                
                           elif choice_game == 2:
                                next()

                                
                      elif choice_game == 2:
                           next()

                 elif choice_game == 2:
                      next()

            elif choice_game == 2:
                 next()
                            

    # Menu do jogo
    print('The Untold History: Eldrida')
    print('1. Iniciar')
    print('2. Sair')
    choice_menu = int(input('Selecione: '))
    if choice_menu == 1:
        game_intro()
    elif choice_menu == 2:
        exit = True





