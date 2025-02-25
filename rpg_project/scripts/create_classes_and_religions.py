import os
import django

# Set up Django settings (update if your project name is different)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rpg_project.settings')
django.setup()

from rpg_app.models import PlayerClass, Religion

# Define new classes
classes_data = [
    {
        "name": "Warrior",
        "description": "A strong melee fighter with high health and strength.",
        "base_health": 30,
        "base_strength": 15,
        "base_dexterity": 8,
        "base_intelligence": 6,
        "base_charisma": 8,
        "base_ethics": 5
    },
    {
        "name": "Mage",
        "description": "A powerful spellcaster with high intelligence.",
        "base_health": 15,
        "base_strength": 5,
        "base_dexterity": 8,
        "base_intelligence": 20,
        "base_charisma": 7,
        "base_ethics": 10
    },
    {
        "name": "Rogue",
        "description": "A sneaky character with high dexterity and agility.",
        "base_health": 18,
        "base_strength": 10,
        "base_dexterity": 20,
        "base_intelligence": 8,
        "base_charisma": 10,
        "base_ethics": 6
    }
]

# Define new religions
religions_data = [
    {
        "name": "Order of Light",
        "description": "A holy order that grants blessings of protection and justice.",
        "bonus1": 3,
        "bonus1_description": "Increased health regeneration",
        "bonus2": 2,
        "bonus2_description": "Damage resistance against dark creatures",
        "bonus3": 1,
        "bonus3_description": "Increased charisma with townsfolk"
    },
    {
        "name": "Cult of the Flame",
        "description": "Followers of a fiery deity who draw power from fire.",
        "bonus1": 4,
        "bonus1_description": "Increased fire resistance",
        "bonus2": 3,
        "bonus2_description": "Bonus fire damage",
        "bonus3": 2,
        "bonus3_description": "Faster experience gain in desert regions"
    },
    {
        "name": "Circle of the Wild",
        "description": "A nature-oriented group with a focus on harmony with animals.",
        "bonus1": 3,
        "bonus1_description": "Improved interaction with animals",
        "bonus2": 2,
        "bonus2_description": "Bonus to hunting and survival skills",
        "bonus3": 1,
        "bonus3_description": "Slight health regeneration in forests"
    }
]

# Create classes in the database
for class_data in classes_data:
    PlayerClass.objects.get_or_create(**class_data)

# Create religions in the database
for religion_data in religions_data:
    Religion.objects.get_or_create(**religion_data)

print("Classes and religions created successfully!")
