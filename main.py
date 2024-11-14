import music21

from converter.tab_converter import tab_converter_parse
from score_reader import tab_part, measure_data

def main():
    score = tab_converter_parse("example_scores/Andante.musicxml")
    tabs = tab_part(score)
    
    data = measure_data(tabs)
    
         

if __name__=="__main__":
    main()