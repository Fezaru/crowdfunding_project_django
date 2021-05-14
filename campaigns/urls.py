from django.urls import path
from . import views
from .views import(
    NewsListView,
    CampaignsListView,
    CampaignsDetailView,
)

urlpatterns = [
    path('', NewsListView.as_view(), name='campaigns-home'),
    path('campaigns/', CampaignsListView.as_view(), name='campaigns-list'),
    path('campaigns/<int:pk>/', CampaignsDetailView.as_view(), name='campaigns-detail'),
]
