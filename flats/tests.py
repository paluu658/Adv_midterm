from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ResaleFlat


# Create your tests here.
class ResaleFlatAPITestCase(TestCase):
    def setUp(self):
        """
        Set up test data for the ResaleFlat model.
        """
        self.client = APIClient()

        # Create some sample data
        ResaleFlat.objects.create(
            month="2024-01",
            town="TOA PAYOH",
            flat_type="4 ROOM",
            block="123",
            street_name="TOA PAYOH NTH",
            storey_range="10 TO 12",
            floor_area_sqm=90.0,
            flat_model="Improved",
            lease_commence_date=1975,
            remaining_lease=50,
            resale_price=450000.0,
        )
        ResaleFlat.objects.create(
            month="2024-02",
            town="BEDOK",
            flat_type="5 ROOM",
            block="456",
            street_name="BEDOK SOUTH",
            storey_range="13 TO 15",
            floor_area_sqm=120.0,
            flat_model="Improved",
            lease_commence_date=1980,
            remaining_lease=40,
            resale_price=600000.0,
        )

    def test_get_all_flats(self):
        """
        Test retrieving all flats.
        """
        response = self.client.get("/api/v1/flats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filtered_flats_view(self):
        """
        Test filtering flats by town.
        """
        response = self.client.get("/api/v1/flats/filter/", {"town": "TOA PAYOH"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            "/api/v1/flats/filter/", {"town": "NON_EXISTENT_TOWN"}
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get("/api/v1/flats/filter/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_price_range_flats_view(self):
        """
        Test filtering flats by price range.
        """
        response = self.client.get(
            "/api/v1/flats/price-range/", {"min_price": "400000", "max_price": "500000"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            "/api/v1/flats/price-range/", {"min_price": "700000"}
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(
            "/api/v1/flats/price-range/", {"min_price": "INVALID"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_flats_grouped_by_type(self):
        """
        Test grouping flats by type.
        """
        response = self.client.get("/api/v1/flats/group-by-type/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_average_price_by_town(self):
        """
        Test retrieving average price by town.
        """
        response = self.client.get("/api/v1/flats/average-price/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_resale_flat(self):
        """
        Test creating a new resale flat.
        """
        new_flat = {
            "month": "2024-03",
            "town": "ANG MO KIO",
            "flat_type": "3 ROOM",
            "block": "789",
            "street_name": "ANG MO KIO AVE 1",
            "storey_range": "16 TO 18",
            "floor_area_sqm": 75.0,
            "flat_model": "Improved",
            "lease_commence_date": 1990,
            "remaining_lease": 35,
            "resale_price": 380000.0,
        }
        # First creation attempt
        response = self.client.post("/api/v1/flats/create/", new_flat, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Duplicate creation attempt
        response = self.client.post("/api/v1/flats/create/", new_flat, format="json")
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_create_resale_flat_invalid_data(self):
        """
        Test creating a flat with invalid data.
        """
        invalid_flat = {
            "month": "2024-03",
            "town": "",
            "flat_type": "3 ROOM",
            "block": "789",
            "street_name": "ANG MO KIO AVE 1",
            "storey_range": "16 TO 18",
            "floor_area_sqm": "INVALID",
            "flat_model": "Improved",
            "lease_commence_date": 1990,
            "remaining_lease": 35,
            "resale_price": 380000.0,
        }
        response = self.client.post(
            "/api/v1/flats/create/", invalid_flat, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_insert_data_successfully(self):
        """
        Test inserting a new resale flat successfully.
        """
        valid_flat = {
            "month": "2024-04",
            "town": "BISHAN",
            "flat_type": "4 ROOM",
            "block": "567",
            "street_name": "BISHAN STREET 22",
            "storey_range": "7 TO 9",
            "floor_area_sqm": 85.0,
            "flat_model": "Simplified",
            "lease_commence_date": 1995,
            "remaining_lease": 45,
            "resale_price": 420000.0,
        }

        # Send POST request to insert data
        response = self.client.post("/api/v1/flats/create/", valid_flat, format="json")

        # Assert the response status is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert the response contains the created data
        self.assertEqual(response.data["month"], valid_flat["month"])
        self.assertEqual(response.data["town"], valid_flat["town"])
        self.assertEqual(response.data["flat_type"], valid_flat["flat_type"])
        self.assertEqual(response.data["block"], valid_flat["block"])
        self.assertEqual(response.data["street_name"], valid_flat["street_name"])
        self.assertEqual(response.data["resale_price"], valid_flat["resale_price"])

        # Assert the database contains the new entry
        self.assertTrue(
            ResaleFlat.objects.filter(
                month=valid_flat["month"],
                town=valid_flat["town"],
                flat_type=valid_flat["flat_type"],
                block=valid_flat["block"],
                street_name=valid_flat["street_name"],
                resale_price=valid_flat["resale_price"],
            ).exists()
        )
