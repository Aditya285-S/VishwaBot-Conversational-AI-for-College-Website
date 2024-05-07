from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma, FAISS

DB_FAISS_PATH = 'vectorstore\db_faiss'

def get_response(text):

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model_kwargs = {"device": "cpu"}
    embeddings_hf = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)


    vectorstore = FAISS.load_local(DB_FAISS_PATH, embeddings_hf, allow_dangerous_deserialization=True)


    llm = ChatGroq(temperature=0.2, model_name="mixtral-8x7b-32768", groq_api_key="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")


    rag_template = """Use the following pieces of information to answer the user's question.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    Context: {context}
    Question: {question}

    Only return the helpful answer below and nothing else.
    Helpful answer:
    """


    rag_prompt = ChatPromptTemplate.from_template(rag_template)
    qa_chain = RetrievalQA.from_chain_type(
        llm, retriever=vectorstore.as_retriever(), chain_type_kwargs={"prompt": rag_prompt},
    )


    response = qa_chain.invoke(text)

    return response['result']