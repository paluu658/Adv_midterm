import os
import sys
import django
import pandas as pd
import json
import requests

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AdvancedWebDevelopment.settings")
django.setup()

from flats.models import ResaleFlat


def load_data_from_csv(file_path):
    """
    Load data from a CSV file into the database, skipping duplicates
    and reporting the number of duplicates skipped.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # Load the CSV file
    data = pd.read_csv(file_path)

    duplicates_count = 0
    inserted_count = 0

    for _, row in data.iterrows():
        # Check if the record already exists
        if ResaleFlat.objects.filter(
            month=row["month"],
            town=row["town"],
            flat_type=row["flat_type"],
            block=row["block"],
            street_name=row["street_name"],
            resale_price=row["resale_price"],
        ).exists():
            duplicates_count += 1
            continue

        # Insert new record
        ResaleFlat.objects.create(
            month=row["month"],
            town=row["town"],
            flat_type=row["flat_type"],
            block=row["block"],
            street_name=row["street_name"],
            storey_range=row["storey_range"],
            floor_area_sqm=row["floor_area_sqm"],
            flat_model=row["flat_model"],
            lease_commence_date=row["lease_commence_date"],
            remaining_lease=row["remaining_lease"],
            resale_price=row["resale_price"],
        )
        inserted_count += 1

    print(
        f"Data loading completed. {inserted_count} records inserted, {duplicates_count} duplicates skipped."
    )


if __name__ == "__main__":
    # Path to the CSV file
    file_path = os.path.join(os.path.dirname(__file__), "../data/data.csv")

    # Load data from CSV into the database
    print("Loading data from CSV...")
    load_data_from_csv(file_path)
