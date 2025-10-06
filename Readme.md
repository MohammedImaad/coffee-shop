# ☕ Coffee Ordering Assistant

## 🧠 Concept
A conversational AI system for ordering coffee — directly from your table.  
It supports **voice or text** prompts, understands natural language, and handles **secure blockchain payments** via **Latinum.ai** using **USDC on Solana**.

Users can chat naturally, ask questions about coffee, place orders, and pay — all in one conversation.

---

## ⚙️ System Architecture

### 1. Data Ingestion Pipeline (`data_ingestion.py`)
- Loads `coffee_knowledge_base.pdf` via **LangChain PyPDFLoader**.  
- Splits content using `RecursiveCharacterTextSplitter`.
- Generates embeddings using **SentenceTransformer** (`all-MiniLM-L6-v2`).
- Stores vectors in a **ChromaDB** persistent store.

**Purpose:** Enables RAG (Retrieval-Augmented Generation) for contextual responses about coffee.

---

### 2. Retriever (`retriever_file.py`)
- Loads stored embeddings from **ChromaDB**.
- Converts user queries to embeddings and retrieves top 3 relevant chunks.
- Provides context for GPT-based responses.

**Purpose:** Supplies real, factual coffee knowledge to the assistant.

---

### 3. Graph Builder (`langgraph_flow.py`)
- Builds a **LangGraph** state machine for conversation handling.
- Uses **GPT-4 (ChatOpenAI)** with blockchain tools:
  - `wallet_info`
  - `signed_tx`
  - `credit`
  - `send_money_to_wallet`
- Interacts with **Latinum.ai** and **MCP** for blockchain functions.
- Implements guardrails for secure, compliant transactions.

**Purpose:** Orchestrates reasoning, retrieval, and blockchain actions dynamically.

---

### 4. MCP Integration (`mcp_helpers.py`)
- Launches **Latinum Wallet MCP server** (`latinum-wallet-mcp`).
- Handles:
  - Session management
  - Wallet info retrieval
  - Transaction signing
  - Fund transfers

**Purpose:** Bridges the assistant securely with blockchain wallet operations.

---

### 5. Payment Processor (`test_payment.py`)
- Uses **Latinum Facilitator API** (`https://facilitator.latinum.ai/api/facilitator`).
- Steps:
  1. Signs transactions using MCP wallet.
  2. Sends signed TX to Facilitator API.
  3. Confirms transaction success & payment details.
- Uses **USDC on Solana** as default stablecoin.

**Purpose:** Executes real-time, verified, on-chain payments.

---

### 6. FastAPI Backend (`main.py`)
- Initializes the **LangGraph** flow on startup.
- Exposes `/chat` endpoint to handle AI conversation.
- Integrates CORS for frontend connection (`http://localhost:8080`).

**Purpose:** Provides HTTP API layer for real-time communication with frontend.

---

## 🧩 Frontend
- Built using **JavaScript (Vue or React)**.
- Connects to backend at `http://localhost:8000/chat`.
- Allows users to chat, order, and view AI-generated images/responses.

Run locally:
```bash
cd frontend
npm run dev
```

---

## 🖥️ Running the Project

### Backend Setup
```bash
cd backend
source venv/bin/activate
python main.py
```

Backend: `http://localhost:8000`  
Frontend: `http://localhost:8080`

---

## 🧱 Tech Stack Overview

| Layer | Tools / Libraries |
|-------|-------------------|
| **AI / NLP** | LangChain, LangGraph, GPT-4 (OpenAI), SentenceTransformers |
| **Vector DB** | ChromaDB |
| **Backend Framework** | FastAPI |
| **Blockchain / Payments** | Latinum.ai (MCP Wallet + Facilitator API), USDC (Solana) |
| **Frontend** | JavaScript (npm-based) |
| **Environment Management** | Python venv, dotenv |
| **Deployment** | Localhost (Dev Mode) |

---

## 🧾 License
This project is for **educational and research** purposes only.  
Ensure compliance with local crypto and payment regulations before deploying in production.

---

## 💡 Author Notes
Built to demonstrate AI + Blockchain integration for real-world conversational experiences.
