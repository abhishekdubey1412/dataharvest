from django.urls import path
from core.views.home import home_view
from core.views.domain import domain_data, staff_data
from core.views.llm_data_clear import ExtractDataView

urlpatterns = [
    path('', home_view, name="home"),
    path("api/scraping-status/<int:id>", domain_data, name="scraping_status"),
    path("api/staff-data/<int:id>", staff_data, name="staff_data"),
    path('api/extract-data/', ExtractDataView.as_view(), name='extract-data'),
]