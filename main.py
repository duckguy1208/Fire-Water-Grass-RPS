import streamlit as st
import random

if 'win' not in st.session_state:
    st.session_state.win = False
    st.session_state.opponent_choice = random.choice(["fire", "water", "grass"])
    st.session_state.result = None

if "button_disabled" not in st.session_state:
    st.session_state.button_disabled = False

choices = ["fire", "water", "grass"]

def disable_button():
    st.session_state.button_disabled = True
   
def win_condition(user_input, opponent_choice):
    if user_input == opponent_choice:
        return "tie"
    elif (user_input == "fire" and opponent_choice == "grass") or (user_input == "water" and opponent_choice == "fire") or (user_input == "grass" and opponent_choice == "water"):
        return "win"
    else:
        return "lose"

st.title("Welcome to Fire, Water, Grass\nRules:\n- Fire beats Grass\n- Water beats Fire\n- Grass beats Water")

st.write("Select your choice (Fire, Water, Grass) ")

if not st.session_state.win:
    if st.button("Fire", disabled=st.session_state.button_disabled):
        st.session_state.result = win_condition("fire", st.session_state.opponent_choice)
        if st.session_state.result != "tie":
            disable_button()
        
    if st.button("Water", disabled=st.session_state.button_disabled):
        st.session_state.result = win_condition("water", st.session_state.opponent_choice)
        if st.session_state.result != "tie":
            disable_button()

    if st.button("Grass", disabled=st.session_state.button_disabled):
        st.session_state.result = win_condition("grass", st.session_state.opponent_choice)
        if st.session_state.result != "tie":
            disable_button()


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
    st.session_state.button_disabled = False
    st.rerun()