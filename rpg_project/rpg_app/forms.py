from django import forms
from .models import Player, PlayerClass, Religion

class HeroCreationForm(forms.ModelForm):
    player_class = forms.ModelChoiceField(queryset=PlayerClass.objects.all(), required=True)
    religion = forms.ModelChoiceField(queryset=Religion.objects.all(), required=True)

    class Meta:
        model = Player
        fields = ['name', 'player_class', 'player_religion']