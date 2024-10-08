# Resume Shortlister Based on Skills and Keywords

A web application that helps in shortlisting resumes based on specific skills and keywords. This tool allows users to upload multiple resumes, enter required skills, and filter resumes according to a chosen score criterion.

## Features

- **Upload Multiple Resumes**: Easily upload multiple PDF resumes at once.
- **Enter Skills and Keywords**: Specify the skills and keywords you are looking for in the resumes.
- **Shortlisting Criteria**: Use a slider to select the minimum score for shortlisting resumes.
- **Download Selected Resumes**: After shortlisting, download the selected resumes as a ZIP file.

## How to Use

- Step 1 : Click on "Choose PDF files" to upload the resumes you want to shortlist.
- Step 2 : In the text box provided, type the skills and keywords you're looking for.
- Step 3 : Use the slider to choose the minimum score for shortlisting resumes.
- Step 4 : Press the "Start Shortlisting" button to begin the process.
- Step 5 : After the shortlisting is complete, download the selected resumes.

## Live Demo

Check out the live version of the app on Streamlit: [Resume Shortlister Live](https://resumeshortlister.streamlit.app/)
### Glimpses see here:
<img src="https://github.com/user-attachments/assets/8d8cbc4d-f87c-46ba-a656-064545a6c5d5" width=800 height=500 />
<img src ="https://github.com/user-attachments/assets/2fccef1a-0dbf-4795-8774-b518aff535fa" width=800 height=500 />
<img src ="https://github.com/user-attachments/assets/6b0f8eed-1360-4636-bb50-595b30193284" width=800 height=500 />

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/ratnapalshende/resume-shortlister.git
   ```

2. Navigate to the project directory:

   ```bash
   cd resume-shortlister
   ```

3. Install the required dependencies:
   > To use this tika library, you need to have Java 7+ installed on your system as tika-python starts up the Tika REST server in the background.
     Visit [Here](https://github.com/chrismattmann/tika-python) for tika installation.
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

5. Open your web browser and go to `http://localhost:8501`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
