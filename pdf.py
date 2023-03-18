from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from PyPDF2 import PdfReader

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'D:\hackathon'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return '\n'.join(text)

def write_text_to_file(text, file_name):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    with open(file_path, 'w') as f:
        f.write(text)
    return file_path

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file_name = secure_filename(file.filename.replace('.pdf', '.txt'))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(file_path)
        text = extract_text_from_pdf(file_path)
        text_file_path = write_text_to_file(text, file_name)
    return render_template('./templates/upload.html')

if __name__ == '__main__':
    app.run(debug=True)