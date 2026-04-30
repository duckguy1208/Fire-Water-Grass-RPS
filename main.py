import streamlit as st
import random

if 'win' not in st.session_state:
    st.session_state.win = False
    st.session_state.opponent_choice = random.choice(["fire", "water", "grass"])
    st.session_state.result = None

choices = ["fire", "water", "grass"]

def win_condition(user_input, opponent_choice):
    if user_input == opponent_choice:
        return "tie"
    elif (user_input == "fire" and opponent_choice == "grass") or (user_input == "water" and opponent_choice == "fire") or (user_input == "grass" and opponent_choice == "water"):
        return "win"
    else:
        return "lose"

st.title("Welcome to Fire, Water, Grass\n- Fire beats Grass\n- Water beats Fire\n- Grass beats Water")

st.write("Select your choice (Fire Water Grass) ")

# Disable buttons if game is already played
game_played = st.session_state.get('win', False)

if st.button("Fire", disabled=game_played):
    st.session_state.result = win_condition("fire", st.session_state.opponent_choice)
    st.session_state.win = True
    st.rerun()
    
if st.button("Water", disabled=game_played):
    st.session_state.result = win_condition("water", st.session_state.opponent_choice)
    st.session_state.win = True
    st.rerun()

if st.button("Grass", disabled=game_played):
    st.session_state.result = win_condition("grass", st.session_state.opponent_choice)
    st.session_state.win = True
    st.rerun()


if st.session_state.result == "win":
    st.write("You win! ")
    st.write("Congratulations! Thanks for playing!")

elif st.session_state.result == "lose":
    st.write("You lose! ")
    st.write("Thanks for playing! Try again to beat the opponent.")

elif st.session_state.result == "tie":
    st.write("It's a tie! Try again.")

st.divider()

if st.button("Play Again"):
    st.session_state.win = False
    st.session_state.opponent_choice = random.choice(choices)
    st.session_state.result = None
    st.rerun()