from django.urls import path
from .views import (
    ResaleFlatListView,
    FilteredFlatsView,
    PriceRangeFlatsView,
    FlatsGroupedByTypeView,
    AveragePriceByTownView,
    ResaleFlatCreateView,  # API Views
    home_view,  # HTML View for home
    flats_create_view,  # HTML View
    flats_list_view,  # HTML View for listing
    flats_filter_view,  # HTML View for filtering
    flats_price_range_view,  # HTML View for price range
    flats_group_by_type_view,  # HTML View for grouping
    flats_average_price_view,  # HTML View for average price
)

urlpatterns = [
    # API Views
    path("api/v1/flats/", ResaleFlatListView.as_view(), name="flat-list"),
    path("api/v1/flats/filter/", FilteredFlatsView.as_view(), name="filtered-flats"),
    path(
        "api/v1/flats/price-range/",
        PriceRangeFlatsView.as_view(),
        name="price-range-flats",
    ),
    path(
        "api/v1/flats/group-by-type/",
        FlatsGroupedByTypeView.as_view(),
        name="group-by-type",
    ),
    path(
        "api/v1/flats/average-price/",
        AveragePriceByTownView.as_view(),
        name="average-price-by-town",
    ),
    path("api/v1/flats/create/", ResaleFlatCreateView.as_view(), name="create-flat"),
    # HTML Views
    path("", home_view, name="home"),
    path("flats/", flats_list_view, name="flat-list-view"),
    path("flats/create/", flats_create_view, name="create-flat"),
    path("flats/filter/", flats_filter_view, name="filtered-flats-view"),
    path("flats/price-range/", flats_price_range_view, name="price-range-flats-view"),
    path("flats/group-by-type/", flats_group_by_type_view, name="group-by-type-view"),
    path("flats/average-price/", flats_average_price_view, name="average-price-view"),
]
