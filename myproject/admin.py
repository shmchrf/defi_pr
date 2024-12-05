# systems/admin.py

from django.contrib import admin
from .models import HumanSystem, OceanSystem, Comparison

# Enregistrer les modèles dans l'admin
admin.site.register(HumanSystem)
admin.site.register(OceanSystem)
admin.site.register(Comparison)
