import random
win = False
user_win = False

print("Welcome to the Fire, Water, Grass game!")

while win==False:
    user_input = input("Enter your choice (Fire, Water, Grass): ").strip().lower()
    choices = ["fire", "water", "grass"]
    opponent_choice = random.choice(choices)
    
    #tie statement
    if user_input == opponent_choice:
        print("It's a tie! Try again.")
    #user win statement
    elif (user_input == "fire" and opponent_choice == "grass"):
        user_win = True
        win = True
    elif (user_input == "water" and opponent_choice == "fire"):
        user_win = True
        win = True
    elif (user_input == "grass" and opponent_choice == "water"):
        user_win = True
        win = True
    #user lose statement
    elif (user_input == "fire" and opponent_choice == "water"):
        user_win = False
        win = True
    elif (user_input == "water" and opponent_choice == "grass"):
        user_win = False
        win = True
    else: #(user_input == "grass" and opponent_choice == "fire"):
        user_win = False
        win = True
    
        
    
#win statement
if user_win == True:
    print("You win! "+user_input+" beats "+opponent_choice+".")

#lose statement
if user_win == False:
    print("You lose! "+opponent_choice+" beats "+user_input+".")

rerun=input("Do you want to play again? (yes/no): ").strip().lower()
if rerun == "yes":
    win = False
else:
    print("Thanks for playing! Goodbye.")

