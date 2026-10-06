import string
from collections import Counter

import pandas as pd
import streamlit as st

st.title("Text Analysis")
st.write("Paste any text to count its words, characters, vowels and repeated words.")

default_text = (
    "Python is a popular language for data analysis. Python is easy to learn, and data analysis "
    "with Python is fun. Many students learn Python because Python is simple and powerful. "
    "Data helps us make better decisions, and good decisions need good data."
)
text = st.text_area("Text", value=default_text, height=180)

if text.strip() == "":
    st.error("Please enter some text.")
else:
    word_count = len(text.split())
    char_count = len(text)
    char_no_space = len("".join(text.split()))
    vowel_count = sum(1 for ch in text.lower() if ch in "aeiou")

    c1, c2 = st.columns(2)
    c1.metric("Words", word_count)
    c2.metric("Characters (with spaces)", char_count)
    c3, c4 = st.columns(2)
    c3.metric("Characters (no spaces)", char_no_space)
    c4.metric("Vowels", vowel_count)

    clean_text = text.lower().translate(str.maketrans("", "", string.punctuation))
    freq = Counter(clean_text.split())
    repeated = sorted(
        [(word, count) for word, count in freq.items() if count > 1],
        key=lambda item: (-item[1], item[0]),
    )

    st.header("Repeated words")
    if repeated:
        df = pd.DataFrame(repeated, columns=["Word", "Count"])
        st.table(df)
        st.bar_chart(df.set_index("Word")["Count"])
    else:
        st.write("No repeated words found.")
