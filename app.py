import streamlit as st
import preprocessor

resumes = st.file_uploader("Choose pdf files",accept_multiple_files=True)
score_list = []
skills = "C, Python, Java, Git, Github, Django 45 Machine learning, Shell scripting, Linux, Networking, Operating System, HTML, CSS"

progress_text = "Shortlisting is in progress..Please Wait!"
if resumes:
    my_bar = st.progress(0, text=progress_text)
else:
    my_bar = None

i=0
for resume in resumes:
    bytes_data = resume.read()
    resume_keywords = preprocessor.read_pdf(bytes_data)
    resume_score = preprocessor.get_score(skills, resume_keywords)
    my_bar.progress((i+1)/len(resumes), text=progress_text)

    score_list.append((resume.name, resume_score))
    i+=1
if my_bar:
    my_bar.progress(100, text="Done!")
        

st.write(score_list)
