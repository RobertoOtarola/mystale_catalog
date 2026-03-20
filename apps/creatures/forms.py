from django import forms
from .models import Creature


class CreatureForm(forms.ModelForm):

    class Meta:
        model  = Creature
        fields = ['name', 'element_type', 'threat_level', 'description',
                  'hp', 'attack', 'defense', 'speed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'threat_level': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return name

    def clean(self):
        cleaned = super().clean()
        for stat in ('hp', 'attack', 'defense', 'speed'):
            val = cleaned.get(stat)
            if val is not None and not (1 <= val <= 255):
                self.add_error(stat, f"{stat.upper()} debe estar entre 1 y 255.")
        return cleaned
