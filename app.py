import streamlit as st
import random

# List of sample quotes
QUOTES = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    "Opportunities don't happen, you create them. – Chris Grosser",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
]

def get_random_quote():
    return random.choice(QUOTES)

# Streamlit UI
st.set_page_config(page_title="Random Quote Generator", page_icon="✨", layout="centered")

st.title("✨ Random Quote Generator")
st.write("Click the button below to get inspired with a random quote.")

if st.button("Generate Quote"):
    quote = get_random_quote()
    st.success(quote)
