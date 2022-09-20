from home.models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission, \
    IsAuthenticated, SAFE_METHODS, DjangoModelPermissions

from rest_framework.response import Response

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [DjangoModelPermissions]

class PublisherViewSet(viewsets.ModelViewSet):

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = PageNumberPagination


class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = PageNumberPagination


class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination



class BookImagesViewSet(viewsets.ModelViewSet):

    queryset = BookImages.objects.all()
    serializer_class = BookImagesSerializer
    pagination_class = PageNumberPagination


class RatingViewSet(viewsets.ModelViewSet):

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = PageNumberPagination


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination


class PartyViewSet(viewsets.ModelViewSet):

    queryset = Party.objects.all()
    serializer_class = PartySerializer
    pagination_class = PageNumberPagination


class SaleViewSet(viewsets.ModelViewSet):

    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    pagination_class = PageNumberPagination


class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = PageNumberPagination


class BasketViewSet(viewsets.ModelViewSet):

    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    pagination_class = PageNumberPagination


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = PageNumberPagination

from django.contrib.auth.models import Group
from rest_framework import viewsets
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['POST'])
def load_data_excell(request):
    try:
        import openpyxl
        import io

        file = request.FILES['file']
        wb = openpyxl.Workbook(filename=file)
        wsh = wb.active
        print(wsh['A1'].value)

        return Response('Ok', status=200)
    except Exception as exc:
        return Response(str(exc.with_traceback()), status=200)