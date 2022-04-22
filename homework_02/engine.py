"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass()
class Engine:
    volume: float = 2
    pistons: int = 3

