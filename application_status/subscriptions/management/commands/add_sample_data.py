from django.core.management.base import BaseCommand
from subscriptions.models import Application, Category
import random

class Command(BaseCommand):
    help = 'Adds sample data to the Application and Category models'

    def handle(self, *args, **kwargs):
        # Define some sample categories and applications
        categories = ["Finance", "Productivity", "Education", "Health", "Entertainment"]
        app_names = [f"App {i}" for i in range(1, 11)]

        # Add categories
        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Category '{category_name}' created"))

        # Add applications with random categories
        for app_name in app_names:
            category = random.choice(Category.objects.all())
            application, created = Application.objects.get_or_create(name=app_name, category=category)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Application '{app_name}' created under category '{category.name}'"))

        self.stdout.write(self.style.SUCCESS("Sample data added successfully"))

