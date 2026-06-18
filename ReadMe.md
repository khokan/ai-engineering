# AI Engineering

A modular framework for building **Retrieval-Augmented Generation (RAG)** pipelines. This project provides a ready-to-use environment for splitting documents, generating embeddings, and managing vector stores.

## Features

- **Text Splitting** — Recursive chunking via `langchain-text-splitters` with configurable `chunk_size` and `chunk_overlap`
- **Embeddings** — Sentence transformer models (`all-MiniLM-L6-v2`) for high-quality vector representations
- **Vector Store** — ChromaDB for scalable, persistent storage and retrieval of embeddings
- **NumPy integration** — Efficient numerical operations for embedding manipulation

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Setup

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

## Project Structure

```
ai-engineering/
├── main.py              # Entry point — orchestrates the RAG pipeline
├── requirements.txt     # Python dependencies
├── .gitignore
└── ReadMe.md
```

## Dependencies

| Package                    | Purpose                        |
| -------------------------- | ------------------------------ |
| `chromadb`                 | Vector database                |
| `sentence-transformers`    | Text embedding models          |
| `langchain-text-splitters` | Document chunking utilities    |
| `numpy`                    | Numerical array operations     |
