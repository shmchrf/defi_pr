import pandas as pd
from myproject.models import HumanSystem, OceanSystem, Comparison  # Remplacez `api` par le nom de votre application

# Charger les données des fichiers CSV
human_systems = pd.read_csv('HumanSystems_Updated.csv')
ocean_systems = pd.read_csv('OceanSystems_Updated.csv')
comparisons = pd.read_csv('Comparisons_Updated.csv')

# Insérer les données des systèmes humains
for _, row in human_systems.iterrows():
    HumanSystem.objects.get_or_create(
        name=row['name'],
        description=row['description']
    )

# Insérer les données des systèmes océaniques
for _, row in ocean_systems.iterrows():
    OceanSystem.objects.get_or_create(
        name=row['name'],
        description=row['description']
    )

# Insérer les comparaisons
for _, row in comparisons.iterrows():
    human_system = HumanSystem.objects.get(name=row['human_system'])
    ocean_system = OceanSystem.objects.get(name=row['ocean_system'])
    Comparison.objects.get_or_create(
        human_system=human_system,
        ocean_system=ocean_system,
        similarities=row['similarities'],
        consequences_of_dysfunction=row['consequences_of_dysfunction']
    )
