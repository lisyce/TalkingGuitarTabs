import music21

from converter.tab_converter import tab_converter_parse
from score_reader import song_data

def main():
    score = tab_converter_parse("../example_scores/BellaCiao.musicxml")
    blah = song_data(score)
    print(blah)

if __name__=="__main__":
    main()