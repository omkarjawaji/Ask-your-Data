import streamlit as st
import pandas as pd
from data_analyzer import DataAnalyzer
import os


st.title('Talk to your Data 🙌')

uploaded_file = st.file_uploader('Choose a CSV file', type=['csv'])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write('File uploaded successfully!')
    st.write(data.head())
    st.session_state['data'] = data

    query = st.text_input("Ask your question:")

    reply_format = st.selectbox('Select reply format', ['Textual', 'Tabular', 'Visualizations'])

    if query:
        try:
            DI = DataAnalyzer(st.session_state['data'])
            result = DI.interpret_question(query)
            st.write('Reply:')
            st.write(result)
        except Exception as e:
            st.error(f'Error: {e}')

st.sidebar.text("DataxChat developed by Omkar Jawaji")
