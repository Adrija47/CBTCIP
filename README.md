# CBTCIP
# Master_Mind_Game
This code is a Python program that simulates a two-player game called "Mastermind." In this game, two players take turns guessing each other's secret multi-digit numbers. The player who guesses the opponent's number in the fewest attempts wins. The code structure can be broken down as follows:

1. The code starts with a welcome message and an explanation of the game rules in the `master_mind_game()` function.

2. `player1_secret_number()` is a function that allows the first player to input their secret number without it being visible on the screen. This number is stored in the variable `secret_number1`.

3. `player2_turn(secretnumber)` is a function where the second player takes their turn to guess the first player's secret number. It keeps track of the number of attempts and provides hints to the second player based on their guesses.

4. `player2_secret_number()` is a function that allows the second player to input their secret number without it being visible on the screen. This number is stored in the variable `secret_number2`.

5. `player1_turn(secretnumber)` is similar to `player2_turn()` but for the first player's turn, where they guess the second player's secret number.

6. The `Run_Game()` function manages the game loop, where players take turns and the scores are updated. It also checks for the end of the game and asks if the players want to play another round.

7. At the end of the game loop, it determines the winner (Player 1, Player 2, or a tie) based on the scores and displays a closing message.

8. Finally, the program is executed in the `if __name__ == "__main__":` block by calling the `Run_Game()` function.

The game continues in rounds until the players decide not to play again. It keeps track of each player's score and declares a winner at the end based on the number of rounds won. It's a simple and interactive two-player game that tests each player's guessing and deduction skills.
