from django.db import models


class AirCompany(models.Model):
    name = models.CharField(max_length=50, verbose_name='Aircompany name')

    def __str__(self):
        return self.name


class Command(models.Model):
    COMMAND = [
        ('business', 'business'),
        ('economy', 'economy'),
        ('captain', 'captain'),
        ('pilot', 'pilot'),
        ('flight attendant', 'flight attendant'),
    ]
    command = models.CharField(choices=COMMAND, max_length=50, verbose_name='Command type')
    air_company = models.ForeignKey(AirCompany, on_delete=models.CASCADE, related_name='commands')
    

    def __str__(self):
         return f"{self.air_company}-{self.command}"
    
class Rotating(models.Model):
    ROTATION = [
        ('Rotation-1', 'Rotation-1'),
        ('Rotation-2', 'Rotation-2'),
        ('Rotation-3', 'Rotation-3'),
        ('Days 1-10', 'Days 1-10'),
        ('Days 11-20', 'Days 11-20'),
        ('Days 21-30', 'Days 21-30')
    ]
    
    command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name='rotatings')
    rotation = models.CharField(choices=ROTATION ,max_length=50, verbose_name='Rotation type', blank=True)
    special = models.TextField(verbose_name='Спецпитание с номером указать здесь!!!' , blank=True)
    def __str__(self):
        return f"{self.command}-{self.rotation}-{self.special}"


class Food(models.Model):
    FOOD = [
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch')
    ]
    food = models.CharField(choices=FOOD, max_length=50, verbose_name='Food type')
    rotation = models.ForeignKey(Rotating, on_delete=models.CASCADE, related_name='foods')
    def __str__(self):
        return f"{self.food}-{self.rotation}"

class HotFood(models.Model):
    hotfood = models.CharField(max_length=10, verbose_name='Необходимо указать тип HB or HM', blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='hotfoods')
    
    def __str__(self) :
        return f"{self.food}-{self.hotfood}"
    

class Image(models.Model):
    images = models.ImageField(upload_to='images/')
    hotfood = models.ForeignKey(HotFood, on_delete=models.CASCADE, related_name='images', blank=True)

    def __str__(self) :
        return f"{self.hotfood}-{self.images}"

class Flight(models.Model):
    air_company = models.ManyToManyField(AirCompany)
    command = models.ManyToManyField(Command)
    rotating = models.ManyToManyField(Rotating)
    food = models.ManyToManyField(Food)
    hotfood = models.ManyToManyField(HotFood)
    image = models.ManyToManyField(Image)

    def __str__(self):
        air_companies = ', '.join([str(ac) for ac in self.air_company.all()])
        return f"Flight {self.pk}: {air_companies}"
