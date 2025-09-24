import sys
from dataclasses import dataclass
from datetime import date



@dataclass
class Club:
    id: int
    name: str
    abbr: str

    def get_venues(self):
        return f"{Venue.clubid()}"

@dataclass
class Venue:
    id: int
    clubid: str
    name: str
    address: str 




class Game():
     def __init__(self, id:int, date: date, gamevenue: Venue):
         pass