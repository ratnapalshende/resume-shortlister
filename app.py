import streamlit as st
import pandas as pd
import preprocessor

# Function to create the UI components
def create_ui():
    st.title("Resume Shortlister")
    resumes = st.file_uploader("Choose PDF files", accept_multiple_files=True)
    skills = st.text_input("Enter skills and keywords (not job description):")
    return resumes, skills

# Function to perform the shortlisting operation
def perform_shortlisting(resumes, skills):
    score_list = []
    progress_text = "Shortlisting is in progress..Please Wait!"
    my_bar = st.progress(0, text=progress_text)

    for i, resume in enumerate(resumes):
        resume_keywords = preprocessor.read_pdf(resume.read())
        resume_score = preprocessor.get_score(skills, resume_keywords)
        score_list.append((resume.name, resume_score, resume_keywords))
        my_bar.progress((i + 1) / len(resumes), text=progress_text)

    my_bar.progress(100, text="Done!")
    return score_list

# Function to display the results
def display_results(score_list):
    if score_list:
        score_list.sort(key=lambda x: x[1], reverse=True)
        df = pd.DataFrame(score_list, columns=["Filename", "Score", "Resume Text"])
        st.bar_chart(df, x="Filename", y="Score", use_container_width=True)
        st.write(df)

# Main function to orchestrate the workflow
def main():
    resumes, skills = create_ui()
    if skills and resumes:
        score_list = perform_shortlisting(resumes, skills)
        display_results(score_list)

if __name__ == "__main__":
    main()
