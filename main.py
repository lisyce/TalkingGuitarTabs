import music21

from tab_converter.tab_converter import tab_converter_parse

def main():
    score = tab_converter_parse("example_scores/fearless.xml")
    for x in score.flatten().notes:
        print(x.duration.fullName, [p.name for p in x.pitches])    

if __name__=="__main__":
    main()