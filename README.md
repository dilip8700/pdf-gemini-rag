````md
# 📄 PDF Gemini RAG  

A simple yet powerful **PDF Question Answering System** using **Gemini API**.  
This project allows you to upload PDFs, process them into embeddings, and ask natural language questions with accurate responses powered by Google Gemini.  

---

## 🚀 Features  

- 📂 **PDF Upload & Parsing** – Extracts text from PDFs.  
- 🧩 **Chunking** – Splits text into manageable chunks for embeddings.  
- 🔎 **Vector Search** – Uses FAISS to store and search embeddings.  
- 🤖 **Gemini API Integration** – Get intelligent answers from your PDF data.  
- 💡 **RAG (Retrieval Augmented Generation)** – Combines retrieved context with Gemini’s LLM.  

---

## 📂 Project Structure  

```text
pdf-gemini-rag/
│── main.py              # Main application file  
│── requirements.txt     # Python dependencies  
│── README.md            # Project documentation  
│── data/                # Store PDFs here  
│── faiss_index/         # FAISS vector index storage  
````

---

## ⚡ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/dilip8700/pdf-gemini-rag.git
cd pdf-gemini-rag
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Script

```bash
python main.py
```

---

## 🛠️ Usage

1. Place your **PDFs** inside the `data/` folder.
2. Run the script:

```bash
python main.py
```

3. Enter your **Gemini API Key** directly in the code (`main.py`).
4. Ask questions like:

```text
Question: What is the main topic of this document?
```

Output:

```text
Answer: The PDF discusses modern cloud computing with Kubernetes and DevOps pipelines.
```

---

## 📦 Requirements

Your `requirements.txt` file should look like this:

```txt
google-generativeai
sentence-transformers
faiss-cpu
numpy
PyPDF2
```

---

## 🌐 API Key Setup

Edit `main.py` and replace:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

with your actual **Gemini API Key**.

---

## 🤝 Contributing

Contributions are welcome! 🚀

* Fork the repo
* Create a new branch (`feature-xyz`)
* Commit your changes
* Submit a PR

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on [GitHub](https://github.com/dilip8700/pdf-gemini-rag.git)!

```
```

