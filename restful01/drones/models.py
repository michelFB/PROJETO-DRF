from django.db import models

# Utilizando conceitos de PK e FK mantendo relacionamento entre classes
# esses relacionamentos ajudam o ORM a identificar quando realiza o migrate
class DroneCategory(models.Model):
    name = models.CharField(max_length=250, unique = True)
    class Meta:
        ordering = ("name",)
    def __str__(self):
        return self.name
# //-------------------------------------------------------------
class Drone(models.Model):
    name = models.CharField(max_length=250, unique=True)
    drone_category = models.ForeignKey(
        DroneCategory, related_name="drones", on_delete=models.CASCADE
    )
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("name",)
    def __str__(self):
        return self.name
# //-------------------------------------------------------------
class Pilot(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )
    name = models.CharField(max_length=150, blank=False, default="", unique=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    races_count = models.IntegerField()
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("name",)
    def __str__(self):
        return self.name
# //-------------------------------------------------------------
class Competition(models.Model):
    pilot = models.ForeignKey(
        Pilot, related_name="competitions", on_delete=models.CASCADE
    )
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()
    class Meta:
        # Order by distance in descending order
        ordering = ("-distance_in_feet",)


def validate_even(value):
    if value % 2 != 0:
        raise models.ValidationError("Este campo deve ser um número par .")

class Person(models.Model):
    name = models.CharField(max_length=150, blank=False, default="", unique=True)
    old = models.IntegerField(validators=[validate_even])
    class Meta:
        ordering = ("name",)
    def __str__(self):
        return self.name
