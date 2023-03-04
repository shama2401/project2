from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel,TreeForeignKey

class Rubric(MPTTModel):
    name = models.CharField(max_length=222)
    parent = TreeForeignKey('self',on_delete=models.CASCADE, null=True, blank=True,related_name='children')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rubric', kwargs={'pk': self.pk})

    class MPTTMeta:
        order_insertion_by = ['name']



class PC(models.Model):
    code = models.IntegerField()
    model = models.ForeignKey('Product', on_delete=models.CASCADE)
    speed = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    hd = models.IntegerField()
    cd = models.CharField(max_length=2222)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/%y/%m/%d')

    def __str__(self):
        return f'{self.code} {self.model} {self.speed} {self.ram} {self.hd}'

class Product(models.Model):
    maker = models.CharField(max_length=2222)
    model = models.CharField(max_length=222)
    type = models.CharField(max_length=2222)
    
    def __str__(self):
        return f'{self.maker} {self.model} {self.type} '

class Laptop(models.Model):
    code = models.IntegerField()
    model = models.ForeignKey('Product', on_delete=models.CASCADE)
    speed = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    hd = models.IntegerField()
    cd = models.CharField(max_length=2222)
    price = models.IntegerField()
    screen = models.SmallIntegerField()

    def __str__(self):
        return f'{self.code} {self.model} {self.speed} {self.ram} {self.hd}'

class Printer(models.Model):
    code = models.CharField(max_length=2222)
    model = models.ForeignKey('Product', on_delete=models.CASCADE)
    color = models.CharField(max_length=22)
    type = models.CharField(max_length=22)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.code} {self.model} {self.color} {self.type} {self.price}'