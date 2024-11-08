from music21.note import Note

class TablatureNote(Note):
    # TODO tabulature init
    def __init__(self, simple_note: Note, **keywords):
        super().__init__(simple_note.pitch, name=simple_note.name, nameWithOctave=simple_note.nameWithOctave, **keywords)
        