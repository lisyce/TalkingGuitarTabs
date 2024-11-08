from music21.note import Note

class TablatureNote(Note):
    def __init__(self, simple_note: Note, string: int | None, fret: int | None):
        super().__init__(**simple_note.__dict__)
        self.duration = simple_note.duration
        self.string = string
        self.fret = fret