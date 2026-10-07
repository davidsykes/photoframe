from dataclasses import dataclass


@dataclass(frozen=True)
class PhotoSetConfiguration:
    include_in_sets: bool
    filter: str