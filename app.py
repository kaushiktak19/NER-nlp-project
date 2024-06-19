import streamlit as st
import spacy_streamlit as spt
import spacy

nlp = spacy.load('en_core_web_sm')

def main():
    st.title('Named Entity Recognition (NER) APP')

    menu = ['Home', 'NER']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Word Tokenization')
        raw_text = st.text_area('Text To Tokenize', 'Enter Text Here')
        docs = nlp(raw_text)
        if st.button('Tokenize'):
            spt.visualize_tokens(docs)

    elif choice == 'NER':
        st.subheader('Named Entity Recognition')
        raw_text = st.text_area('Text To Analyze', 'Enter Text Here')
        docs = nlp(raw_text)
        if st.button('Show NER'):
            spt.visualize_ner(docs)
        #spt.visualize_ner(docs)

if __name__ == '__main__':
    main()
