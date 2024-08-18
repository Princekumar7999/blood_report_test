import streamlit as st
from PyPDF2 import PdfReader
import io
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Attempt to import google.generativeai
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# Configure Gemini API if available
if GEMINI_AVAILABLE:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def analyze_blood_test(blood_test_data):
    if not GEMINI_AVAILABLE:
        return "Gemini API is not available. Please check your configuration."

    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Analyze the following blood test report and provide health recommendations:

    {blood_test_data}

    Please provide:
    1. A summary of the blood test results
    2. Any notable findings or abnormalities
    3. General health recommendations based on these results
    4. Suggestions for further tests or consultations if necessary
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while analyzing the blood test: {str(e)}"

st.title('Blood Test Analyzer')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    try:
        st.write("Analyzing your blood test report...")
        
        # Read PDF content
        pdf_content = extract_text_from_pdf(uploaded_file)
        
        # Analyze the blood test using Gemini
        result = analyze_blood_test(pdf_content)
        
        st.write("Analysis complete!")
        st.write(result)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Add a note about Gemini API availability
if not GEMINI_AVAILABLE:
    st.warning("Note: Gemini API is not available. Some features may be limited.")