import random
def roll():
    min_value= 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    Players = input("Enter the number of players (2-4):")
    if Players.isdigit():
        Players= int(Players)
        if 2 <= Players <= 4:
            break
        else:
            print("Must be betwee 2-4 players.")
    else:
        print("Invalid, try again.")
        
max_score =50
Players_scores = [0 for _ in range(Players)]
while max(Players_scores) < max_score:
    for player_idx in range(Players):
        print("\nPlayer number", player_idx +1, "turn has just started!")
        print("Yours total score is: ", Players_scores[player_idx], "\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll(y)?")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            
            print("Your score is: ", current_score)
            
        Players_scores[player_idx] += current_score
        print("Your total score is:", Players_scores[player_idx])
max_score = max(Players_scores)
winning_idx = Players_scores.index(max_score)
print("Player number", winning_idx +1, "is the winner with a score of: ", max_score)
            
                
    