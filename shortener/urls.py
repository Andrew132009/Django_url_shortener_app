from django.urls import path
from .views import redirect_url


urlpatterns = [
    path('<str:short_url>', redirect_url, name='redirect_url')
]