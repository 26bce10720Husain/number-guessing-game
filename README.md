## Number Guessing Game

A simple terminal-based number guessing game built in Python. It’s a small project I made to practice loops, conditionals, and handling user input. The game has three difficulty levels, tracks your score, and shows your session stats while you play.

_________________________________________________________________________________________________________

# How to Run

You only need Python 3. No extra packages are required—the game uses random and time, which comes built-in Python.

>'python main.py'

__________________________________________________________________________________________

# How to Play

1. When the game starts, enter your name. If you just press Enter, you’ll be called “Player”.
2. From the main menu, choose Start new game.
3. Pick a difficulty level (Easy, Medium, or Hard).
4. Start guessing the secret number.

- After each guess, the game tells you:
-> If your guess is too high or too low
-> If you’re within 10 of the secret number (“Very close!”)

___________________________________________________________________

# Difficulty Levels

Level	 Number Range	  Max Attempts	  Points per Attempt Left

Easy	  1 – 100	            10	                 10
Medium  1 – 500	            12	                 20
Hard	  1 – 1000	          15	                 30

__________________________________________________________________

# Special Inputs While Playing

- Type 0 to get a hint (it tells you if the number is odd or even).
(This doesn’t use an attempt, but it costs 10 points.)

- Type -1 to quit the current round. The game ends and shows you the secret number.

______________________________________________________________________

# Scoring

- Your score is calculated like this:
**Score = (Attempts left * Points per attempt) − (Hints used * 10)**

- The faster you guess, the higher your score.
- Your score can’t go below 0.
- Your best score becomes the high score for that session.

_________________________________________________________________________________

# Main Menu Options

>Start new game – Choose a level and begin playing.
>View rules – See a quick list of how the game works.
>View high score – Check the best score and who got it.
>View game history – See all games played in this session.
>View game statistics – See total games played, wins, losses, and win percentage. 
>Exit – Shows a final summary and closes the game.

________________________________________________________________________________________________

# Important Notes

- Everything is stored in memory. When you close the program, your high score and history reset.
- The game handles invalid inputs (like typing letters instead of numbers), so it won’t crash.
- If you quit a game early using -1, it counts as a game played, but not as a win or a loss.

____________________________________________________________________________

# Concepts Used

- This project uses basic Python concepts:

>while and for loops

>if/elif/else conditionals

>Functions from the random module

>Lists to store history and stats

>try/except for handling bad input

>Simple string formatting for output

___________________________________________________________________________________________________________________________________________________________________________

