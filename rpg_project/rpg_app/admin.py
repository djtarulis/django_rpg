from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Player, PlayerInventory, Item, Religion, Quest, Enemy, Building, PlayerClass

# Inline class to display inventory within PlayerAdmin
class InventoryInline(admin.TabularInline):
    model = PlayerInventory
    extra = 0
    fields = ['item', 'quantity']
    readonly_fields = ['item']
    can_delete = False

# CustomPlayerAdmin: Grouped fields and display inventory
@admin.register(Player)
class CustomPlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'level', 'player_class', 'player_religion', 'display_inventory_link']
    search_fields = ['name', 'user__username']
    list_filter = ['name']

    # Group fields using fieldsets
    fieldsets = (
        (None, {'fields': ('name', 'user')}),
        ('Hero Details', {'fields': ('player_class', 'player_religion', 'level', 'experience')}),
        ('Currency & Resources', {'fields': ('currency',)}),
    )

    # Inline inventory display within the PlayerAdmin form
    inlines = [InventoryInline]

    # Method to display a clickable link to the player's full inventory
    def display_inventory_link(self, obj):
        url = reverse('admin:rpg_app_playerinventory_changelist') + f'?user__id__exact={obj.id}'
        return format_html('<a href="{}">View Full Inventory</a>', url)

    display_inventory_link.short_description = 'Inventory'

# InventoryAdmin: Manage player inventory directly
@admin.register(PlayerInventory)
class PlayerInventoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'quantity']
    search_fields = ['user']
    list_filter = ['item', 'user']
    fields = ['user', 'item', 'quantity']

# ItemAdmin: Manage game items
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description', 
        'price', 
        'type', 
        'health_bonus', 
        'strength_bonus', 
        'dexterity_bonus', 
        'intelligence_bonus',
        'charisma_bonus',
        'ethics_bonus',
        ]
    search_fields = ['name', 'type']
    fields = [  # Fields for creating items in admin
        'name',
        'description', 
        'price', 
        'type', 
        'health_bonus', 
        'strength_bonus', 
        'dexterity_bonus', 
        'intelligence_bonus',
        'charisma_bonus',
        'ethics_bonus',
        ]

# ReligionAdmin: Manage creation of religions
@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description', 
        'bonus1', 
        'bonus1_description', 
        'bonus2', 
        'bonus2_description', 
        'bonus3', 
        'bonus3_description'
        ]
    search_fields = ['name', 'description', 'bonus1', 'bonus2', 'bonus3']
    fields = [
        'name',
        'description', 
        'bonus1', 
        'bonus1_description', 
        'bonus2', 
        'bonus2_description', 
        'bonus3', 
        'bonus3_description'
    ]

# QuestAdmin: Manage quests and rewards
@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'difficulty', 'gold_reward', 'exp_reward']
    search_fields = ['name', 'difficult', 'gold_rewared', 'exp_reward']
    fields = ['name', 'description', 'difficulty', 'gold_reward', 'exp_reward']

# EnemyAdmin: Manage enemies and monsters
@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'health']
    search_fields = ['name', 'health']
    fields = ['name', 'health']

# BuildingAdmin: Manage buildings
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']
    fields = ['name', 'description']

# PlayerClassAdmin: Manage player classes
@admin.register(PlayerClass)
class PlayerClass(admin.ModelAdmin):
    list_display = [
        'name', 
        'description', 
        'base_health', 
        'base_strength', 
        'base_dexterity',
        'base_intelligence',
        'base_charisma',
        'base_ethics'
        ]
    search_fields = ['name']
    fields = [
        'name', 
        'description', 
        'base_health', 
        'base_strength', 
        'base_dexterity',
        'base_intelligence',
        'base_charisma',
        'base_ethics'
        ]



