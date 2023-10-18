from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    msisdn = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return f'Productname: {self.name}'


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    sum_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Order id: {self.id}'
