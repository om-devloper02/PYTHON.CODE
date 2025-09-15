# Function to print the tic tac toe board
import random
from flask import Flask

def mytictactoe(val):
    print("\n")
    print("\t {} | {} | {}".format(val[0], val[1], val[2]))
    print("\t-----------")
    print("\t {} | {} | {}".format(val[3], val[4], val[5]))
    print("\t-----------")
    print("\t {} | {} | {}".format(val[6], val[7], val[8]))
    print("\n")


# Function to check victory
def check_victory(playerpos, curplayer):
    solution = [[1,2,3],[4,5,6],[7,8,9],
                [1,4,7],[2,5,8],[3,6,9],
                [1,5,9],[3,5,7]]
    for i in solution:
        if all(j in playerpos[curplayer] for j in i):
            return True
    return False


# Function to check tie
def check_tie(playerpos):
    if len(playerpos['X']) + len(playerpos['O']) == 9:
        return True
    return False


# Function to display scoreboard
def myscorboard(scoreboard):
    print("\t----------------------------")
    print("\t       SCORE BOARD         ")
    print("\t----------------------------")
    listtoplayers = list(scoreboard.keys())
    print("\t", listtoplayers[0], "\t", scoreboard[listtoplayers[0]])
    print("\t", listtoplayers[1], "\t", scoreboard[listtoplayers[1]])
    print("\t----------------------------\n")


# Bot personality comments
bot_comments_move = [
    "Hmm... interesting choice.",
    "Your end is near!",
    "Let's see you block this.",
    "I have a plan...",
    "You can't win this time!"
]

bot_comments_win = [
    "I told you, I never lose!",
    "Victory is mine!",
    "Better luck next time," 
]

bot_comments_lose = [
    "Nooo... you got lucky!",
    "I will remember this defeat.",
    "You won? Impossible!"
]

def bot_talk(event):
    if event == "move":
        print("Bot:", random.choice(bot_comments_move))
    elif event == "win":
        print("Bot:", random.choice(bot_comments_win))
    elif event == "lose":
        print("Bot:", random.choice(bot_comments_lose))


# Bot move selection
def bot_move(val):
    available = [i for i, v in enumerate(val) if v == ' ']
    return random.choice(available) + 1


# Function for a single game
def singlegame(curplayer, bot_symbol=None):
    val = [' ' for _ in range(9)]
    playerpos = {'X': [], 'O': []}

    while True:
        mytictactoe(val)

        # Bot or player move
        if curplayer == bot_symbol:
            chance = bot_move(val)
            print(f"Bot chooses: {chance}")
            bot_talk("move")  # Bot talks when making a move
        else:
            try:
                print("Player", curplayer, "turn, Choose your Block (1-9):", end=" ")
                chance = int(input())
            except ValueError:
                print("Invalid input!!! Try Again")
                continue

        # Check input validity
        if chance < 1 or chance > 9:
            print("Invalid input!!! Try Again")
            continue

        # Check if block is already taken
        if val[chance - 1] != ' ':
            print("Oops! The Place is already occupied, Try again!!")
            continue

        # Update board and player positions
        val[chance - 1] = curplayer
        playerpos[curplayer].append(chance)

        # Check victory
        if check_victory(playerpos, curplayer):
            mytictactoe(val)
            print("Congratulations! Player", curplayer, "has won the game!")
            # Bot reaction
            if bot_symbol is not None:
                if curplayer == bot_symbol:
                    bot_talk("win")
                else:
                    bot_talk("lose")
            print("\n")
            return curplayer

        # Check tie
        if check_tie(playerpos):
            mytictactoe(val)
            print("Oh! Game tied.")
            print("\n")
            return 'D'

        # Switch turn
        curplayer = 'O' if curplayer == 'X' else 'X'


# Main game
if __name__ == "__main__":
    print("First Player")
    FirstPlayer = input("Specify the name: ")
    print("\n")

    print("Second Player (type 'bot' for computer):")
    SecondPlayer = input("Specify the name: ")
    print("\n")

    # Avoid same names
    if SecondPlayer == FirstPlayer:
        print("Second Player name must be different. Restart the game!")
        exit(1)

    # Bot symbol setup
    bot_symbol = None

    # Storing the player who chooses X and O
    curplayer = FirstPlayer
    playerchoice = {'X': "", 'O': ""}

    # Scoreboard
    scoreboard = {FirstPlayer: 0, SecondPlayer: 0}
    myscorboard(scoreboard)

    # Loop for multiple games
    while True:
        print(curplayer, "will make the choice:")
        print("Press 1 for X")
        print("Press 2 for O")
        print("Press 3 to Quit")

        try:
            the_choice = int(input())
        except ValueError:
            print("Invalid input!!! Try Again\n")
            continue

        # Assign choices
        if the_choice == 1:
            playerchoice['X'] = curplayer
            playerchoice['O'] = SecondPlayer if curplayer == FirstPlayer else FirstPlayer

        elif the_choice == 2:
            playerchoice['O'] = curplayer
            playerchoice['X'] = SecondPlayer if curplayer == FirstPlayer else FirstPlayer

        elif the_choice == 3:
            print("The Final Scores:")
            myscorboard(scoreboard)
            break

        else:
            print("Invalid selection!!! Try Again\n")
            continue

        # Bot detection
        if playerchoice['X'].lower() == "bot":
            bot_symbol = 'X'
        elif playerchoice['O'].lower() == "bot":
            bot_symbol = 'O'
        else:
            bot_symbol = None

        # Play one game
        symbol = 'X' if the_choice == 1 else 'O'
        win = singlegame(symbol, bot_symbol)

        # Update scoreboard
        if win != 'D':
            playerWon = playerchoice[win]
            scoreboard[playerWon] += 1

        myscorboard(scoreboard)

        # Switch who chooses X or O
        curplayer = SecondPlayer if curplayer == FirstPlayer else FirstPlayer