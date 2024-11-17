from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_wtf import FlaskForm, CSRFProtect
from jinja2 import Environment, PackageLoader, select_autoescape
import os

app = Flask(__name__)

# Set the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

# If you want to customize Jinja2 settings in Flask, you can do so here
env = Environment(
    loader=PackageLoader("app"),  # Your package or template folder
    autoescape=select_autoescape([".musicxml"])  # Enable auto-escaping
)

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

                parsed_output = parse_file(filename)

                return redirect(url_for('guitar_tab_display', input=parsed_output))

    # Pass the file (or None if no file uploaded) to the template
    return render_template("home.html")


def parse_file(filename):
    # sample data
    music_data = {
        'title': 'Sample Song Title',
        'description': 'A short sample piece for testing.',
        'bars': [
            {
                'time_signature': '4/4',
                'key': 'C Major',
                'notes': [
                    ('Quarter Note', 6, 3),  # String 6, Fret 3 (G note)
                    ('Eighth Note', 5, 2),   # String 5, Fret 2 (B note)
                    ('Eighth Note', 4, 0),   # String 4, Fret 0 (D note)
                    ('Quarter Note', 3, 0),  # String 3, Fret 0 (G note)
                    ('Eighth Note', 2, 1)    # String 2, Fret 1 (C note)
                ]
            },
            {
                'time_signature': '4/4',
                'key': 'C Major',
                'notes': [
                    ('Quarter Note', 4, 3),  # String 4, Fret 3 (F note)
                    ('Quarter Note', 5, 0),  # String 5, Fret 0 (A note)
                    ('Eighth Note', 6, 1),   # String 6, Fret 1 (F note)
                    ('Eighth Note', 3, 2),   # String 3, Fret 2 (A note)
                    ('Quarter Note', 2, 0)   # String 2, Fret 0 (B note)
                ]
            }
        ]
    }

    return music_data

@app.route('/guitar_tab_display')
def guitar_tab_display(input):
    parsed_output = request.args.get('input')  # Get it from the query string
    return render_template("guitar_tab_template.html", title=parsed_output.title, description=parsed_output.description, bars=parsed_output.bars)


if __name__ == "__main__":
    # Make folder for file uploads
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    app.run(debug=True)
