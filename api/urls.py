from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.url_data import UrlDataViewSet
from api.views.domain_data import DomainDataViewSet
from api.views.raw_data import RawDataViewSet
from api.views.scraped_data import ScrapedDataViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'url-data', UrlDataViewSet, basename='url-data')
router.register(r'domain-data', DomainDataViewSet, basename='domain-data')
router.register(r'raw-data', RawDataViewSet, basename='raw-data')
router.register(r'scraped-data', ScrapedDataViewSet, basename='scraped-data')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
