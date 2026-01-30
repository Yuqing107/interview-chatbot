import streamlit as st

# st.title("_This_ is :blue[a little] :speech_balloon:")
# st.title("$E = mc^2$")

# st.header('This is a header')
# st.subheader('This is a subheader')

# st.text('This is a plain text with no format')
# st.markdown("# This is a header\n **This is bold text** \n -This is a list item")

# st.write('This is plain text using st.write')

# data = {"Name" : "Alice", "Age": "24", "Occupation":"Teacher"}
# st.write(data)

#----------------------------

with st.chat_message("AI"):
    st.write("Hello There!")

prompt = st.chat_input("Type your message", max_chars = 50)
if prompt:
    st.write(f"User Message: {prompt}")

