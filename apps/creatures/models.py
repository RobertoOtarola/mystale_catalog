from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Creature(models.Model):

    ELEMENT_CHOICES = [
        ('fuego',   'Fuego'),
        ('agua',    'Agua'),
        ('tierra',  'Tierra'),
        ('rayo',    'Rayo'),
        ('sombra',  'Sombra'),
        ('cristal', 'Cristal'),
        ('viento',  'Viento'),
        ('hielo',   'Hielo'),
    ]

    name         = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    element_type = models.CharField(max_length=20, choices=ELEMENT_CHOICES, verbose_name='Categoría elemental')
    threat_level = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Nivel de amenaza'
    )
    description  = models.TextField(verbose_name='Descripción de campo')
    created_at   = models.DateTimeField(auto_now_add=True)

    # Estadísticas de combate — agregadas en 0002
    hp      = models.PositiveSmallIntegerField(default=50, verbose_name='HP',       validators=[MinValueValidator(1), MaxValueValidator(255)])
    attack  = models.PositiveSmallIntegerField(default=50, verbose_name='Ataque',   validators=[MinValueValidator(1), MaxValueValidator(255)])
    defense = models.PositiveSmallIntegerField(default=50, verbose_name='Defensa',  validators=[MinValueValidator(1), MaxValueValidator(255)])
    speed   = models.PositiveSmallIntegerField(default=50, verbose_name='Velocidad',validators=[MinValueValidator(1), MaxValueValidator(255)])

    class Meta:
        ordering = ['name']
        verbose_name = 'Criatura'
        verbose_name_plural = 'Criaturas'

    def __str__(self):
        return f"{self.name} [{self.get_element_type_display()}]"
