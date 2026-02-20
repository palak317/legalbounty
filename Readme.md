# ⚖️ Legal Document Explainer Bot
**Simplifying legalese into plain English using Generative AI.**

## 📌 Project Overview
Legal documents are often dense, confusing, and filled with "legalese" that makes it difficult for non-lawyers to understand their rights and obligations. This project is an AI-powered assistant designed to ingest complex legal PDFs and generate concise, actionable summaries.

### 🚀 Key Features
- **PDF Upload & Parsing:** Seamlessly extract text from legal contracts and agreements.
- **Smart Summarization:** Powered by **Gemini 3 Flash**, it breaks down documents into:
  - **Core Agreement:** What is this document actually about?
  - **Key Obligations:** What actions are required from the user?
  - **Risk Assessment:** Highlighting potential "red flags" and liability clauses.
- **Interactive UI:** A clean, responsive dashboard built with **Streamlit**.

---

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **AI Engine:** [Google Gemini API](https://aistudio.google.com/) (Model: `gemini-3-flash-preview`)
- **PDF Processing:** `PyPDF2`
- **Language:** Python 3.10+

---

## 🏃 Getting Started

### Prerequisites
- Python 3.10 or higher.
- A Google AI Studio API Key.

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/palak317/legal-explainer-bot.git](https://github.com/palak317/legal-explainer-bot.git)
   cd legal-explainer-bot