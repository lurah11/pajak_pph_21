from django.db import models

# Create your models here.
class Cat(models.Model): 
    category=models.CharField(max_length=10)
    group=models.CharField(max_length=5)

    def __str__(self): 
        return f"{self.category}--{self.group}"

class Tier(models.Model): 
    no=models.CharField(max_length=10)
    cat=models.CharField(max_length=2)
    from_value=models.FloatField()
    to_value=models.FloatField()
    rate=models.FloatField()

    def __str__(self): 
        return f"{self.cat}--rate:{self.rate*100}%"