import streamlit as st
import random

win = False
user_win = False

choices = ["fire", "water", "grass"]
opponent_choice = random.choice(choices)

st.title("Welcome to the Fire, Water, Grass game!\nRules:\n- Fire beats Grass\n- Water beats Fire\n- Grass beats Water\nLet's play!\n")

while win == False:
    st.write("Select your choice (Fire, Water, Grass) ")

    if st.button("Fire"):
        user_input = "fire"

    if st.button("Water"):
        user_input = "water"

    if st.button("Grass"):
        user_input = "grass"

    if user_input == opponent_choice:
        st.write("It's a tie! Try again.")

    if (user_input == "fire" and opponent_choice == "grass") or (user_input == "water" and opponent_choice == "fire") or (user_input == "grass" and opponent_choice == "water"):
        user_win = True
        win = True

    if user_win == True:
        st.write("You win! "+user_input+" beats "+opponent_choice+".")

    if win == True and user_win == False:
        st.write("You lose! "+opponent_choice+" beats "+user_input+".")

    
