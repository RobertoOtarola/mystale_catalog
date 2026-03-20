# Mystale Catalog

Bootcamp Desarrollo de Aplicaciones Fullstack Python Trainee | Challenge Módulo 7 (ABP).

Sistema web para catalogar criaturas energéticas, construido con Django y SQLite.

## Stack

- Python 3
- Django 6.0.3
- SQLite
- Templates nativos de Django

## Puesta en marcha

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Aplicación disponible en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Funcionalidades

- Listado de criaturas con estilo tipo "pokedex".
- Filtro por categoría elemental.
- Vista de detalle por criatura.
- Formulario de creación con validaciones.
- Mensajes de éxito y error en operaciones de formulario.

## Estructura principal

- `config/`: configuración global del proyecto Django.
- `apps/creatures/`: app principal del catálogo.
- `apps/creatures/templates/creatures/`: plantillas HTML.
- `static/css/`: estilos de la interfaz.

## Migraciones de la app `creatures`

- `0001_initial`: campos base (`name`, `element_type`, `threat_level`, `description`).
- `0002_add_stats_fields`: estadísticas (`hp`, `attack`, `defense`, `speed`).

Ejemplo de rollback:

```bash
python manage.py migrate creatures 0001
```

## Notas técnicas

- Se usa arquitectura modular con `apps/creatures` para favorecer mantenibilidad.
- Las vistas están implementadas con CBVs (`ListView`, `DetailView`, `CreateView`).
- Las validaciones de formulario viven en `CreatureForm` (`clean_name` y `clean`).
