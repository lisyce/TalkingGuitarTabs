import music21

from converter.tab_converter import tab_converter_parse

def main():
    score = tab_converter_parse("example_scores/Dance_of_the_Moonlight_Jellies.musicxml")
    for x in score.flatten().notes:
        if isinstance(x, music21.chord.Chord):
            print(x.duration.fullName, [(n.pitch.name, n.string, n.fret) for n in x.notes])   
        else:
            print(x.duration.fullName, [(x.pitch.name, x.string, x.fret)])
         

if __name__=="__main__":
    main()