from music21.converter.subConverters import ConverterMusicXML
from music21.musicxml import xmlToM21

from .parsers import TablaturePartParser


class TablatureConverterMusicXML(ConverterMusicXML):
    def __init__(self, **keywords) -> None:
        super().__init__(**keywords)
    
    def parseData(self, xmlString: str, number=None):
        c = TablatureMusicXMLImporter()
        c.xmlText = xmlString
        c.parseXMLText()
        self.stream = c.stream


class TablatureMusicXMLImporter(xmlToM21.MusicXMLImporter):
    def __init__(self):
        super().__init__()
    
    def xmlPartToPart(self, mxPart, mxScorePart):
        parser = TablaturePartParser(mxPart, mxScorePart=mxScorePart, parent=self)
        parser.parse()
        if parser.appendToScoreAfterParse is True:
            return parser.stream
        else:
            return None
