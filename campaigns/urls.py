from django.urls import path
from . import views
from .views import(
    NewsListView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView,
    CampaignsListView,
    CampaignsDetailView,
    CampaignsCreateView,
    CampaignsUpdateView,
    CampaignsDeleteView,
    BonusesCreateView,
    BonusesUpdateView,
    BonusesDeleteView,
    BonusPurchaseView,
    ImagesCreateView,
    ImagesUpdateView,
    ImagesDeleteView,
)

urlpatterns = [
    path('', NewsListView.as_view(), name='campaigns-home'),
    path('campaigns/', CampaignsListView.as_view(), name='campaigns-list'),
    path('campaigns/<int:pk>/', CampaignsDetailView.as_view(), name='campaigns-detail'),
    path('campaigns/new/', CampaignsCreateView.as_view(), name='campaigns-create'),
    path('campaigns/<int:pk>/update/', CampaignsUpdateView.as_view(), name='campaigns-update'),
    path('campaigns/<int:pk>/delete/', CampaignsDeleteView.as_view(), name='campaigns-delete'),
    path('campaigns/<int:pk>/bonuses/new', BonusesCreateView.as_view(), name='bonuses-create'),
    path('bonuses/<int:pk>/update', BonusesUpdateView.as_view(), name='bonuses-update'),
    path('bonuses/<int:pk>/delete', BonusesDeleteView.as_view(), name='bonuses-delete'),
    path('campaigns/<int:pk1>/bonuses/<int:pk2>/purchase', BonusPurchaseView, name='bonuses-purchase'),
    path('campaigns/<int:pk>/images/new', ImagesCreateView.as_view(), name='images-create'),
    path('images/<int:pk>/update', ImagesUpdateView.as_view(), name='images-update'),
    path('images/<int:pk>/delete', ImagesDeleteView.as_view(), name='images-delete'),
    path('campaigns/<int:pk>/news/new', NewsCreateView.as_view(), name='news-create'),
    path('news/<int:pk>/update', NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', NewsDeleteView.as_view(), name='news-delete'),
]
