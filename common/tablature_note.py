from music21.note import Note

class TablatureNote(Note):
    def __init__(self, simple_note: Note, string: int, fret: int):
        super().__init__(**simple_note.__dict__)
        self.duration = simple_note.duration
        self.string = string
        self.fret = fret