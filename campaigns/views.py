from django.shortcuts import render, get_object_or_404
from .models import News, Campaign
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)


class NewsListView(ListView):
    model = News
    template_name = 'campaigns/home.html'
    context_object_name = 'news'
    ordering = ['-date_posted']
    paginate_by = 5


class CampaignsListView(ListView):
    model = Campaign
    template_name = 'campaigns/campaigns_list.html'
    context_object_name = 'campaigns'
    ordering = ['-created_date']
    paginate_by = 5


class CampaignsDetailView(DetailView):
    model = Campaign
    template_name = 'campaigns/campaigns_detail.html'
    
