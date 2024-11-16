# from flask import Flask, render_template, redirect, url_for, request, jsonify
# from flask_wtf import FlaskForm, CSRFProtect
# from jinja2 import Environment, PackageLoader, select_autoescape
# import os

# app = Flask(__name__)

# # Set the upload folder
# app.config['UPLOAD_FOLDER'] = 'uploads'

# # If you want to customize Jinja2 settings in Flask, you can do so here
# env = Environment(
#     loader=PackageLoader("app"),  # Your package or template folder
#     autoescape=select_autoescape(["html", "xml"])  # Enable auto-escaping
# )

# class Song:
#     def __init__(self, title, description, bars):
#         self.title = title
#         self.description = description
#         self.bars = bars

# class Bar:
#     def __init__(self, time_signature, key, notes):
#         self.time_signature = time_signature
#         self.key = key
#         self.notes = notes

# class Note:
#     def __init__(self, duration, string, fret):
#         self.duration = duration
#         self.string = string
#         self.fret = fret

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'xml'}

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     file = None

#     if request.method == 'POST':
#         # Check if a file is part of the request
#         if 'file' in request.files:
#             file = request.files['file']

#             # If a file was submitted and is valid
#             if file and allowed_file(file.filename):
#                 # Save the file to the configured upload folder
#                 filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#                 file.save(filename)
                
#                 # You could also pass the file name to the template if you want to display it
#                 file = filename  # or file.filename if you want to display just the name

#                 parsed_output = parse_file(filename)

#                 return redirect(url_for('guitar_tab_display', input=parsed_output))

#     # Pass the file (or None if no file uploaded) to the template
#     return render_template("home.html")

# @app.route('/guitar_tab_display')
# def guitar_tab_display():
#     parsed_output = request.args.get('input')  # Get it from the query string
#     return render_template("guitar_tab_template.html", title=parsed_output, description="Some description", bars=[])

# def parse_file(filename):
#     return "Parsed Output"  # Just a placeholder for now

# if __name__ == "__main__":
#     # Make folder for file uploads
#     os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

#     app.run(debug=True)

from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from flask_wtf import FlaskForm, CSRFProtect
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)

# Set the upload folder and allowed file extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'xml'}
app.config['SECRET_KEY'] = 'your_secret_key_here'  # for CSRF protection

csrf = CSRFProtect(app)  # Enable CSRF protection

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
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            parsed_output = parse_file(filepath)

            # Serialize parsed data (if it's a complex object) or just pass as needed
            parsed_output_json = json.dumps(parsed_output)  # Example of serialization
            return redirect(url_for('guitar_tab_display', parsed_output=parsed_output_json))

    return render_template("home.html")

@app.route('/guitar_tab_display')
def guitar_tab_display():
    # Retrieve and deserialize parsed_output from query args
    parsed_output_json = request.args.get('parsed_output')
    if parsed_output_json:
        parsed_output = json.loads(parsed_output_json)
    else:
        parsed_output = None
    
    # In your template, you will need to render title, description, and bars from parsed_output
    return render_template("guitar_tab_template.html", parsed_output=parsed_output)

def parse_file(filename):
    # Implement the actual file parsing logic here (e.g., XML parsing)
    # For demonstration, return a mock Song object
    song = Song(
        title="Sample Song",
        description="A great song",
        bars=[
            Bar(time_signature="4/4", key="C", notes=[Note(1, 6, 3), Note(1, 5, 2)]),
            Bar(time_signature="4/4", key="G", notes=[Note(0.5, 4, 3), Note(0.5, 3, 5)])
        ]
    )
    return song  # Return a Song object (or dictionary)

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
