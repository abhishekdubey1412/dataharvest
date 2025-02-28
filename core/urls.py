from django.urls import path
from core.views.home import home_view
from core.views.domain import domain_data, staff_data

urlpatterns = [
    path('', home_view, name="home"),
    path("api/scraping-status/<int:id>", domain_data, name="scraping_status"),
    path("api/staff-data/<int:id>", staff_data, name="staff_data"),
]