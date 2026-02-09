import random

print("Welcome to the Fire, Water, Grass game!\nRules:\n- Fire beats Grass\n- Water beats Fire\n- Grass beats Water\nLet's play!\n")

#counters for wins, losses, and ties
win_counter = 0
lose_counter = 0
tie_counter = 0

play_again = True
while play_again:
    win = False
    user_win = False
    while win==False:
        user_input = input("Enter your choice (Fire, Water, Grass): ").strip().lower()
        choices = ["fire", "water", "grass"]
        opponent_choice = random.choice(choices)
        
        #tie statement
        if user_input == opponent_choice:
            print("It's a tie! Try again.")
            tie_counter += 1
        #user win statement
        elif (user_input == "fire" and opponent_choice == "grass"):
            user_win = True
            win = True
            win_counter += 1
        elif (user_input == "water" and opponent_choice == "fire"):
            user_win = True
            win = True
            win_counter += 1
        elif (user_input == "grass" and opponent_choice == "water"):
            user_win = True
            win = True
            win_counter += 1
        #user lose statement
        elif (user_input == "fire" and opponent_choice == "water"):
            user_win = False
            win = True
            lose_counter += 1
        elif (user_input == "water" and opponent_choice == "grass"):
            user_win = False
            win = True
            lose_counter += 1
        elif (user_input == "grass" and opponent_choice == "fire"):
            user_win = False
            win = True
            lose_counter += 1
        else:
            print("Invalid input. Please enter Fire, Water, or Grass.")
    
            
    
    #win statement
    if user_win == True:
        print("You win! "+user_input+" beats "+opponent_choice+".")
    
    #lose statement
    if user_win == False:
        print("You lose! "+opponent_choice+" beats "+user_input+".")
    
    rerun=input("Do you want to play again? (yes/no): ").strip().lower()
    if rerun == "yes":
        play_again = True
    elif rerun == "no":
        play_again = False
        print("Thanks for playing! Goodbye.")
        print("Your final score: "+str(win_counter)+" wins, "+str(lose_counter)+" losses, and "+str(tie_counter)+" ties.")
    else:
        play_again = False
        print("Invalid input. Exiting the game. Goodbye.")
        print("Your final score: "+str(win_counter)+" wins, "+str(lose_counter)+" losses, and "+str(tie_counter)+" ties.")

        