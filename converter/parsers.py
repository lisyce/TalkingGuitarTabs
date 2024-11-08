import typing as t
import warnings

from music21.note import Note, Unpitched, Rest
from music21.stream.base import Measure
from music21.musicxml.xmlObjects import MusicXMLImportException, MusicXMLWarning
from music21.musicxml import xmlToM21

from xml.etree.ElementTree import Element

from common.tablature_note import TablatureNote

class TablaturePartParser(xmlToM21.PartParser):
    def __init__(self, mxPart: Element | None = None, mxScorePart: Element | None = None, parent: xmlToM21.MusicXMLImporter | None = None):
        super().__init__(mxPart, mxScorePart, parent)
    
    def xmlMeasureToMeasure(self, mxMeasure: Element) -> Measure:
        measureParser = TablatureMeasureParser(mxMeasure, parent=self)
        
        # below code taken from music21.musicxml.xmlToM21 PartParser.xmlMeasureToMeasure
        try:
            measureParser.parse()
        except MusicXMLImportException as e:
            e.measureNumber = str(measureParser.measureNumber)
            e.partName = self.stream.partName
            raise e
        except Exception as e:
            warnings.warn(
                f'The following exception took place in m. {measureParser.measureNumber} in '
                + f'part {self.stream.partName}.',
                MusicXMLWarning
            )
            raise e

        self.lastMeasureParser = measureParser

        self.maxStaves = max(self.maxStaves, measureParser.staves)

        if measureParser.transposition is not None:
            self.updateTransposition(measureParser.transposition)

        self.firstMeasureParsed = True
        self.staffReferenceList.append(measureParser.staffReference)

        m = measureParser.stream
        self.setLastMeasureInfo(m)
        if measureParser.fullMeasureRest is True:
            # recurse is necessary because it could be in voices
            r1 = m[Rest].first()

            if t.TYPE_CHECKING:
                # fullMeasureRest is True, means Rest will be found
                assert r1 is not None

            if self.lastTimeSignature is not None:
                lastTSQl = self.lastTimeSignature.barDuration.quarterLength
            else:
                lastTSQl = 4.0  # sensible default.

            if (r1.fullMeasure is True  # set by xml measure='yes'
                or (r1.duration.quarterLength != lastTSQl
                    and r1.duration.type in ('whole', 'breve')
                    and r1.duration.dots == 0
                    and not r1.duration.tuplets)):
                r1.duration.quarterLength = lastTSQl
                r1.fullMeasure = True

        # NB: not coreInsert, because barDurationProportion()
        # is called in adjustTimeAttributesFromMeasure()
        self.stream.insert(self.lastMeasureOffset, m)
        self.adjustTimeAttributesFromMeasure(m)

        return m

class TablatureMeasureParser(xmlToM21.MeasureParser):
    def __init__(self, mxMeasure: Element | None = None, parent: xmlToM21.PartParser | None = None):
        super().__init__(mxMeasure, parent)
     
    # TODO use the super() output and additionally add tabulature data
    def xmlToSimpleNote(self, mxNote, freeSpanners=True) -> TablatureNote | Unpitched:
        simple =  super().xmlToSimpleNote(mxNote, freeSpanners)
        if isinstance(simple, Note):
            return TablatureNote(simple)
        
        return simple