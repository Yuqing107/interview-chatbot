import streamlit as st


st.title("Nested Button Example")

if 'show_second_button' not in st.session_state:
    st.session_state.show_second_button = False

if st.button("First Button"):
    st.session_state.show_second_button = True

if st.session_state.show_second_button:
   st.write("Revealed")
   if st.button("Second Button"):
        st.write("Second Button Clicked")

