from django.urls import path
from . import views


urlpatterns = [
    path('<slug:url>/', views.page_view, name='page_detail'),
    path('<slug:url>/<slug:child_url>', views.page_view, name='page_nested'),
]

