from typing import List

from music21.stream import Score, Part, Measure
from music21 import meter, clef, note, chord

from common.measure_data import MeasureData
from common.tablature_note import TablatureNote


def tab_part(score: Score) -> Part:
    for part in score.parts:
        for m in part.measures(0, None):  # for some reason the first measure might not have it; check until we find one
            measure_clef = m.getContextByClass(clef.Clef)
            if type(measure_clef) == clef.TabClef:
                return part
    
    raise Exception("tablature part not found in score")

def measure_data(part: Part) -> List[MeasureData]:
    result = []
    
    curr_key = None
    curr_time = None
    for m in part.measures(0, None):
        if type(m) != Measure:  # not sure why this is a thing but we need it
            continue
        
        if m.keySignature is not None:
            curr_key = m.keySignature._strDescription()
        if m.timeSignature is not None:
            curr_time = m.timeSignature.ratioString
        
        descs = [_note_and_rest_to_str(nr) for nr in m.flatten().notesAndRests]
        result.append(MeasureData(curr_time, curr_key, descs))
        
    return result

        
def _note_and_rest_to_str(nr: note.GeneralNote) -> str:
    if type(nr) == TablatureNote:
        return f"{nr.duration.fullName} string {nr.string} fret {nr.fret}"
    elif type(nr) == chord.Chord:
        notes_str = ", ".join([_note_and_rest_to_str(n) for n in nr.notes])
        return f"{len(nr.notes)}-note chord: {notes_str}"
    elif type(nr) == note.Rest:
        return f"{nr.duration.fullName} rest"
    else:
        raise Exception("unknown element type in measure")