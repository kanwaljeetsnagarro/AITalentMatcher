#Field to put in the JD

#Upload PDF file
#Convert PDF to Image format --> processing --> Google Gemini Pro
#Prompts Template [Multiple Prompts]
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import streamlit as st
import os   
import io
from PIL import Image
import pdf2image
from pdf2image import convert_from_path
import base64
import google.generativeai as genai
from pathlib import Path
#from llama_index.core import download_loader
from getpass import getpass

pinecone_api_key = os.getenv("PINECONE_API_KEY") #or getpass("e09705a3-6968-4df0-8894-408525347c9d")
openai_api_key = os.getenv("OPENAI_API_KEY") #or getpass("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")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Download and instantiate `PDFReader` from LlamaHub
#PDFReader = download_loader("PDFReader")
#loader = PDFReader()
# Load HNSW PDF from LFS
#documents = loader.load_data(file=Path('Data/Assignment Support Document.pdf'))
# Preview one of our documents
#documents[0]

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel(model_name="gemini-1.5-flash")
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ##Convert the pdf file to image format
       # images = pdf2image.convert_from_bytes(uploaded_file.read())
        images = pdf2image.convert_from_bytes(uploaded_file.read(),poppler_path=r"C:\OneDrive\OneDrive - Nagarro\LEARNING\poppler-24.08.0\Library\bin")
        
        first_page = images[0]

        #Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format = 'JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
            "mime_type":"image/jpeg",
            "data":base64.b64encode(img_byte_arr).decode() #encode to base64
            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError("Invalid file format. Please upload a PDF file.")  

#Streamlit App

st.set_page_config(page_title="ATS Resume Expert")
st.header("AI Resume Matcher")
input_text=st.text_area("Job Description: ", key="input")
uploaded_file=st.file_uploader("Upload your resume in PDF format",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell me about the resume")

submit2 = st.button("How can the skills be improved?")

submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced HR with Tech experience in the field of Data Science, Full Stack Web development, Big Data Engineering, DevOps, Data Analyst, your task is to be able to review the provided resume against the job description for these profiles.

Please share your professional evaluation on whether the candidate profile aligns with the job description and highlight the strengths and weaknesses of the applicant in relation to the specified job description"""

input_prompt2 = """
You are an experienced HR with Tech experience in the field of Data Science, Full Stack Web development, Big Data Engineering, DevOps, Data Analyst, your task is to be able to review the improvement areas for the resume against the job description
Please share your professional evaluation on what improvements are required in the candidate profile when aligned qwith the job description and highlight the strengths and weaknesses of the applicant in relation to the specified job description"""

input_prompt3 = """
You are a skilled ATS (Application Tracking System) scanner with a deep understanding of Data Science, Full Stack Web development, Big Data Engineering, DevOps, Data Analyst and deep ATS functionality

your task is to be to review the provided resume against the job description for these profiles. give me the percentage match in the heading format if the resume matches the job description. First the output of the matching should come as percentage and then the keywords missing and final thoughts; try to be consistent with the score always"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The response is: ")
        st.write(response)
    else:
        st.write("Please upload a resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The response is: ")
        st.write(response)
    else:
        st.write("Please upload a resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The response is: ")
        st.write(response)
    else:
        st.write("Please upload a resume")