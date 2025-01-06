import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvancedWebDevelopment.settings")
django.setup()

from flats.models import ResaleFlat


def remove_duplicates():
    """
    Identify and remove duplicate entries in the ResaleFlat table.
    """
    seen = set()
    duplicates = []

    for flat in ResaleFlat.objects.all():
        unique_identifier = (
            flat.month,
            flat.town,
            flat.flat_type,
            flat.block,
            flat.street_name,
            flat.resale_price,
        )
        if unique_identifier in seen:
            duplicates.append(flat.id)
        else:
            seen.add(unique_identifier)

    # Delete duplicates
    ResaleFlat.objects.filter(id__in=duplicates).delete()
    print(f"Removed {len(duplicates)} duplicate entries.")


if __name__ == "__main__":
    remove_duplicates()
