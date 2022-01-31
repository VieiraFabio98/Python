import random

def deal_cards():
    '''Função que distrubui a carta'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards): 
    '''Função que calcula o valor das cartas de cada usuario'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"           



def game():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""") 
    user_cards = []
    dealer_cards = []
    is_game_over = False 
    
    for _ in range(2):
        user_cards.append(deal_cards())
        dealer_cards.append(deal_cards())
        
    while not is_game_over:    
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards) 

        print(f"your cards {user_cards}, current score {user_score}")
        print(f"dealers cards {dealer_cards[0]}")
            
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want to hint another card? Y or N: ")
            if another_card == "Y" or another_card == "y":
                user_cards.append(deal_cards())
            else:    
                is_game_over = True         
        
    while dealer_score < 17 and dealer_score != 0:
            dealer_cards.append(deal_cards())
            dealer_score = calculate_score(dealer_cards)
            
    print(f"Your final hand is {user_cards} and the final score is {user_score}")     
    print(f"Dealer final hand is {dealer_cards} and the final score is {dealer_score}")     
    print(compare(user_score, dealer_score))
    
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print("\033c", end='')  
        game()        
        
game()        
        