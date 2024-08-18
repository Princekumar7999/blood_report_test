import streamlit as st
from PyPDF2 import PdfReader
import io
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def analyze_blood_test(blood_test_data):
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

    response = model.generate_content(prompt)
    return response.text

st.title('Blood Test Analyzer')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    try:
        st.write("Analyzing your blood test report...")
        
        
        pdf_content = extract_text_from_pdf(uploaded_file)
        
       
        result = analyze_blood_test(pdf_content)
        
        st.write("Analysis complete!")
        st.write(result)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")