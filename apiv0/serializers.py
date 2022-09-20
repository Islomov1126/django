from rest_framework import serializers
from home.models import *

class PublisherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookImages
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class PartySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Party
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sale
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Basket
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'

from django.contrib.auth.models import Group
class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class LoadDataExcel(serializers.BaseSerializer):
    file = serializers.FileField()