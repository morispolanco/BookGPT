import streamlit as st
import openai
from book import Book
from utils import get_categories

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key

    def initialize():
        # Verificar si la clave de la API es válida
        try:
            openai.Engine.list()
            return True
        except openai.error.AuthenticationError:
            return False

    def generate_book(chapters, words, category, topic, language):
        book = Book(chapters, words, topic, category, language)
        content = book.get_md()
        return content

    def show_form():
        # Crear formulario para la entrada del usuario
        with st.form('BookGPT'):
            # Obtener el número de capítulos
            chapters = st.number_input('How many chapters should the book have?', min_value=3, max_value=100, value=5)

            # Obtener el número de palabras por capítulo
            words = st.number_input('How many words should each chapter have?', min_value=100, max_value=3500, value=1000, step=50)

            # Obtener la categoría del libro
            category = st.selectbox('What is the category of the book?', get_categories())

            # Obtener el tema del libro
            topic = st.text_input('What is the topic of the book?', placeholder='e.g. "Finance"')

            # Obtener el idioma del libro
            language = st.text_input('What is the language of the book?', placeholder='e.g. "English"')

            # Botón de envío
            submit = st.form_submit_button('Generate')

            # Verificar si todos los campos están completos
            if submit and not (chapters and words and category and topic and language):
                st.error('Please fill in all fields!')

            # Generar el libro
            elif submit:
                content = generate_book(chapters, words, category, topic, language)
                st.text(content)

    def main():
        # Título centrado
        st.title('BookGPT')
        st.text('---')

        # Mostrar el formulario
        show_form()

    if __name__ == "__main__":
        main()
