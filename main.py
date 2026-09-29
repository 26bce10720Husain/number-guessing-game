import random
import time
#__________________________________________________NUMBER GUESSING GAME______________________________________________________
high_score = 0
high_score_name = "Nobody"

total_games = 0
total_wins = 0
total_losses = 0

game_history = []

print("===========================================================================================================")
print("                                       WELCOME TO NUMBER GUESSING GAME")
print("===========================================================================================================")
print()
name = input("ENTER YOUR NAME : ")

if name == "":
    name = "Player"
    
print()
print("HELLO", name.upper(), "!")
print("LET'S START THE GAME")
print()

while True:

    print("==============================================")
    print("                 MAIN MENU")
    print("==============================================")
    print()
    print("1 : START NEW GAME")
    print()
    print("2 : VIEW RULES")
    print()
    print("3 : VIEW HIGH SCORE")
    print()
    print("4 : VIEW GAME HISTORY")
    print()
    print("5 : VIEW GAME STATISTICS")
    print()
    print("6 : EXIT GAME")
    print()

    try:

        menu_choice = int(input("ENTER YOUR CHOICE : "))
        print()

    except ValueError:

        print("INVALID INPUT")
        print("PLEASE ENTER A NUMBER FROM THE MENU")
        print()
        continue
#_________________________________________START NEW GAME________________________________________________________
    if menu_choice == 1:

        total_games = total_games + 1

        print("==============================================")
        print("             CHOOSE YOUR LEVEL")
        print("==============================================")
        print()
        print("1 : LEVEL EASY")
        print("    RANGE : 1 TO 100")
        print("    ATTEMPTS : 10")
        print()
        print("2 : LEVEL MEDIUM")
        print("    RANGE : 1 TO 500")
        print("    ATTEMPTS : 12")
        print()
        print("3 : LEVEL HARD")
        print("    RANGE : 1 TO 1000")
        print("    ATTEMPTS : 15")
        print()
        print("4 : BACK TO MAIN MENU")
        print()

        try:

            choice = int(input("ENTER YOUR CHOICE 1, 2 OR 3 : "))
            print()

        except ValueError:

            print("INVALID INPUT")
            print("RETURNING TO MAIN MENU")
            print()
            continue
# __________________________EASY LEVEL___________________________________
        if choice == 1:

            level_name = "EASY"
            lower_limit = 1
            upper_limit = 100
            maximum_attempts = 10
            points_per_attempt = 10
#_________________________________MEDIUM LEVEL___________________________________________

        elif choice == 2:

            level_name = "MEDIUM"
            lower_limit = 1
            upper_limit = 500
            maximum_attempts = 12
            points_per_attempt = 20
#____________________________________HARD LEVEL________________________________________
        elif choice == 3:

            level_name = "HARD"
            lower_limit = 1
            upper_limit = 1000
            maximum_attempts = 15
            points_per_attempt = 30
#___________________________________BACK TO THE MENU_____________________________________
        elif choice == 4:

            print("RETURNING TO MAIN MENU")
            print()
            continue
#________________INVAlID LEVEL ENTERED________________
        else:

            print("WRONG CHOICE")
            print("PLEASE SELECT 1, 2 OR 3")
            print()
            continue
#_____________________________GAME LOGIC_________________________________
        secret_number = random.randint(lower_limit, upper_limit)

        count = 0
        hints_used = 0
        game_won = False

        print("==============================================")
        print("            ", level_name, "LEVEL STARTED")
        print("==============================================")
        print()

        print("HELLO", name.upper())
        print()
        print("I HAVE CHOSEN A NUMBER BETWEEN", lower_limit, "AND", upper_limit)
        print()
        print("YOU HAVE", maximum_attempts, "ATTEMPTS")
        print()

        print("SPECIAL OPTIONS")
        print()
        print("TYPE 0 FOR A HINT")
        print()
        print("TYPE -1 TO QUIT THE CURRENT GAME")
        print()

        time.sleep(1)

        # ---------------------------------------------
        # GUESSING LOOP
        # ---------------------------------------------

        while count < maximum_attempts:

            attempts_left = maximum_attempts - count

            print("----------------------------------------------")
            print("ATTEMPTS LEFT :", attempts_left)
            print("----------------------------------------------")

            try:

                guess = int(input("ENTER YOUR GUESS : "))
                print()

            except ValueError:

                print("INVALID INPUT")
                print("PLEASE ENTER A VALID NUMBER")
                print()
                continue

            # ---------------------------------------------
            # HINT OPTION
            # ---------------------------------------------

            if guess == 0:

                hints_used = hints_used + 1

                if secret_number % 2 == 0:

                    print("HINT : THE SECRET NUMBER IS EVEN")

                else:

                    print("HINT : THE SECRET NUMBER IS ODD")

                print("HINTS USED :", hints_used)
                print()
                continue

            # ---------------------------------------------
            # QUIT CURRENT GAME
            # ---------------------------------------------

            elif guess == -1:

                print("YOU QUIT THE CURRENT GAME")
                print("THE SECRET NUMBER WAS :", secret_number)
                print()

                game_history.append(
                    name + " played " + level_name + " level and quit the game."
                )

                break

            # ---------------------------------------------
            # RANGE VALIDATION
            # ---------------------------------------------

            elif guess < lower_limit or guess > upper_limit:

                print("PLEASE ENTER A NUMBER BETWEEN", lower_limit, "AND", upper_limit)
                print()
                continue

            # Valid guess is counted here
            count = count + 1

            # ---------------------------------------------
            # LOW GUESS
            # ---------------------------------------------

            if guess < secret_number:

                print("YOUR GUESS IS TOO LOW")
                print("TRY A HIGHER NUMBER")
                print()

                difference = secret_number - guess

                if difference <= 10:

                    print("YOU ARE VERY CLOSE!")
                    print()

            # ---------------------------------------------
            # HIGH GUESS
            # ---------------------------------------------

            elif guess > secret_number:

                print("YOUR GUESS IS TOO HIGH")
                print("TRY A LOWER NUMBER")
                print()

                difference = guess - secret_number

                if difference <= 10:

                    print("YOU ARE VERY CLOSE!")
                    print()

            # ---------------------------------------------
            # CORRECT GUESS
            # ---------------------------------------------

            elif guess == secret_number:

                game_won = True
                total_wins = total_wins + 1

                print("==============================================")
                print("            WOHOO ! YOU WON THE GAME")
                print("==============================================")
                print()

                print("CORRECT NUMBER :", secret_number)
                print("YOU TOOK", count, "ATTEMPTS")
                print("HINTS USED :", hints_used)
                print()

                # ---------------------------------------------
                # SCORE CALCULATION
                # ---------------------------------------------

                remaining_attempts = maximum_attempts - count

                score = remaining_attempts * points_per_attempt

                hint_deduction = hints_used * 10

                score = score - hint_deduction

                if score < 0:
                    score = 0

                print("YOUR SCORE :", score)
                print()

                # ---------------------------------------------
                # HIGH SCORE UPDATE
                # ---------------------------------------------

                if score > high_score:

                    high_score = score
                    high_score_name = name

                    print("==============================================")
                    print("           NEW HIGH SCORE CREATED!")
                    print("==============================================")
                    print()

                    print("CONGRATULATIONS", name.upper())
                    print("YOUR NEW HIGH SCORE IS :", high_score)
                    print()

                else:

                    print("CURRENT HIGH SCORE :", high_score)
                    print("HIGH SCORE HOLDER :", high_score_name)
                    print()

                # ---------------------------------------------
                # SAVE WIN HISTORY
                # ---------------------------------------------

                game_history.append(
                    name + " won " + level_name +
                    " level in " + str(count) +
                    " attempts with score " + str(score)
                )

                break

        # ---------------------------------------------
        # GAME OVER WHEN ATTEMPTS FINISH
        # ---------------------------------------------

        if count == maximum_attempts and game_won == False:

            total_losses = total_losses + 1

            print("==============================================")
            print("                 GAME OVER")
            print("==============================================")
            print()

            print("YOU HAVE USED ALL YOUR ATTEMPTS")
            print("THE SECRET NUMBER WAS :", secret_number)
            print()

            game_history.append(
                name + " lost " + level_name +
                " level. Secret number was " + str(secret_number)
            )

    # ---------------------------------------------
    # VIEW RULES
    # ---------------------------------------------

    elif menu_choice == 2:

        print("==============================================")
        print("                  GAME RULES")
        print("==============================================")
        print()

        print("1. SELECT A DIFFICULTY LEVEL.")
        print()
        print("2. GUESS THE SECRET NUMBER IN THE GIVEN RANGE.")
        print()
        print("3. YOU HAVE LIMITED ATTEMPTS IN EVERY LEVEL.")
        print()
        print("4. TYPE 0 IF YOU WANT A HINT.")
        print()
        print("5. TYPE -1 IF YOU WANT TO QUIT THE GAME.")
        print()
        print("6. FEWER ATTEMPTS GIVE YOU A HIGHER SCORE.")
        print()
        print("7. USING HINTS WILL REDUCE YOUR SCORE.")
        print()
        print("8. THE HIGHEST SCORE IS SAVED AS HIGH SCORE.")
        print()

    # ---------------------------------------------
    # VIEW HIGH SCORE
    # ---------------------------------------------

    elif menu_choice == 3:

        print("==============================================")
        print("                HIGH SCORE BOARD")
        print("==============================================")
        print()

        if high_score == 0:

            print("NO HIGH SCORE AVAILABLE YET")
            print("PLAY A GAME TO CREATE A HIGH SCORE")
            print()

        else:

            print("HIGH SCORE :", high_score)
            print("HIGH SCORE HOLDER :", high_score_name)
            print()

    # ---------------------------------------------
    # VIEW GAME HISTORY
    # ---------------------------------------------

    elif menu_choice == 4:

        print("==============================================")
        print("                 GAME HISTORY")
        print("==============================================")
        print()

        if len(game_history) == 0:

            print("NO GAME HISTORY AVAILABLE")
            print()

        else:

            history_number = 1

            for item in game_history:

                print(history_number, ":", item)

                history_number = history_number + 1

            print()

    # ---------------------------------------------
    # VIEW STATISTICS
    # ---------------------------------------------

    elif menu_choice == 5:

        print("==============================================")
        print("                GAME STATISTICS")
        print("==============================================")
        print()

        print("PLAYER NAME :", name)
        print()
        print("TOTAL GAMES PLAYED :", total_games)
        print()
        print("TOTAL GAMES WON :", total_wins)
        print()
        print("TOTAL GAMES LOST :", total_losses)
        print()
        print("CURRENT HIGH SCORE :", high_score)
        print()

        if total_games > 0:

            win_percentage = (total_wins / total_games) * 100

            print("WIN PERCENTAGE :", round(win_percentage, 2), "%")
            print()

        else:

            print("WIN PERCENTAGE : 0 %")
            print()

    # ---------------------------------------------
    # EXIT GAME
    # ---------------------------------------------

    elif menu_choice == 6:

        print("==============================================")
        print("         THANK YOU FOR PLAYING THE GAME")
        print("==============================================")
        print()

        print("PLAYER :", name)
        print()
        print("TOTAL GAMES PLAYED :", total_games)
        print()
        print("TOTAL WINS :", total_wins)
        print()
        print("TOTAL LOSSES :", total_losses)
        print()
        print("FINAL HIGH SCORE :", high_score)
        print()
        print("HIGH SCORE HOLDER :", high_score_name)
        break

    # ---------------------------------------------
    # INVALID MAIN MENU OPTION
    # ---------------------------------------------

    else:

        print("WRONG CHOICE")
        print("PLEASE CHOOSE A VALID MENU OPTION")
        print()