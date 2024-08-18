import zipfile
import io
import pandas as pd
import streamlit as st
import preprocessor

# Function to create the UI components
def create_ui():
    """Create the user interface components for the resume shortlisting app."""
    st.title("CV Shortlisting System based on Skills and Keywords")

    # Instructions for users
    st.markdown("""
        **How to Use the Resume Shortlister:**

        1. **Upload Resumes**: Click on "Choose PDF files" to upload the resumes you want to shortlist. You can select multiple files at once.
        2. **Enter Skills**: In the text box provided, type the skills and keywords you're looking for in the resumes.
        3. **Select Criteria**: Use the slider to choose the minimum score for shortlisting resumes.
        4. **Start Shortlisting**: Once you've uploaded the resumes and entered the skills, click on 'start shortlisting' button  the app will start shortlisting.
        5. **Download Resumes**: After shortlisting, download the selected resumes as a zip file.
    """)

    st.subheader("Select Resumes from system")
    uploaded_resumes = st.file_uploader("Choose PDF files", accept_multiple_files=True)

    st.subheader("Enter skills and keywords (not job description)")
    input_skills = st.text_input('Enter here:')

    st.subheader("Select criteria for shortlisting")
    score_criteria = st.slider(
        "Select here:",
        min_value=0,
        max_value=100,
        value=50
    )

    start_shortlisting = st.button("Start Shortlisting")
    return uploaded_resumes, input_skills, score_criteria, start_shortlisting

# Function to perform the shortlisting operation
def perform_shortlisting(resumes, skills):
    """Process the resumes and compute scores based on input skills."""
    score_list = []
    progress_text = "Shortlisting is in progress..Please Wait!"
    progress_bar = st.progress(0, text=progress_text)

    for i, resume in enumerate(resumes):
        resume_keywords = preprocessor.read_pdf(resume.read())
        resume_score = preprocessor.get_score(skills, resume_keywords)
        score_list.append((resume.name, resume_score, resume, resume_keywords))
        progress_bar.progress((i + 1) / len(resumes), text=progress_text)

    progress_bar.progress(100, text="Done!")
    return score_list

# Function to filter resumes based on the score criteria
def filter_resumes(score_list, criteria):
    """Filter resumes based on the minimum score criteria."""
    return [(name, score, file) for name, score, file, _ in score_list if score >= criteria]

# Function to create a zip file for download
def create_zip(filtered_resumes):
    """Create a zip file containing the filtered resumes."""
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        for name, _, file in filtered_resumes:
            zf.writestr(name, file.getbuffer())
    return zip_buffer

# Function to display the results and download option
def display_results(score_list, criteria):
    """Display the shortlisting results and provide a download option."""
    st.header("Results")
    if score_list:
        score_list.sort(key=lambda x: x[1], reverse=True)
        df = pd.DataFrame([(name, score, keywords) for name, score, _, keywords in score_list], 
                          columns=["Filename", "Score", "Resume Text"])
        st.bar_chart(df, x="Filename", y="Score", use_container_width=True)
        st.write(df)

        # Filter resumes based on the selected score criteria
        filtered_resumes = filter_resumes(score_list, criteria)
        
        if filtered_resumes:
            st.markdown(
    f"<p style='color:green;'><b>{len(filtered_resumes)} resumes matched the score of {criteria} or higher.</b></p>",
    unsafe_allow_html=True
)
            # Create a zip file of the filtered resumes
            zip_buffer = create_zip(filtered_resumes)
            st.download_button(
                label="Download Selected Resumes",
                data=zip_buffer.getvalue(),
                file_name="shortlisted_resumes.zip",
                mime="application/zip"
            )
        else:
            st.markdown(f"No resumes matched the score of {criteria} or higher.")


resumes, skills, score_criteria, start_shortlisting = create_ui()
if start_shortlisting and skills and resumes:
    score_list =  perform_shortlisting(resumes, skills)
    display_results(score_list, score_criteria)
