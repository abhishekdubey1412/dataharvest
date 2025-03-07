from django.urls import path
from core.views import home_view
from core.groq_extractor import ExtractDataView

urlpatterns = [
    path('', home_view, name='home'),
    path('staff-ai-extract/', ExtractDataView.as_view(), name='staff-ai-extract')
]