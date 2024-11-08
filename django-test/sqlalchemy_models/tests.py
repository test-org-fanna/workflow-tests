import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from .models import Base, FunnyAnimal


# Use an in-memory SQLite database for tests
@pytest.fixture(scope="function")
def session():
    # Set up the in-memory SQLite database
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)  # Create tables

    # Set up a new session for each test
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # Provide the session to the test

    # Clean up after the test
    session.close()
    Base.metadata.drop_all(engine)


# Test case: Verify creation of a FunnyAnimal instance
def test_create_funny_animal(session):
    animal = FunnyAnimal(
        name="Grumpy Cat",
        mood="Grumpy",
        quirkiness_level=10.0,
        favorite_food="Pickles"
    )
    session.add(animal)
    session.commit()

    # Retrieve the animal from the database
    result = session.query(FunnyAnimal).filter_by(name="Grumpy Cat").one()
    assert result.name == "Grumpy Cat"
    assert result.mood == "Grumpy"
    assert result.quirkiness_level == 10.0
    assert result.favorite_food == "Pickles"


# Test case: Check that mood is required (not nullable)
def test_mood_is_required(session):
    animal = FunnyAnimal(
        name="Mysterious Cat",
        quirkiness_level=5.0,
        favorite_food="Mystery Meat"
    )

    # Expect an IntegrityError because mood is required
    with pytest.raises(IntegrityError):
        session.add(animal)
        session.commit()


# Test case: Verify quirkiness_level defaults to 1.0 if not specified
def test_default_quirkiness_level(session):
    animal = FunnyAnimal(
        name="Happy Dog",
        mood="Happy",
        favorite_food="Bones"
    )
    session.add(animal)
    session.commit()

    result = session.query(FunnyAnimal).filter_by(name="Happy Dog").one()
    assert result.quirkiness_level == 1.0


# Test case: Ensure that quirkiness_level accepts float values
def test_quirkiness_level_as_float(session):
    animal = FunnyAnimal(
        name="Funny Parrot",
        mood="Playful",
        quirkiness_level=7.5,
        favorite_food="Crackers"
    )
    session.add(animal)
    session.commit()

    result = session.query(FunnyAnimal).filter_by(name="Funny Parrot").one()
    assert isinstance(result.quirkiness_level, float)
    assert result.quirkiness_level == 7.5


# Test case: Ensure sighting_timestamp is set by default
def test_sighting_timestamp_default(session):
    animal = FunnyAnimal(
        name="Silly Rabbit",
        mood="Silly",
        quirkiness_level=8.5,
        favorite_food="Carrots"
    )
    session.add(animal)
    session.commit()

    result = session.query(FunnyAnimal).filter_by(name="Silly Rabbit").one()
    assert result.sighting_timestamp is not None
