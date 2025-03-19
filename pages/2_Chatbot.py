import streamlit as st

st.title("Welcome to NLQ page")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = []

# The context input
input_data = st.text_input("Input your text here")
submit = st.button("Submit")

if submit:
    st.session_state["my_input"].append(input_data)

    for input in st.session_state["my_input"]:
        st.write(f"You entered {input}")