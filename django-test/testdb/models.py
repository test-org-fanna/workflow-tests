from django.db import models


class PetRock(models.Model):
    """Represents the idea of owning a pet rock—a fad from the 1970s. Created by ChatGPT"""
    # Rocks need names too!
    name = models.CharField(max_length=100, unique=True)

    # Rocks are born... or just found. Let's assume they have birth dates.
    birth_date = models.DateField()

    # Rocks don't do much, but they do have moods!
    MOOD_CHOICES = [
        ('HAPPY', 'Happy'),
        ('GRUMPY', 'Grumpy'),
        ('SLEEPY', 'Sleepy'),
        ('EXCITED', 'Excited'),
    ]
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES, default='HAPPY')

    # In Geology, rocks have classifications
    MOOD_CHOICES = [
        ('IGNEOUS', 'Igneous'),
        ('SEDIMENTARY', 'Sedimentary'),
        ('METAMORPHIC', 'Metamorphic'),
    ]
    classification = models.CharField(max_length=15, choices=MOOD_CHOICES, default='IGNEOUS')

    # Every pet rock deserves a custom resting spot
    resting_spot = models.CharField(max_length=255, default="A soft pillow")

    # Rocks can't move, but let's track how many times they've 'rolled'
    times_rolled = models.PositiveIntegerField(default=0)

    def roll(self):
        """Pretend that the rock rolls."""
        self.times_rolled += 1
        return f"{self.name} has rolled {self.times_rolled} times. Impressive!"

    def __str__(self):
        return f"{self.name} (Mood: {self.get_mood_display()}, Times Rolled: {self.times_rolled})"

    class Meta:
        verbose_name = "Pet Rock"
        verbose_name_plural = "Pet Rocks"
