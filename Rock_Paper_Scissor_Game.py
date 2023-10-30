import random
from getpass import getpass

def player_turn():
    player_input= getpass("Player enter your choice [ROCK|PAPER|SCISSOR]?: ").casefold()
    if (player_input != "rock" and player_input != "paper" and player_input != "scissor"):
        print("Invalid choice or Incorrect spelling! Please choose from the given options or correct your spelling.")
        return player_turn()
    else:
       return player_input 
 

def computer_turn():
    choices= ["Rock", "Paper", "Scissor"]
    comp_choice= random.choice(choices).casefold()
    return comp_choice

def winning_conditions(playerchoice, computerchoice):

    if playerchoice == computerchoice:
        return "Ohh no its a Tie!"
       
    if ((playerchoice == "rock" and computerchoice == "scissor") or (playerchoice == "scissor" and computerchoice == "paper") or (playerchoice == "paper" and computerchoice == "rock")):
        return "The Player Wins"
     
    else:
        return "The Computer Wins"
    

def run_game():
    rounds=1
    ps= 0 #player's score counter
    cs= 0 #computer's score counter
    
    while True:
        player_choice= player_turn()
        computer_choice= computer_turn()
        print(f"The Player has choosen: {player_choice}")
        print(f"The Computer has choosen: {computer_choice}")
        winner= winning_conditions(player_choice, computer_choice)
        print(winner)

        if "The Player Wins" in winner:
            ps += 1
        elif "The Computer Wins" in winner:
            cs += 1
        rounds += 1

        print(f"The Score of the Player is: {ps}")
        print(f"The Score of the Computer is: {cs}")

        play_again = input("Do you want to play another round? [YES|NO]: ")
        if play_again.casefold() != "yes":
            break


    print(f"The total number of rounds played is: {rounds}")
    if ps > cs:
        print(f"The overall winner of the ROCK-PAPER-SCISSOR Game is The Player with score: {ps}")
    elif cs > ps:
        print(f"The overall winner of the ROCK-PAPER-SCISSOR Game is The Computer with score: {cs} ")
    else:
        print("Its an overall Tie")
    print("Thankyou for playing. Have a nice day!")

if __name__ == "__main__":
    print("!#.#.#.#.#.#.#.#.#.#!~&&&&&~ WELCOME TO THE ROCK-PAPER-SCISSOR GAME ~&&&&&~!#.#.#.#.#.#.#.#.#.#!")
    print("Best Of Luck! Let's see who wins! The Computer or You.")

    run_game()




         



