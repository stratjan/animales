from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
import uuid


class Animal(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    animal_id: str
    name: str
    continent: str
    image_url: str
    sound_urls: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "animal_id": "af-1",
                "name": "Elefante",
                "continent": "africa",
                "image_url": "https://...",
                "sound_urls": [
                    "https://soundbible.com/mp3/elephant1.mp3",
                    "https://soundbible.com/mp3/elephant2.mp3"
                ]
            }
        }


class AnimalResponse(BaseModel):
    id: str
    name: str
    image: str
    sounds: List[str]


class ContinentInfo(BaseModel):
    id: str
    name: str


class AnimalsDataResponse(BaseModel):
    continents: List[ContinentInfo]
    animals: dict
