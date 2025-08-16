import google.generativeai as genai
import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# ======================
# 1. Setup Gemini API
# ======================
API_KEY = "YOUR GEMINI API KEY HERE"
genai.configure(api_key=API_KEY)

# ======================
# 2. Load PDF and extract text
# ======================
def load_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

pdf_text = load_pdf("YOUR PDF PATH HERE")

# ======================
# 3. Split text into chunks
# ======================
def chunk_text(text, chunk_size=300):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

chunks = chunk_text(pdf_text)

# ======================
# 4. Create embeddings with SentenceTransformer
# ======================
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

# ======================
# 5. Store in FAISS index
# ======================
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# ======================
# 6. Retrieve relevant chunks
# ======================
def retrieve(query, top_k=3):
    q_emb = model.encode([query])
    distances, indices = index.search(np.array(q_emb), top_k)
    return [chunks[i] for i in indices[0]]

# ======================
# 7. Ask Gemini with context
# ======================
def ask_gemini(query):
    context = "\n".join(retrieve(query))
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    
    response = genai.GenerativeModel("gemini-2.5-pro").generate_content(prompt)
    return response.text

# ======================
# 8. Example query
# ======================
if __name__ == "__main__":
    question = "Summarize the key points of this PDF."
    answer = ask_gemini(question)
    print("Q:", question)
    print("A:", answer)

