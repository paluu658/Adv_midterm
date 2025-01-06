import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvancedWebDevelopment.settings")
django.setup()

from flats.models import ResaleFlat


def delete_all_data():
    """
    Delete all data from the ResaleFlat model.
    """
    count = ResaleFlat.objects.count()
    ResaleFlat.objects.all().delete()
    print(f"Deleted {count} records from the database.")


if __name__ == "__main__":
    print("Starting data deletion...")
    delete_all_data()
