from django.db import models


class AirCompany(models.Model):
    name = models.CharField(max_length=50, verbose_name='Aircompany name')

    def __str__(self):
        return self.name

class Rotating(models.Model):
    ROTATION = [
        ('Rotation-1', 'Rotation-1'),
        ('Rotation-2', 'Rotation-2'),
        ('Rotation-3', 'Rotation-3')
    ]
    rotation = models.CharField(choices=ROTATION, max_length=50, verbose_name='Rotation type')
    air_company = models.ForeignKey(AirCompany, on_delete=models.CASCADE, related_name='rotatings')

    def __str__(self):
        return f"{self.rotation}-{self.air_company}"

class Command(models.Model):
    COMMAND = [
        ('business', 'business'),
        ('economy', 'economy'),
        ('flight attendant', 'flight attendant'),
        ('pilot', 'pilot'),
        ('captain', 'captain'),
    ]
    command = models.CharField(choices=COMMAND, max_length=50, verbose_name='Command type')
    rotating = models.ForeignKey(Rotating, on_delete=models.CASCADE, related_name='commands')

    def __str__(self):
         return f"{self.command}-{self.rotating}"

class Food(models.Model):
    FOOD = [
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner')
    ]
    food = models.CharField(choices=FOOD, max_length=50, verbose_name='Food type')
    command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return f"{self.food}-{self.command}"

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='images')

class Flight(models.Model):
    air_company = models.ManyToManyField(AirCompany)
    rotating = models.ManyToManyField(Rotating)
    command = models.ManyToManyField(Command)
    food = models.ManyToManyField(Food)
    image = models.ManyToManyField(Image)

    def __str__(self):
        air_companies = ', '.join([str(ac) for ac in self.air_company.all()])
        return f"Flight {self.pk}: {air_companies}"
