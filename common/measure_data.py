from typing import List

class MeasureData():
  def __init__(self, time_signature: str, key_signature: str, note_descs: List[str]) -> None:
    self.time_signature: str = time_signature
    self.key_signature: str = key_signature