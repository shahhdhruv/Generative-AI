from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("facts.txt")
docs = loader.load()
    
text_splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)
documents=text_splitter.split_documents(docs)
# print(documents[:5])

doc = documents[:50]

db = Chroma.from_documents(
    doc,
    embedding=OllamaEmbeddings(),
    persist_directory="emb"
)

results = db.similarity_search(
    "What is a fact about Great Wall of China"
)

for result in results:
    print("\n")
    print(result.page_content)
