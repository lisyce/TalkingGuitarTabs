from typing import List

from music21.stream import Score, Part, Measure
from music21 import clef, note, chord

from common.types import TablatureNote, Bar, Song


def song_data(score: Score) -> Song:
    title = score.metadata.bestTitle
    composers = ", ".join(score.metadata.composers)
    
    if len(composers.strip()) == 0:
        composers = "No composer information found."
    
    tab_part = _tab_part(score)
    measures = _measure_data(tab_part)
    
    measure_count = len(measures)
    desc = f"There are {measure_count} measures."
    
    return {
        "title": title,
        "composers": composers,
        "description": desc,
        "bars": measures
    }
    
    
def _tab_part(score: Score) -> Part:
    for part in score.parts:
        for m in part.measures(0, None):  # for some reason the first measure might not have it; check until we find one
            measure_clef = m.getContextByClass(clef.Clef)
            if type(measure_clef) == clef.TabClef:
                return part
    
    raise Exception("tablature part not found in score")

def _measure_data(part: Part) -> List[Bar]:
    result = []

    curr_key = None
    curr_time = None
    curr_tempo = None
    for m in part.measures(0, None):
        if type(m) != Measure:  # not sure why this is a thing but we need it
            continue
        
        tempos = m.metronomeMarkBoundaries()
        if tempos:
            t0 = tempos[0][2]
            curr_tempo = f"{t0.referent.fullName} = {t0.number}"
            if t0.text:
                curr_tempo += f" ({t0.text})"
        if m.keySignature is not None:
            curr_key = m.keySignature._strDescription()
        if m.timeSignature is not None:
            curr_time = m.timeSignature.ratioString
        
        notes = [_note_and_rest_to_str(nr) for nr in m.flatten().notesAndRests]
        bar: Bar = {
            'time_signature': curr_time,
            'key': curr_key,
            'tempo': curr_tempo,
            'notes': notes
        }
        result.append(bar)
        
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