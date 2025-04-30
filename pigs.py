import random

def pigs_players():

    while True:
        players = input("How many players? (2-4): ")
        choices = [2,3,4]

        if players.isdigit() == False or int(players) not in choices:
            print("Please put a number between 2-4.")
            continue
        
        players = int(players)
        print("\nLet's go players!")
        return (players)

def pigs_rolldie():
    num_players = pigs_players()  #Store the number of players
    total_score = [0] * num_players #List to keep track of all players' scores
    max_score = 20

    for player_index in range(1, num_players+1): #Loop through each player
                                                 #Stop before num_players + 1, because the range() function excludes the stop number.

        print(f"Player {player_index}, you're up!")
        score = 0  # Reset the score for the current player

        while True:
            choice_roll = input(f"\nPlayer {player_index}, roll the die? (y/n): ").lower()

            if choice_roll != "y" and choice_roll != "n":
                print("Please choose y/n.")
            
            elif choice_roll == "n":
                print("Ok, bye!")
                print(f"Your score is {score}")
                break
            
            else:
                print("\nLet's go!")
                roll_die = random.randint(1, 6)
                print(f"You rolled a {roll_die}")

                if roll_die == 1:
                    print("Sorry, your turn has ended.")
                    score = 0
                    total_score[player_index-1] = 0
                    print(f"Your score is {score}\n")
                    break

                else:
                    score += roll_die
                    total_score[player_index-1] = score
                    print(f"Your score is {score}")

                    if total_score[player_index-1] == max_score:
                        print("YAY! You got the maximum score!!")
                        continue

                    elif total_score[player_index-1] >= 20:
                        score = 0
                        total_score[player_index-1] = 0
                        print(f"You exceed 20 points! Your new score is {score} :( \n")
                        break

    print("\nThank you for playing.")
    print("Scoreboard:")
    for player_index in range(1, num_players+1):
        print(f"Player {player_index}: {total_score[player_index-1]}")



            

pigs_rolldie()