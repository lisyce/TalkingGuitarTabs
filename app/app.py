from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_wtf import FlaskForm, CSRFProtect
from jinja2 import Environment, PackageLoader, select_autoescape
import os

app = Flask(__name__)

# Set the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

class Song:
    def __init__(self, title, description, bars):
        self.title = title
        self.description = description
        self.bars = bars

class Bar:
    def __init__(self, time_signature, key, notes):
        self.time_signature = time_signature
        self.key = key
        self.notes = notes

class Note:
    def __init__(self, duration, string, fret):
        self.duration = duration
        self.string = string
        self.fret = fret

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'xml'}

@app.route('/', methods=['GET', 'POST'])
def home():
    file = None

    if request.method == 'POST':
        # Check if a file is part of the request
        if 'file' in request.files:
            file = request.files['file']

            # If a file was submitted and is valid
            if file and allowed_file(file.filename):
                # Save the file to the configured upload folder
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)
                
                # You could also pass the file name to the template if you want to display it
                file = filename  # or file.filename if you want to display just the name

                parsed_output = parse_file(filename)

                return redirect(url_for('guitar_tab_display', input=parsed_output))

    # Pass the file (or None if no file uploaded) to the template
    return render_template("home.html")

@app.route('/guitar_tab_display')
def guitar_tab_display():
    parsed_output = request.args.get('input')  # Get it from the query string
    return render_template("guitar_tab_template.html", title=parsed_output, description="Some description", bars=[])

def parse_file(filename):
    return "Parsed Output"  # Just a placeholder for now

if __name__ == "__main__":
    # Make folder for file uploads
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    app.run(debug=True)
