import streamlit as st
from core.langchain_helper import create_vector_db_from_youtube, get_response_from_query
import textwrap

st.title('YouTube assistant')

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label='Enter a YouTube video URL',
            max_chars=50
        )
        query = st.sidebar.text_area(
            label='Ask me about the video',
            max_chars=50,
            key='query'
        )

        submit_button = st.form_submit_button(label='Submit')
        
if query and youtube_url:
    db = create_vector_db_from_youtube(video_url=youtube_url)
    response = get_response_from_query(query=query, db=db, k=3)
    
    st.subheader("Answer: ")
    st.text(textwrap.fill(response, width=100))
