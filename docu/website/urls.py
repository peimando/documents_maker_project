from .apps import WebsiteConfig
from django.urls import path
from .views import (
    Home,
    AddOrdinario,
)

app_name = WebsiteConfig.name

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('ordinario/new', AddOrdinario.as_view(), name='add_ordinario'),
    # path('ordinario/<slug:slug>/edit')
    # path('generate_pdf/', report, name='report'),
    # path('home', Home.as_view(), name='home1')
]
