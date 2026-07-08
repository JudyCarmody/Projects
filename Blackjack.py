import random
print("Blackjack")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
cpu_cards = []

def pick_cards():
    for _ in range(2):
        player_cards.append(random.choice(cards))
        cpu_cards.append(random.choice(cards))
    return player_cards, cpu_cards

def totals(card_list):
    total = 0
    for card in card_list:
        total += card
    return total

def end_game(player_total, cpu_total):
    if player_total == cpu_total:
        print("DRAW!")
    elif player_total == 21 or cpu_total == 21:
        print("BLACKJACK!")
        if player_total == 21:
            print("You Win!")
        else:
            print("You Lose!")
    elif player_total >= 22 or cpu_total >= 22:
        print("BUST!")
        if player_total >= 22:
            print("You Lose!")
        else:
            print("You Win!")
    elif player_total > cpu_total:
        print("You Win!")
    else:
        print("You Lose!")
    play_again = input("Play again (y/n)? ").lower()
    if play_again == 'y':
        print("\n" * 5)
        reset(player_cards)
        reset(cpu_cards)
        pick_cards()
        playing_game()
    else:
        exit()

def reset(card_list):
    for _ in range(len(card_list)):
        card_list.pop()
    return card_list

def playing_game():
    print(f"Player cards: {player_cards}")
    print(f"CPU first card: {cpu_cards[0]}")
    continue_playing = input("Get another card (y/n)? ").lower()
    if continue_playing == 'y':
        for _ in range(1):
            player_cards.append(random.choice(cards))
        print(player_cards)
        playing_game()
    elif continue_playing == 'n':
        player_total = totals(player_cards)
        cpu_total = totals(cpu_cards)
        print(f"Player total: {player_total}")
        print(f"CPU total: {cpu_total}")
        end_game(player_total, cpu_total)
        playing = False

play_game = input("Start game (y/n)? ").lower()
if play_game == 'y':
    pick_cards()
    playing_game()
else:
    exit()