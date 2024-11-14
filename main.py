import music21

from converter.tab_converter import tab_converter_parse
from needs_named import tab_part, measure_data

def main():
    score = tab_converter_parse("example_scores/Andante.musicxml")
    tabs = tab_part(score)
    
    measure_data(tabs)
    
    # for x in score.measures(1, 4):
    #     print(x)
        # if isinstance(x, music21.chord.Chord):
        #     print(x.duration.fullName, [(n.pitch.name, n.string, n.fret) for n in x.notes])   
        # else:
        #     print(x.duration.fullName, [(x.pitch.name, x.string, x.fret)])
         

if __name__=="__main__":
    main()