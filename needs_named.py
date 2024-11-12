from music21.stream import Score, Part, Measure
from music21 import meter, clef, note, chord

from common.tablature_note import TablatureNote

# 1. get the part with the TAB clef
# 2. get all measures
# 3. get time sig ("6 8"), key sig ("2 flats")
# 4. get note info ("quarter string 3 fret 2", "quarter 2-note chord: string 3 fret 2, string 2 open")

def tab_part(score: Score) -> Part:
    for part in score.parts:
        for m in part.measures(0, None):  # for some reason the first measure might not have it; check until we find one
            measure_clef = m.getContextByClass(clef.Clef)
            if type(measure_clef) == clef.TabClef:
                return part
    
    raise Exception("tablature part not found in score")

def measure_data(part: Part):
    curr_key = None
    curr_time = None
    for m in part.measures(0, None):
        if type(m) != Measure:  # not sure why this is a thing but we need it
            continue
        
        if m.keySignature is not None:
            curr_key = m.keySignature._strDescription()
        if m.timeSignature is not None:
            curr_time = m.timeSignature.ratioString
            
        for nr in m.flatten().notesAndRests:
            print(_note_and_rest_to_str(nr))
        break
        
def _note_and_rest_to_str(nr: note.GeneralNote) -> str:
    if type(nr) == TablatureNote:
        pass
    elif type(nr) == chord.Chord:
        pass
    elif type(nr) == note.Rest:
        pass
    else:
        raise Exception("unknown element type in measure")