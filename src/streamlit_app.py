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
    api_key = st.text_input("Enter your OpenAI API key", type="password")

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
        user_input = st.text_input("You:").strip().lower()

        if user_input == "exit":
            st.write("Goodbye! Feel free to come back whenever you want to create a book.")
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
def get_option(options):
    # Print the available options
    st.write('BookBot:', 'Please select an option:')
    for i, option in enumerate(options):
        st.write(f'[{i + 1}] {option}')

    # Get the selection
    selection = int(st.text_input('You:'))

    return selection

# Generate a new book
def generate_book():
    global chapters, words_per_chapter, topic, category, tolerance, additional_parameters, book

    # Get the number of chapters
    st.write("BookBot:", "How many chapters should the book have?")
    chapters = int(st.text_input('You:'))

    # Get the number of words per chapter
    st.write("BookBot:", "How many words should each chapter have?")
    words_per_chapter = int(st.text_input('You:'))
    if words_per_chapter <= 1200:
        words_per_chapter = 1200
        st.write("BookBot:", "The number of words per chapter has been set to 1200. (The max number of words per chapter)")

    # Get the category of the book
    st.write("BookBot:", "What is the category of the book?")
    category = st.text_input('You:')

    # Get the topic of the book
    st.write("BookBot:", "What is the topic of the book?")
    topic = st.text_input('You:')

    # Get the tolerance of the book
    st.write("BookBot:", "What is the tolerance of the book? (0.8 means that 80% of the words will be written 100%)")
    tolerance = float(st.text_input('You:'))
    if tolerance < 0 or tolerance > 1:
        tolerance = 0.8

    # Initialize the Book
    st.write("BookBot:", "Initializing the book with the following parameters:")
    st.write(f"- Chapters: {chapters}")
    st.write(f"- Words per Chapter: {words_per_chapter}")
    st.write(f"- Category: {category}")
    st.write(f"- Topic: {topic}")
    st.write(f"- Tolerance: {tolerance}")
    
    # Continue with generating the book using these parameters
    # ...
    st.write("BookBot:", "Book generated successfully!")

# Run the chat app
if __name__ == '__main__':
    main_chat()
