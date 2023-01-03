import streamlit as st
import re


def bionic_reader(text):
    # Tokenize the text
    tokens = re.findall(r"\w+", text)

    # Separate the characters and apply the bolding rules
    formatted_text = ""
    for token in tokens:
        # Special characters at the beginning or end of a word are not highlighted
        if token[0].isalpha() and token[-1].isalpha():
            # Bold the appropriate number of characters
            length = len(token)
            if length <= 4:
                num_non_bold_chars = 1
            elif length <= 12:
                num_non_bold_chars = 2
            elif length <= 16:
                num_non_bold_chars = 3
            elif length <= 24:
                num_non_bold_chars = 4
            elif length <= 29:
                num_non_bold_chars = 5
            elif length <= 35:
                num_non_bold_chars = 6
            elif length <= 42:
                num_non_bold_chars = 7
            elif length <= 48:
                num_non_bold_chars = 8
            else:
                num_non_bold_chars = 9
            formatted_text += f"**{token[:length-num_non_bold_chars]}**{token[length-num_non_bold_chars:]} "
        else:
            formatted_text += f"{token} "

    return formatted_text


st.title("Bionic Reader!")
st.text_input("Enter Text", key="name")
st.write(f"{bionic_reader(st.session_state.name)}")
