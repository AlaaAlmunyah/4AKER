# PDF and Audio Processing Web Application

## Overview
This project is a web application built using Flask that integrates file upload functionality and audio recording capabilities. The application allows users to upload PDF files, extract text from them, and record audio. It leverages various libraries and technologies such as PyPDF2 for PDF text extraction, PyAudio for audio recording, and OpenAI's API for additional processing.

## Features
- **File Upload:** Upload PDF files and extract text from them.
- **Audio Recording:** Record audio and save it as a WAV file.
- **Text Extraction:** Extract text from PDF files using PyPDF2.
- **Audio Processing:** Record audio using PyAudio with placeholders for advanced processing.

## Technologies and Libraries
- **Flask:** A micro web framework for Python.
- **Flask-WTF and WTForms:** For creating and validating web forms.
- **PyPDF2:** For reading and extracting text from PDF files.
- **PyAudio:** For recording and processing audio data.
- **OpenAI API:** For advanced processing (e.g., language models).
- **Scikit-learn:** For text processing and similarity calculations.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- Flask-WTF
- WTForms
- PyPDF2
- PyAudio
- OpenAI
- Scikit-learn

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage
1. **Run the Flask Application:**
    ```sh
    python pdf.py
    ```
   Open your web browser and navigate to `http://localhost:5000` to access the file upload form.

2. **Upload a PDF File:**
   - Use the provided form to upload a PDF file.
   - The application will extract text from the uploaded PDF and save it to a file in the specified upload folder.

3. **Record Audio:**
   - Execute the audio recording functionality:
     ```sh
     python app.py
     ```
   - This will record audio for the specified duration and save it as a WAV file.

## Project Structure
```
|-- pdf.py                 # Handles PDF file uploads and text extraction
|-- app.py                 # Handles audio recording and processing
|-- templates/             # HTML templates for the Flask application
    |-- upload.html        # Upload form template
|-- static/                # Static files (CSS, JS, images)
|-- requirements.txt       # List of required Python packages
|-- README.md              # Project overview and setup instructions
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgements
- Flask
- Flask-WTF
- WTForms
- PyPDF2
- PyAudio
- OpenAI
- Scikit-learn
