from django.contrib import admin
from .models import Creature

@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    list_display  = ('name', 'element_type', 'threat_level', 'attack', 'defense')
    list_filter   = ('element_type',)
    search_fields = ('name',)