from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class PlayerClass(models.Model):
    """
    Hero Class for making classes
    """
    # Class Info
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField()
    
    # Base attributes
    base_health = models.IntegerField(default=20)
    base_strength = models.IntegerField(default=10)
    base_dexterity = models.IntegerField(default=10)
    base_intelligence = models.IntegerField(default=10)
    base_charisma = models.IntegerField(default=10)
    base_ethics = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.name}, {self.description}"
    
class Religion(models.Model):
    """
    Template for religions and their passive benefits.
    """
    #Religion info
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField('Religion Template')

    # Passive attributes
    bonus1 = models.IntegerField(default=1)
    bonus1_description = models.TextField('Bonus description')
    bonus2 = models.IntegerField(default=1)
    bonus2_description = models.TextField('Bonus description')
    bonus3 = models.IntegerField(default=1)
    bonus3_description = models.TextField('Bonus description')

    def __str__(self):
        return f"{self.name}, {self.description}"
    
class Player(models.Model):
    """
    The Player, including class and religion
    """
    # Identifiers
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='player_profile')
    name = models.CharField(max_length=25, unique=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    # Starting class and religion
    player_class = models.ForeignKey(PlayerClass, on_delete=models.SET_NULL, null=True)
    player_religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True)

    # Levels
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    experience_to_next_level = models.IntegerField(default=100)

    # Currency
    currency = models.IntegerField(default=1000)

    # Attributes
    health = models.IntegerField(default=10)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    ethics = models.IntegerField(default=10)

    def initialize_stats(self):
        """
        Initialize stats based on hero class.
        """
        if self.player_class:
            self.health = self.player_class.base_health
            self.strength = self.player_class.base_strength
            self.dexterity = self.player_class.base_dexterity
            self.intelligence = self.player_class.base_intelligence
            self.charisma = self.player_class.base_charisma
            self.ethics = self.player_class.base_ethics
    
    def __str__(self):
        return f"{self.name}, (Level {self.level})"
    
class Building(models.Model):
    """
    Building template
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Quest(models.Model):
    """
    Quest template
    """
    # TODO: Fix player default error
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    gold_reward = models.IntegerField(default=10)
    exp_reward = models.IntegerField(default=10)
    is_completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class BattleLog(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    description = models.TextField()
    result = models.CharField(max_length=50)  # Win/Loss/Draw
    date = models.DateTimeField(auto_now_add=True)

class Enemy(models.Model):
    """
    Enemy template
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    health = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.name}"
    
class Item(models.Model):
    """
    Item attributes
    """
    ITEM_TYPES = [
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('potion', 'Potion'),
        ('misc', 'Miscellaneous')
    ]

    # Basic Fields
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    type = models.CharField(max_length=20, choices=ITEM_TYPES, default='misc')

    # Stat bonuses (optional)
    health_bonus = models.IntegerField(default=0)
    strength_bonus = models.IntegerField(default=0)
    dexterity_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)
    ethics_bonus = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class PlayerInventory(models.Model):
    """
    Tracks which item a user owns and how many.
    """
    user = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_inventory")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="inventory_item")
    quantity = models.PositiveIntegerField(default=0) # Number of item user owns.
    is_equipped = models.BooleanField(default=False)

    def __str__(self):
        """
        Prints string to display User and what items they have
        """
        # Example "john_doe - Apple (x3)"
        return f"{self.user} - {self.item.name} (x{self.quantity})"
 