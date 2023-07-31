from .apps import WebsiteConfig
from django.urls import path
from .views import (
    index,
    report
    # Home
)

app_name = WebsiteConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('generate_pdf/', report, name='report'),
    # path('home', Home.as_view(), name='home1')
]
