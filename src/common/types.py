from typing import TypedDict, List
from music21.note import Note

class TablatureNote(Note):
    def __init__(self, simple_note: Note, string: int | None, fret: int | None):
        super().__init__(**simple_note.__dict__)
        self.duration = simple_note.duration
        self.string = string
        self.fret = fret

Bar = TypedDict('Bar', {
    'time_signature': str,
    'key': str,
    'tempo': str,
    'notes': List[str],
})

Song = TypedDict('Song', {
    'title': str,
    'composers': str,
    'description': str,
    'bars': List[Bar]
})
