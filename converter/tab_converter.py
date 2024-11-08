from music21.stream import Score

from .converters import TablatureConverterMusicXML

def tab_converter_parse(file_path: str) -> Score:
    c = TablatureConverterMusicXML()
    
    # parse file
    content = None
    with open(file_path) as f:
        content = f.read()
    
    c.parseData(content)
    return c.stream
