from music21.stream import Score

from .converters import TabulatureConverterMusicXML

def tab_converter_parse(file_path: str) -> Score:
    c = TabulatureConverterMusicXML()
    
    # parse file
    content = None
    with open(file_path) as f:
        content = f.read()
    
    c.parseData(content)
    return c.stream
