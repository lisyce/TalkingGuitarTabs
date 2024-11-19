import os
import json

from flask import Flask, render_template, redirect, url_for, request, session, jsonify

from converter.tab_converter import tab_converter_parse
from score_reader import song_data
from common.types import Song

app = Flask(__name__)

# Set the secret key for session to work (make sure to keep this secret)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Set the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

# Allowed file extension check
def allowed_file(filename):
    return filename.endswith('.musicxml')
    # return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'xml'}

# Song and Bar class definitions (no changes)

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

# Home route to upload the file
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if a file is part of the request
        if 'file' in request.files:
            file = request.files['file']
            
            # If a file was submitted and is valid
            if file and allowed_file(file.filename):
                # Save the file to the configured upload folder
                filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filename)

                # Parse the uploaded file
                parsed_output = parse_file(filename)

                # Store the parsed output in session
                session['parsed_output'] = json.dumps(parsed_output, default=str)  # Use json.dumps to store non-primitive types in session

                # Redirect to guitar_tab_display route
                return redirect(url_for('guitar_tab_display'))

    # Render home page
    return render_template("home.html")

# Guitar tab display route (display parsed data)
@app.route('/guitar_tab_display',  methods=['GET'])
def guitar_tab_display():
    # Retrieve the parsed output from session
    # parsed_output = {
    #     'title': 'Sample Song Title',
    #     'description': 'A short sample piece for testing.',
    #     'bars': [
    #         {
    #             'time_signature': '4/4',
    #             'key': 'C Major',
    #             'notes': [
    #                 'Quarter Note, 6, 3',
    #                 'Eighth Note, 5, 2',
    #                 'Eighth Note, 4, 0',
    #                 'Quarter Note, 3, 0',
    #                 'Eighth Note, 2, 1'
    #             ]
    #         },
    #         {
    #             'time_signature': '4/4',
    #             'key': 'C Major',
    #             'notes': [
    #                 'Quarter Note, 4, 3',
    #                 'Quarter Note, 5, 0',
    #                 'Eighth Note, 6, 1',
    #                 'Eighth Note, 3, 2',
    #                 'Quarter Note, 2, 0'
    #             ]
    #         }
    #     ]
    # }
    
    parsed_output: Song = json.loads(session['parsed_output'])

    return render_template("guitar_tab_template.html", title=parsed_output['title'], description=parsed_output['description'],
                           bars=parsed_output['bars'], composer=parsed_output["composers"])


# Parse the uploaded file (stubbed with sample data)
def parse_file(filename) -> Song:   
    score = tab_converter_parse(filename)
    return song_data(score)

if __name__ == "__main__":
    # Make folder for file uploads if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # TODO: use temp dirs if python supports it?

    app.run(debug=True)
