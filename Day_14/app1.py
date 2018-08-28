import random
import pdb

game_dict = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def header():
    print("Welcome to Rock / Paper / Scissors")
    print("----------------------------------")

def get_name():
    return input("Enter your name: ")

def number_of_plays():
    return int(input("Number of iterations: "))

def do_roll():
    return random.choice(list(game_dict.keys()))

def find_winner(player_roll, computer_roll):
    if player_roll == computer_roll:
        tally["Ties"] += 1
        return "Tie"
    if game_dict[player_roll] == computer_roll:
        tally["Player"] += 1
        return "Player Wins"
    else:
        tally["Computer"] += 1
        return "Computer Wins"      

if __name__ == "__main__":
    header()
    player = get_name()
    itterations = number_of_plays()

    counter = 0
    
    tally = {
        "Ties": 0,
        "Player": 0, 
        "Computer": 0,
    }

    while counter < itterations:
        counter += 1
        player_roll = do_roll()
        computer_roll = do_roll()
        print("-----------------------------------")
        print(f"Roll #{counter}")
        print(f"player rolls: {player_roll}")
        print(f"computer rolls: {computer_roll}")
        print(find_winner(player_roll, computer_roll))

    print(tally)


