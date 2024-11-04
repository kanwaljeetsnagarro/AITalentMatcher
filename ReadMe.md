# AI Resume Matching, Analysis, and Chat

This project is a Streamlit web application for automated resume processing using AI. It provides functionalities for resume filtering, analysis, and a chat interface for Q&A with the resume. The app uses NLP models to match resumes with job descriptions, extract key details, and interact with resumes through conversational prompts.

## Features
1. **Resume Filter** - Upload multiple resumes, input a job description, and get a similarity score to identify the top-matching resumes.
2. **Resume Analysis** - Upload a resume for summary and extraction of key details like skills, experience, and education.
3. **Resume Chat** - Chat-based interface where users can ask questions about a resume, and the AI provides answers.

## Technologies Used
- **Streamlit**: Web application framework for the UI.
- **Google Gemini API**: For generating content responses.
- **Sentence Transformers**: NLP model for sentence embedding and similarity comparison.
- **pdfplumber**: To extract text from PDF resumes.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/AI-Resume-Matching.git
   cd AI-Resume-Matching

2. Install the required packages:
   pip install -r requirements.txt

3. Configure Google Gemini API:
   Set up a Google Gemini API key and store it in an environment variable GOOGLE_API_KEY

 ## Usage
 
1. Run the Streamlit application:

   ```bash
   streamlit run app.py

2. Select Activity: Choose from "Resume Filter," "Resume Analysis," or "Resume Chat" on the sidebar.

- **Resume Filter**: Upload resumes and provide a job description to see top matching resumes based on similarity scores.
- **Resume Analysis**: Upload a resume to get a summary and key information such as skills, experience, and education.
- **Resume Chat**: Upload a resume and ask questions to receive AI-generated answers based on the resume content.

## Project Structure

- **app.py**: Main application code.
- **requirements.txt**: Python dependencies required for the project.
- **README.md**: Project documentation.


## Acknowledgments

- **Streamlit** for the web framework.
- **pdfplumber** for PDF text extraction.
- **Sentence Transformers** for NLP models.
- **Google Gemini** for generative content support.
