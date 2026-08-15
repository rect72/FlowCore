from dataclasses import dataclass


@dataclass
class Organization:
    id: int | None
    name: str