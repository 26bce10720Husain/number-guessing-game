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
Screenshots :

<img width="1656" height="978" alt="Screenshot 2026-09-29 at 12 42 08 AM" src="https://github.com/user-attachments/assets/b5f4e4a2-8cfd-4a83-bcb0-9d9e68560a38" />

<img width="1647" height="976" alt="Screenshot 2026-09-29 at 12 46 01 AM" src="https://github.com/user-attachments/assets/e1cd0d21-a359-473a-9722-a2d18a6d2d75" />

<img width="1643" height="965" alt="Screenshot 2026-09-29 at 12 46 53 AM" src="https://github.com/user-attachments/assets/bcce52c6-baf6-4b7f-a5eb-761eadc37bb2" />

<img width="1649" height="973" alt="Screenshot 2026-09-29 at 12 47 31 AM" src="https://github.com/user-attachments/assets/99d1114a-29fd-4664-9b1c-34408e18e773" />

<img width="1649" height="973" alt="Screenshot 2026-09-29 at 12 47 50 AM" src="https://github.com/user-attachments/assets/0852de49-0134-4392-a306-eaa8d80cf075" />

<img width="1650" height="963" alt="Screenshot 2026-09-29 at 12 48 21 AM" src="https://github.com/user-attachments/assets/7824d4e3-3182-4da4-b3b4-8cb9e7b957a0" />

<img width="1645" height="976" alt="Screenshot 2026-09-29 at 12 48 43 AM" src="https://github.com/user-attachments/assets/02556bfe-5cc7-48fd-9ce6-e8cdeb6bc619" />

<img width="1645" height="961" alt="Screenshot 2026-09-29 at 12 48 59 AM" src="https://github.com/user-attachments/assets/798de1bb-d885-4c74-8dfe-fa394d826e91" />

<img width="1654" height="978" alt="Screenshot 2026-09-29 at 12 49 19 AM" src="https://github.com/user-attachments/assets/30d46299-6fd6-4b09-94e8-e52df2aa72c6" />

<img width="1651" height="961" alt="Screenshot 2026-09-29 at 12 49 37 AM" src="https://github.com/user-attachments/assets/9e8d2d82-fd7f-4a30-b182-fdd032a814ce" />

<h2>OUTPUT :</h2>

<img width="1420" height="944" alt="Screenshot 2026-09-29 at 2 48 23 PM" src="https://github.com/user-attachments/assets/09b2a09b-e36f-4e95-a022-4759a6a4e616" />

<img width="1431" height="929" alt="Screenshot 2026-09-29 at 2 48 55 PM" src="https://github.com/user-attachments/assets/e4fef0d4-2ae2-4f71-b578-f99141b6a693" />

<img width="1430" height="918" alt="Screenshot 2026-09-29 at 2 49 18 PM" src="https://github.com/user-attachments/assets/86a3b108-773e-4ca9-91f5-25342de8f8eb" />

<img width="1434" height="947" alt="Screenshot 2026-09-29 at 2 49 36 PM" src="https://github.com/user-attachments/assets/b8596606-0abc-499c-b7f1-666171a3e7c1" />

<img width="1435" height="912" alt="Screenshot 2026-09-29 at 2 49 50 PM" src="https://github.com/user-attachments/assets/beb81f10-f7dc-4c4a-90e6-260f0d87104a" />

<img width="1429" height="937" alt="Screenshot 2026-09-29 at 2 50 06 PM" src="https://github.com/user-attachments/assets/36eadb79-d25a-4b64-bf7f-04575dfe03d0" />

<img width="1432" height="924" alt="Screenshot 2026-09-29 at 2 50 20 PM" src="https://github.com/user-attachments/assets/b5c15cb0-4154-47e7-bce4-35af8f86f924" />

<img width="1437" height="900" alt="Screenshot 2026-09-29 at 2 50 33 PM" src="https://github.com/user-attachments/assets/4b0abf0c-dce2-416b-9840-619ea2c00c40" />
















