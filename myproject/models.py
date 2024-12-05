from django.db import models

# Modèle pour les systèmes humains
class HumanSystem(models.Model):
    name = models.CharField(max_length=255)  # Nom du système humain (ex: "Cœur")
    description = models.TextField()  # Description du système humain

    def __str__(self):
        return self.name

# Modèle pour les systèmes océaniques
class OceanSystem(models.Model):
    name = models.CharField(max_length=255)  # Nom du système océanique (ex: "Courants marins")
    description = models.TextField()  # Description du système océanique

    def __str__(self):
        return self.name

# Modèle pour la comparaison entre systèmes humains et océaniques
class Comparison(models.Model):
    human_system = models.ForeignKey(HumanSystem, on_delete=models.CASCADE)  # Lien vers HumanSystem
    ocean_system = models.ForeignKey(OceanSystem, on_delete=models.CASCADE)  # Lien vers OceanSystem
    similarities = models.TextField()  # Description des similitudes
    consequences_of_dysfunction = models.TextField()  # Conséquences des dysfonctionnements

    def __str__(self):
        return f"{self.human_system.name} - {self.ocean_system.name}"