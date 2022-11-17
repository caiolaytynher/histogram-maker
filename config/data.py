from dataclasses import dataclass
from pathlib import Path


@dataclass
class Data:
    file: Path
    column: str
    data: int
    bins: int
    imgname: str