from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()


class FunnyAnimal(Base):
    __tablename__ = 'funny_animals'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # The animal's name (e.g., "Grumpy Cat")
    mood = Column(String, nullable=False)  # Mood (e.g., "Grumpy", "Happy", "Confused")
    quirkiness_level = Column(Float, default=1.0)  # Level of quirkiness (1.0 to 10.0)
    sighting_timestamp = Column(DateTime, default=datetime.now(timezone.utc))  # When the animal was last spotted
    # ------- To enable the migration check test, uncomment the column below ------
    favorite_food = Column(String)  # Favorite food (e.g., "Pickles")

    def __repr__(self):
        return (
            f"<FunnyAnimal(id={self.id}, name='{self.name}', mood='{self.mood}', "
            f"quirkiness_level={self.quirkiness_level}, favorite_food='{self.favorite_food}', "
            f"sighting_timestamp={self.sighting_timestamp})>"
        )
