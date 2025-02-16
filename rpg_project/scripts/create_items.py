from rpg_app.models import Item

# Define new classes
items_data = [
    {
        "name": "Shortsword",
        "description": "A sword commonly used by militia.",
        "price": "50",
        "type": "Weapon",
        "health_bonus": 0,
        "strength_bonus": 0,
        "dexterity_bonus": 0,
        "intelligence_bonus": 0,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    },
    {
        "name": "Longsword",
        "description": "A sword commonly used by militia.",
        "price": "70",
        "type": "Weapon",
        "health_bonus": 0,
        "strength_bonus": 0,
        "dexterity_bonus": 0,
        "intelligence_bonus": 0,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    },
    {
        "name": "Mace",
        "description": "A short weapon used for blunt attacks",
        "price": "50",
        "type": "Weapon",
        "health_bonus": 0,
        "strength_bonus": 0,
        "dexterity_bonus": 0,
        "intelligence_bonus": 0,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    },
    {
        "name": "Wooden Bow",
        "description": "A standard bow a hunter might use.",
        "price": "50",
        "type": "Weapon",
        "health_bonus": 0,
        "strength_bonus": 0,
        "dexterity_bonus": 1,
        "intelligence_bonus": 0,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    },
    {
        "name": "Crossbow",
        "description": "Slow to reload, but massive damage",
        "price": "100",
        "type": "Weapon",
        "health_bonus": 0,
        "strength_bonus": 0,
        "dexterity_bonus": -2,
        "intelligence_bonus": 0,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    },
    {
        "name": "Staff",
        "description": "A metal walking stick.",
        "price": "25",
        "type": "Weapon",
        "health_bonus": 0,
        "strength_bonus": 0,
        "dexterity_bonus": 0,
        "intelligence_bonus": 1,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    },
    {
        "name": "Light Armor",
        "description": "Light armor made of mostly padded cloth",
        "price": "10",
        "type": "Armor",
        "health_bonus": 5,
        "strength_bonus": 0,
        "dexterity_bonus": 0,
        "intelligence_bonus": 0,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    },
    {
        "name": "Medium Armor",
        "description": "Medium armor made of leather and patched plates.",
        "price": "80",
        "type": "Armor",
        "health_bonus": 15,
        "strength_bonus": 0,
        "dexterity_bonus": 0,
        "intelligence_bonus": 0,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    },
    {
        "name": "Heavy Armor",
        "description": "The heaviest of metal armors.",
        "price": "200",
        "type": "Armor",
        "health_bonus": 30,
        "strength_bonus": 0,
        "dexterity_bonus": -3,
        "intelligence_bonus": 0,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    },
    {
        "name": "Health Potion",
        "description": "Standard health potion.",
        "price": "15",
        "type": "Potion",
        "health_bonus": 0,
        "strength_bonus": 0,
        "dexterity_bonus": 0,
        "intelligence_bonus": 0,
        "charisma_bonus": 0,
        "ethics_bonus": 0
    }
]

for item_data in items_data:
    Item.objects.get_or_create(**item_data)

print("Items created successfully!")