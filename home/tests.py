from django.test import TestCase, Client
from .models import Author, Publisher, Genre
from django.urls import reverse_lazy

# Create your tests here.
class PublisherTestCase(TestCase):
    def setUp(self) -> None:
        self.xamza = Publisher.objects.create(name="Xamza", city="Tashkent", email="xamza@publish.com")

    def test_publishers_count_and_create(self):
        publishers = Publisher.objects.all()
        self.assertEqual(len(publishers), 1)
        self.assertEqual(self.xamza, publishers[0])
    
    def test_update_publisher(self):
        self.xamza.name = "Xamza Hakimzoda Niyoziy"
        self.xamza.save()

        xamza = Publisher.objects.first()
        self.assertEqual(self.xamza, xamza)
    
    def test_delete(self):
        self.xamza.delete()

        publishers = Publisher.objects.all()
        self.assertEqual(len(publishers), 0)


class BookViewTest(TestCase):

    def setUp(self) -> None:
        self.cleint = Client()

    def test_list_of_books(self):
        response = self.cleint.get(reverse_lazy('index'))

        self.assertEqual(response.status_code, 200)
    
    def test_create_count_book(self):
        pub = Publisher.objects.create(name="Xamza", city="Tashkent", email="xamza@publish.com")
        auth = Author.objects.create(name="Alisher", salutation="Navoiy")
        genre = Genre.objects.create(name="Badiy")
        
        response = self.cleint.post(reverse_lazy('add-book'), {
            'name': "Xamsa",
            'description': 'Xamsa asari',
            'publisher': pub.id,
            'count': 10,
            "authors": [auth.id],
            'genres': [genre.id]
        })

        self.assertEqual(response.status_code, 302)

        response = self.cleint.get(reverse_lazy('index'))
        self.assertEqual(response.status_code, 200)

        assert "Xamsa" in str(response.content)