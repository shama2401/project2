from django.db import models


class PC(models.Model):
    code = models.IntegerField()
    model = models.ForeignKey('Product', on_delete=models.CASCADE)
    speed = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    hd = models.IntegerField()
    cd = models.CharField(max_length=2222)
    price = models.IntegerField()

    def str(self):
        return f'{self.code} {self.model} {self.speed} {self.ram} {self.hd}'


class Product(models.Model):
    maker = models.CharField(max_length=2222)
    model = models.CharField(max_length=222)
    type = models.CharField(max_length=2222)

    def str(self):
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

    def str(self):
        return f'{self.code} {self.model} {self.speed} {self.ram} {self.hd}'


class Printer(models.Model):
    code = models.CharField(max_length=2222)
    model = models.ForeignKey('Product', on_delete=models.CASCADE)
    color = models.CharField(max_length=22)
    type = models.CharField(max_length=22)
    price = models.IntegerField()

    def str(self):
        return f'{self.code} {self.model} {self.color} {self.type} {self.price}'