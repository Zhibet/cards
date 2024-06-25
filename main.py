import random


def draw_card():
    random_card = random.randint(0, 21)
    print(f'You drew a {random_card}')
    return random_card


def player_turn(player_name):
    user_total = 0
    while True:
        print(f"{player_name}'s score is {user_total}")
        question_one = input(f"{player_name}, do you want to draw? Type 'yes' or 'no': ").strip().lower()
        if question_one == 'yes':
            card = draw_card()
            user_total += card
            if user_total > 21:
                print(f"{player_name}, you lose!")
                return user_total, True
            elif user_total == 21:
                print(f"{player_name}, you win!")
        else:
            return user_total, False


def main():
    num_players = int(input("Enter the number of players: "))
    players = [input(f"Enter the name of player {i + 1}: ") for i in range(num_players)]

    scores = {player: 0 for player in players}
    game_on = True
    current_player_index = 0

    while game_on:
        current_player = players[current_player_index]
        print(f"\n{current_player}'s turn:")
        score, lost = player_turn(current_player)
        scores[current_player] = score

        if lost:
            game_on = False
        else:
            current_player_index = (current_player_index + 1) % num_players
            if current_player_index == 0:
                continue_game = input(
                    "Do all players want to continue to the next round? Type 'yes' or 'no': ").strip().lower()
                if continue_game == 'no':
                    game_on = False

    print("\nFinal scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

if __name__ == "__main__":
    main()
