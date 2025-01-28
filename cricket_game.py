import random

def toss():
    player_choice = input("Choose Heads or Tails: ").strip().lower()
    toss_result = random.choice(["heads", "tails"])
    print(f"Toss result: {toss_result.capitalize()}")
    if player_choice == toss_result:
        print("You won the toss!")
        return input("Choose to Bat or Ball: ").strip().lower()
    else:
        computer_choice = random.choice(["bat", "ball"])
        print(f"Computer won the toss and chose to {computer_choice}.")
        return computer_choice

def play_innings(is_player_batting):
    score = 0
    wickets = 2
    balls = 12

    while wickets > 0 and balls > 0:
        player_input = int(input("Enter a number (1-6): ")) if is_player_batting else random.randint(1, 6)
        computer_input = random.randint(1, 6) if is_player_batting else int(input("Enter a number (1-6): "))
        
        print(f"Player chose: {player_input}, Computer chose: {computer_input}")

        if player_input == computer_input:
            wickets -= 1
            print(f"{'Player' if is_player_batting else 'Computer'} is OUT! Wickets left: {wickets}")
        else:
            score += player_input if is_player_batting else computer_input
            print(f"{'Player' if is_player_batting else 'Computer'} scored {player_input if is_player_batting else computer_input}. Total score: {score}")
        
        balls -= 1
        print(f"Balls remaining: {balls}\n")

    return score

def main():
    print("Welcome to the Cricket Game!")
    first_innings_choice = toss()

    print("\nFirst Innings:")
    if first_innings_choice == "bat":
        player_score = play_innings(True)
        print(f"Player's innings ended with a score of {player_score}.")
        print("\nSecond Innings:")
        computer_score = play_innings(False)
    else:
        computer_score = play_innings(False)
        print(f"Computer's innings ended with a score of {computer_score}.")
        print("\nSecond Innings:")
        player_score = play_innings(True)

    print("\nMatch Result:")
    print(f"Player's Total Score: {player_score}")
    print(f"Computer's Total Score: {computer_score}")

    if player_score > computer_score:
        print("Congratulations! You win!")
    elif player_score < computer_score:
        print("Computer wins! Better luck next time.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()