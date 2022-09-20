from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='publisher-logo', null=True)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    salutation = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=0)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class BookImages(models.Model):
    image = models.ImageField(upload_to='book-images')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Rating(models.Model):
    rating = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} {self.book} {self.rating}"


class Comment(models.Model):
    text = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.book} {self.user} {self.created}"


class Party(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.FloatField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.book} {self.price} {self.count} {self.created}"


class Sale(models.Model):
    percent = models.FloatField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    from_date = models.DateField(auto_now=True)
    to_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.user}"


class Basket(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.book} {self.user} {self.count}"


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    sale = models.ForeignKey(Sale, on_delete=models.RESTRICT, null=True)
    
    # status:
    # 1-ordered
    # 2-paid
    # 3-delevired
    # 4-received
    status = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.book} {self.user} {self.count} {self.status}"


class Payment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    
    # type:
    # 1-cash
    # 2-credit card
    # 3-transfer
    type = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.book} {self.user} {self.amount}"