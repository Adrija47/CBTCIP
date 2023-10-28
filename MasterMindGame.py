from getpass import getpass
def master_mind_game():
    print("!#.#.#.#.#.#.#.#.#.#!~ WELCOME TO THE MASTERMIND GAME ~!#.#.#.#.#.#.#.#.#.#!")
    print("Two players play against eachother and guess eachothers secret numbers that they have selected. The player who guessed in fewer attempts wins!")
    print("Best Of Luck! May the best player win.")


def player1_secret_number():
    secret_number1= getpass("Player 1 enter a multidigit number so that Player 2 can guess: ") 
    return secret_number1

def player2_turn(secretnumber):
    tries= 0
    while True:
        print(f"Player 1 has entered a {len(secretnumber)} digit number.")
        guess=input("Player 2 enter your guess! ")
        tries += 1
        if (guess == secretnumber):
            print(f"Congratulations! You guessed it at the {tries} attempt and you're crowned as the Mastermind!")
            return tries
        else:
            print("Player 1 wants to provide hints!")
            for i in range(len(secretnumber)):
                if guess[i] == secretnumber[i]:
                    print("Correct Digit: ", guess[i])
                elif guess[i] > secretnumber[i]:
                    print("Digit: Too High!")
                elif guess[i]< secretnumber[i]:
                    print("Digit: Too Low")
                else:
                    print("Incorrect Digit: ")
        

        
def player2_secret_number():
    secret_number2= getpass("Player 2 enter a multidigit number so that Player 1 can guess: ") 
    return secret_number2

def player1_turn(secretnumber):
    tries= 0
    while True:
        print(f"Player 2 has entered a {len(secretnumber)} digit number.")
        guess=input("Player 1 enter your guess! ")
        tries += 1
        if (guess == secretnumber):
            print(f"Congratulations! You guessed it at the {tries} attempt and you're crowned as the Mastermind!")
            return tries
        
        else:
            print("Player 2 wants to provide hints!")
            for i in range(len(secretnumber)):
                if guess[i] == secretnumber[i]:
                    print("Correct Digit: ", guess[i])
                elif guess[i] > secretnumber[i]:
                    print("Digit: Too High!")
                elif guess[i]< secretnumber[i]:
                    print("Digit: Too Low")
                
                else:
                    print("Incorrect Digit: ")
        
                
        

def Run_Game():
    Player1_Score= 0
    Player2_Score= 0
    while True:
        master_mind_game()
        secret_num_1= player1_secret_number()
        Player2= player2_turn(secret_num_1) 
        secret_num_2= player2_secret_number()
        Player1= player1_turn(secret_num_2)

        if Player1 < Player2:
            Player1_Score += 1
            print("Player 1 wins this round!")
        elif Player2 < Player1:
            Player2_Score += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie for this round!")

        print(f"Player 1 Score: {Player1_Score}")
        print(f"Player 2 Score: {Player2_Score}")
        

        play_again = input("Do you want to play another round? [YES|NO]: ")
        if play_again.casefold() != "yes":
            break

    if Player1_Score > Player2_Score:
        print("Player 1 is crowned as the Mastermind!")
    elif Player2_Score > Player1_Score:
        print("Player 2 is crowned as the Mastermind!")
    else:
        print("It's a tie for the overall game!")
    print("Thankyou for playing. Have a nice day!")

if __name__ == "__main__":
    Run_Game()




