from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

video_url = 'https://www.youtube.com/watch?v=lG7Uxts9SXs&list=PLPFBjI6lbnOIswGu1oVqF9w3gaEWM5y2_&index=4'

def create_vector_db_from_youtube(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)
    
    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    return db
