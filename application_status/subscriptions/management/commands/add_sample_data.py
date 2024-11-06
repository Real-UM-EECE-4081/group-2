from django.core.management.base import BaseCommand
from subscriptions.models import Application, Category
import random

class Command(BaseCommand):
    help = 'Adds sample data to the Application and Category models'

    def handle(self, *args, **kwargs):
        categories = ["Finance", "Productivity", "Education", "Health", "Entertainment"] # Random application categories
        app_names = [f"App {i}" for i in range(1, 11)]

        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)

        for app_name in app_names:
            category = random.choice(Category.objects.all())
            application, created = Application.objects.get_or_create(name=app_name, category=category)

