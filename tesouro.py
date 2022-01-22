print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

escolha1 = input("Você chega em um rio e percebe um barco vazio vindo em sua direção. Você atravessa NADANDO ou espera o BARCO ?")
if escolha1 == "BARCO":
    escolha2 = input("Você chegou em uma porção de terra, a sua ESQUERDA existe um caminho tenebroso, na sua DIREITA uma ponte parcialmente quebrada. Qual caminho você toma?")
    if escolha2 =="DIREITA":
        escolha3 = input("Atravessando a ponte, você encontra um altar com um baú, você ABRE ele ou VERIFICA o entorno primeiro?")
        if escolha3 == "ABRE":
            print("Uma armadilha e acionada. GAME OVER")
        else:
            print("Você encontrou um tesouro. Fim de Jogo")    
    else:
        print("Durant o caminho tenebroso, uma cobra venenosa picou voc~ê. GAME OVER")    

else:
    print("Você caiu em um buraco. GAME OVER.")