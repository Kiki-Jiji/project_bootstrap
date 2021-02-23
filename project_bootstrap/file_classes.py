from dataclasses import dataclass

@dataclass(frozen=True)
class Folder:
    name: str
    files: list = None
    root: bool = True
    path: str = None
    description: str = None

@dataclass(frozen=True)
class File:
    name: str
    contents: str = None
    description: str = None
