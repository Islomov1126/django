import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from home.models import Author


auth = Author.objects.create(name='test1', salutation='salutation')
