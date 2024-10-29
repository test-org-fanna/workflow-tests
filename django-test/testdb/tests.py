from django.test import TestCase
from .models import PetRock
from datetime import date


class PetRockModelTests(TestCase):

    def setUp(self):
        """Set up initial data for tests."""
        # Create a sample PetRock
        self.rock = PetRock.objects.create(
            name="Rocky",
            birth_date=date(2023, 1, 1),
            mood="HAPPY",
            resting_spot="On a soft pillow"
        )

    def test_create_pet_rock(self):
        """Test the creation of a PetRock."""
        rocky = PetRock.objects.get(name="Rocky")
        self.assertEqual(rocky.name, "Rockyfdgdf")
        self.assertEqual(rocky.mood, "HAPPY")
        self.assertEqual(rocky.resting_spot, "On a soft pillow")
        self.assertEqual(rocky.times_rolled, 0)  # By default, it should be 0

    def test_roll_method(self):
        """Test the roll method."""
        self.rock.roll()  # Roll the rock once
        self.assertEqual(self.rock.times_rolled, 1)

        # Roll it again
        self.rock.roll()
        self.assertEqual(self.rock.times_rolled, 2)

    def test_get_mood_display(self):
        """Test the get_mood_display method."""
        # Verify that get_mood_display returns the human-readable mood
        self.assertEqual(self.rock.get_mood_display(), "Happy")

        # Change mood and test
        self.rock.mood = "GRUMPY"
        self.rock.save()
        self.assertEqual(self.rock.get_mood_display(), "Grumpy")

    def test_update_pet_rock(self):
        """Test updating a PetRock."""
        self.rock.mood = "SLEEPY"
        self.rock.save()

        updated_rock = PetRock.objects.get(name="Rocky")
        self.assertEqual(updated_rock.mood, "SLEEPY")
        self.assertEqual(updated_rock.get_mood_display(), "Sleepy")

    def test_delete_pet_rock(self):
        """Test deleting a PetRock."""
        self.rock.delete()
        with self.assertRaises(PetRock.DoesNotExist):
            PetRock.objects.get(name="Rocky")
