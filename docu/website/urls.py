from .apps import WebsiteConfig
from django.urls import path
from .views import (
    Home,
    ListOrdinarios,
    AddOrdinario,
    EditOrdinario,
    DetailOrdinario,
    DownloadDocument
)

app_name = WebsiteConfig.name

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('ordinario/list', ListOrdinarios.as_view(), name='list_ordinarios'),
    path('ordinario/add', AddOrdinario.as_view(), name='add_ordinario'),
    path('ordinario/<slug:slug>/edit', EditOrdinario.as_view(), name='edit_ordinario'),
    path('ordinario/<slug:slug>/detail', DetailOrdinario.as_view(), name='detail_ordinario'),
    path('ordinario/download', DownloadDocument.as_view(), name='download_document'),

]
