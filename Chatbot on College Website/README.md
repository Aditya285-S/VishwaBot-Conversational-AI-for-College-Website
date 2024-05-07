# Vishwa-bot: College Conversational AI

## Overview

Vishwa-bot is a project aimed at implementing an effective conversational AI system for a college website to address student queries efficiently, streamline administrative tasks, and enhance overall user experience and satisfaction.

## Methodology

The project leverages retrieval augmented generation (RAG) techniques with the Mistral-2-7B large language model (LLM) to handle college-related inquiries. The methodology can be broken down into the following key steps:

1. **Data Collection and Preprocessing**:
   - Collect information from the college website and preprocess documents to extract relevant information.
   - Tasks such as text normalization, tokenization, and removal of irrelevant content are performed.

2. **Text Embedding and Database Creation**:
   - Utilize the `sentence-transformers/all-MiniLM-L6-v2` model from Hugging Face to embed preprocessed text segments into high-dimensional vector embeddings.
   - Use the FAISS library for efficient creation of a vector database from the embedded text segments, enabling fast similarity search and retrieval operations.

3. **Retrieval QA Chain**:
   - Construct a retrieval QA chain integrating the Llama-2-7B model with the vector database retriever.
   - Process user queries, retrieve relevant documents from the vector database, and generate coherent responses based on the retrieved context.

## Challenges

The project encountered several challenges during development:

- **Data Collection and Storage**: Extracting and organizing data from the college website into a suitable format (e.g., PDFs) based on user queries.

- **Selection of Embedding Model**: Choosing the optimal embedding model to convert natural language data into vector embeddings, balancing between accuracy and computational efficiency.

## Future Improvements

Potential enhancements for Vishwa-bot include:

- Implementing automated data scraping and updating mechanisms to ensure database freshness.
  
- Experimenting with different language models or fine-tuning existing models to improve response accuracy.
  
- Optimizing system architecture for better scalability and reduced computational overhead.

## Results

### Results obtained from the model:

![](https://github.com/Aditya285-S/VishwaBot-Conversational-AI-for-College-Website/blob/main/Chatbot%20on%20College%20Website/Results/Result%201.png)


![](https://github.com/Aditya285-S/VishwaBot-Conversational-AI-for-College-Website/blob/main/Visualizations/Result1.png)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aditya285-S/VishwaBot-Conversational-AI-for-College-Website.git

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

1. **Create Embeddings:**

   ```bash
   python ingest.py

1. **Run the application:**

   ```bash
   chainlit run model.py
