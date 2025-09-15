Here’s the ready-to-use README.md:

# 🎮 Tic Tac Toe with Bot Personality

This is a Python implementation of the **Tic Tac Toe** game where two players (or a player vs Bot) can play.  
The Bot has a fun personality with random comments during moves, wins, and losses.  
A scoreboard is also maintained across multiple games.  

---

## 📌 Features
- Play **Player vs Player** or **Player vs Bot**.
- Interactive text-based game board.
- Bot personality:
  - Random comments while making a move.
  - Victory and defeat reactions.
- Victory and tie detection.
- Scoreboard system maintained across rounds.
- Option to quit anytime.

---

## ⚙️ Requirements
Make sure you have Python installed.  
No extra libraries are needed except **Flask** (though currently unused in the script).

Install Flask if not already installed:
```bash
pip install flask

▶️ How to Run

Save the script as tictactoe.py.

Open terminal in the project folder.

Run:

python tictactoe.py

🎯 How to Play

Enter First Player name.

Enter Second Player name (or type bot to play against the computer).

Players take turns choosing X or O.

On each turn:

Player enters a block number (1–9).

Bot randomly selects an available block and talks.

The game checks for:

Victory → Player wins if 3 marks align.

Tie → If the board is full and no one wins.

After each game:

Scoreboard is displayed.

The game continues until you choose Quit.

🗂️ Board Layout (Positions)
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

📖 Sample Game Flow
First Player
Specify the name: Omkar

Second Player (type 'bot' for computer):
Specify the name: bot

----------------------------
       SCORE BOARD
----------------------------
 Omkar   0
 bot     0
----------------------------

Omkar will make the choice:
Press 1 for X
Press 2 for O
Press 3 to Quit

Bot in action
Bot chooses: 5
Bot: Hmm... interesting choice.

📊 Scoreboard Example
----------------------------
       SCORE BOARD
----------------------------
 Omkar    1
 bot      2
----------------------------