# TalkingGuitarTabs

## About

Talking Guitar Tabs, based off of the [Talking Scores Project](https://www.marchantpeter.co.uk/talking-sheet-music.php), is an accessible format converter from `.musicXML` to a screen reader-friendly HTML output. This project is designed for blind and low-vision musicians, or for anyone who would benefit from an alternative format for guitar tabs.

There are a variety of features that could be added to our project to make it more robust, convey more of the information found in guitar tabs, and increase accessibility. There is a variety of musical notation that is important to support in order to increase parity with the original guitar tabs. This includes structural elements like repeats, note and rhythm details like ties and articulations, and guitar specific notation like hammer-ons and pull-offs.

Additionally, there are some features that the original Talking Scores project has that blind and low-vision individuals have said are beneficial to them. This includes the ability to play the midi representation of selected measures so users can listen to the score that the text represents.

We hope to see continued improvement in accessibility for music scores so that everyone can enjoy playing music.

## Setup

From within `src/`:

1. Create virtual env: `python -m venv .venv`
1. Activate virtual env:
    1. MacOS/Linux: `source .venv/bin/activate`
    1. On Windows: `.venv/Scripts/activate`
1. Install requirements: `pip install -r requirements.txt`
1. Run: `python app.py`