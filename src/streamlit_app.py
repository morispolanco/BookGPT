import streamlit as st
from pyfiglet import Figlet
from book import Book
import json
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API


# Draw the given text in a figlet
def draw(text):
    # Create a new figlet object
    f = Figlet()

    # Print the figlet
    st.text(f.renderText(text))

# Get a selection from a list of options
def get_option(options):
    # Print the available options
    st.write('Please select an option:')
    for i, option in enumerate(options):
        st.write(f'[{i + 1}] {option}')

    # While the user input is not valid
    while True:
        try:
            # Get the selection
            selection = int(st.text_input('> '))

            # Check if the selection is valid
            if selection < 1 or selection > len(options):
                raise ValueError

            # Return the selection
            return selection

        # User input was not valid
        except ValueError:
            st.write('Invalid option. Please try again.')

# Main function
def main():
    # Set the OpenAI API key
    openai.api_key = get_api_key()

    # Draw the title
    draw('BookGPT')

    # Check if the user wants to generate a new book or not
    if get_option(['Generate a book', 'Exit']) - 1:
        return

    # Get the number of chapters
    st.write('How many chapters should the book have?')
    chapters = int(st.text_input('> '))

    # Get the number of words per chapter
    st.write('How many words should each chapter have?')
    # Check if it is below 1200
    words = int(st.text_input('> '))
    if words <= 1200:
        words = 1200
        st.write('The number of words per chapter has been set to 1200. (The max number of words per chapter)')

    # Get the category of the book
    st.write('What is the category of the book?')
    category = st.text_input('> ')

    # Get the topic of the book
    st.write('What is the topic of the book?')
    topic = st.text_input('> ')

    # What is the tolerance of the book?
    st.write('What is the tolerance of the book? (0.8 means that 80% of the words will be written 100%)')
    tolerance = float(st.text_input('> '))
    if tolerance < 0 or tolerance > 1:
        tolerance = 0.8

    # Do you want to add any additional parameters?
    st.write('Do you want to add any additional parameters?')
    if get_option(['No', 'Yes']) - 1:
        st.write('Please enter the additional parameters in the following format: "parameter1=value1, parameter2=value2, ..."')
        additional_parameters = st.text_input('> ')
        additional_parameters = additional_parameters.split(', ')
        for i in range(len(additional_parameters)):
            additional_parameters[i] = additional_parameters[i].split('=')
        additional_parameters = dict(additional_parameters)
    else:
        additional_parameters = {}

    # Initialize the Book
    book = Book(chapters=chapters, words_per_chapter=words, topic=topic, category=category, tolerance=tolerance,
                **additional_parameters)

    # Print the title
    st.write(f'Title: {book.get_title()}')

    # Ask if he wants to change the title until he is satisfied
    while True:
        st.write('Do you want to generate a new title?')
        if get_option(['No', 'Yes']) - 1:
            st.write(f'Title: {book.get_title()}')
        else:
            break

    # Print the structure of the book
    st.write('Structure of the book:')
    structure, _ = book.get_structure()
    st.write(structure)

    # Ask if he wants to change the structure until he is satisfied
    while True:
        st.write('Do you want to generate a new structure?')
        if get_option(['No', 'Yes']) - 1:
            st.write('Structure of the book:')
            structure, _ = book.get
