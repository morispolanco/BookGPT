import streamlit as st
from pyfiglet import Figlet
from book import Book
import json
import openai

# Initialize the OpenAI API key
api_key = None

# Initialize Book parameters
chapters = None
words_per_chapter = None
topic = None
category = None
tolerance = None
additional_parameters = {}

# Initialize Book object
book = None

# Configure the OpenAI API key
def configure_api_key():
    st.write("Hello! I'm BookBot. Please enter your OpenAI API key to get started.")
    api_key = st.text_input("Enter your OpenAI API key", type="password", key="api_key_input")

    if api_key:
        st.success("API key configured successfully!")
    
    return api_key

# Main chat function
def main_chat():
    st.title("BookBot - Your Personal Book Generator")

    # Configure API key
    api_key = configure_api_key()
    if not api_key:
        st.warning("Please enter a valid API key to continue.")
        return
    
    openai.api_key = api_key

    # Draw the title
    draw('BookGPT')

    # Chat loop
    while True:
        user_input = st.text_input("You:", key="user_input").strip().lower()

        if user_input == "exit":
            st.write("BookBot: Goodbye! Feel free to come back whenever you want to create a book.")
            break
        elif "generate a book" in user_input:
            st.write("BookBot: Great! Let's generate a book.")
            generate_book()
        else:
            st.write("BookBot: I'm here to help you generate a book. You can ask me to 'generate a book' or 'exit'.")

# Draw the given text in a figlet
def draw(text):
    # Create a new figlet object
    f = Figlet()

    # Print the figlet
    st.text(f.renderText(text))

# Get a selection from a list of options
def get_option(options, key):
    # Print the available options
    st.write('BookBot:', 'Please select an option:')
    for i, option in enumerate(options):
        st.write(f'[{i + 1}] {option}')

    # Get the selection
    selection = int(st.text_input('You:', key=key))

    return selection

# Generate a new book
def generate_book():
    global chapters, words_per_chapter, topic, category, tolerance, additional_parameters, book

    # Get the number of chapters
    st.write("BookBot:", "How many chapters should the book have?")
    chapters = int(st.text_input('You:', key="chapters_input"))

    # Rest of your generate_book() function...

# Run the chat app
if __name__ == '__main__':
    main_chat()
