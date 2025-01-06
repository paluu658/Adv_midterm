from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Avg
from .models import ResaleFlat
from .serializers import ResaleFlatSerializer
from django.db.utils import IntegrityError


# Create your views here.
# API Views
class ResaleFlatListView(APIView):
    def get(self, request):
        try:
            flats = ResaleFlat.objects.all()
            serializer = ResaleFlatSerializer(flats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FilteredFlatsView(APIView):
    def get(self, request):
        try:
            town = request.query_params.get("town", None)
            if not town:
                return Response(
                    {"error": "Town query parameter is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            flats = ResaleFlat.objects.filter(town__icontains=town)
            if not flats.exists():
                return Response(
                    {"message": f"No flats found for town: {town}"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = ResaleFlatSerializer(flats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PriceRangeFlatsView(APIView):
    def get(self, request):
        try:
            min_price = request.query_params.get("min_price", None)
            max_price = request.query_params.get("max_price", None)

            flats = ResaleFlat.objects.all()
            if min_price:
                try:
                    min_price = float(min_price)
                    flats = flats.filter(resale_price__gte=min_price)
                except ValueError:
                    return Response(
                        {"error": "min_price must be a valid number."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            if max_price:
                try:
                    max_price = float(max_price)
                    flats = flats.filter(resale_price__lte=max_price)
                except ValueError:
                    return Response(
                        {"error": "max_price must be a valid number."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            if not flats.exists():
                return Response(
                    {"message": "No flats found in the given price range."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = ResaleFlatSerializer(flats, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FlatsGroupedByTypeView(APIView):
    def get(self, request):
        try:
            grouped_data = ResaleFlat.objects.values("flat_type").annotate(
                count=Count("flat_type")
            )
            if not grouped_data:
                return Response(
                    {"message": "No flats found to group by type."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return Response(grouped_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AveragePriceByTownView(APIView):
    def get(self, request):
        try:
            average_price = ResaleFlat.objects.values("town").annotate(
                average_price=Avg("resale_price")
            )
            if not average_price:
                return Response(
                    {
                        "message": "No data available to calculate average price by town."
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
            return Response(average_price, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ResaleFlatCreateView(APIView):
    def post(self, request):
        try:
            serializer = ResaleFlatSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # Handle unique_together validation errors
            if "non_field_errors" in serializer.errors:
                if any(
                    "unique" in str(error)
                    for error in serializer.errors["non_field_errors"]
                ):
                    return Response(
                        {"error": "Duplicate entry detected. Record already exists."},
                        status=status.HTTP_409_CONFLICT,
                    )
            # Handle other validation errors
            return Response(
                {"error": "Validation error", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": "Internal server error", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# HTML Views
def home_view(request):
    return render(request, "flats/home.html")


def flats_list_view(request):
    return render(request, "flats/list.html")


def flats_filter_view(request):
    return render(request, "flats/filter.html")


def flats_price_range_view(request):
    return render(request, "flats/price_range.html")


def flats_group_by_type_view(request):
    return render(request, "flats/group_by_type.html")


def flats_average_price_view(request):
    return render(request, "flats/average_price.html")


def flats_create_view(request):
    return render(request, "flats/create.html")
