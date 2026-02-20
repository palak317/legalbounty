import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# --- 1. API SETUP ---
# For local testing, you can paste your key here.
# For hosting, use st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="Legal Ease Bot", layout="centered")
st.title("⚖️ Legal Document Explainer")


# --- 2. HELPER FUNCTIONS ---
def get_pdf_text(pdf_docs):
    text = ""
    pdf_reader = PdfReader(pdf_docs)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def get_gemini_response(input_text):
    # gemini-3-flash-preview is the latest and best for agentic tasks like summarization
    model = genai.GenerativeModel('gemini-3-flash-preview')# 'flash' is faster for summaries
    prompt = f"""
    You are a professional legal assistant. Please simplify the following 
    legal document into a summary that a common person can understand.
    Break it down into:
    - Summary of the agreement
    - Important Deadlines
    - Potential Risks or Red Flags

    Document Text: {input_text}
    """
    response = model.generate_content(prompt)
    return response.text


# --- 3. UI ---
uploaded_file = st.file_uploader("Upload your legal document (PDF)", type="pdf")

if uploaded_file is not None:
    if st.button("Analyze Document"):
        with st.spinner("Processing..."):
            # 1. Extract text
            raw_text = get_pdf_text(uploaded_file)

            # 2. Get AI Explanation
            summary = get_gemini_response(raw_text)

            # 3. Display Result
            st.subheader("Legal Explanation:")

            st.write(summary)
