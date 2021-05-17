from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import News, Campaign, Bonus, Image, UserBonus
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


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.campaign = Campaign.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'content', 'image']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.campaign.owner:
            return True
        return False


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.campaign.owner:
            return True
        return False


class CampaignsListView(ListView):
    model = Campaign
    template_name = 'campaigns/campaigns_list.html'
    context_object_name = 'campaigns'
    ordering = ['-created_date']
    paginate_by = 5


class CampaignsDetailView(DetailView):
    model = Campaign
    template_name = 'campaigns/campaigns_detail.html'


class CampaignsCreateView(LoginRequiredMixin, CreateView):
    model = Campaign
    fields = ['name', 'description', 'theme', 'tags', 'video_URL', 'target_money', 'end_date']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CampaignsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Campaign
    fields = ['name', 'description', 'theme', 'tags', 'video_URL', 'target_money', 'end_date']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        campaign = self.get_object()
        if self.request.user == campaign.owner:
            return True
        return False


class CampaignsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Campaign
    success_url = '/campaigns'

    def test_func(self):
        campaign = self.get_object()
        if self.request.user == campaign.owner:
            return True
        return False


class BonusesCreateView(LoginRequiredMixin, CreateView):
    model = Bonus
    fields = ['name', 'price', 'description']

    def form_valid(self, form):
        form.instance.campaign = Campaign.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class BonusesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bonus
    fields = ['name', 'price', 'description']

    # def get_queryset(self):
    #     return Bonus.objects.filter(id=self.kwargs['pk'])

    # def form_valid(self, form):
    #     form.instance.campaign = Campaign.objects.get(id=self.kwargs['pk'])
    #     return super().form_valid(form)

    def test_func(self):
        bonus = self.get_object()
        if self.request.user == bonus.campaign.owner:
            return True
        return False


class BonusesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bonus

    def get_success_url(self):
        return '/campaigns/' + str(self.object.campaign.id)

    def test_func(self):
        bonus = self.get_object()
        if self.request.user == bonus.campaign.owner:
            return True
        return False


@login_required()
def BonusPurchaseView(request, pk1, pk2):
    users_bonus = UserBonus(user=request.user, bonus=Bonus.objects.get(id=pk2))
    users_bonus.save()
    messages.success(request, 'Purchase completed')
    return redirect('campaigns-detail', pk1)


class ImagesCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['image']

    def form_valid(self, form):
        form.instance.campaign = Campaign.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class ImagesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    fields = ['image']

    def test_func(self):
        img = self.get_object()
        if self.request.user == img.campaign.owner:
            return True
        return False


class ImagesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image

    def get_success_url(self):
        return '/campaigns/' + str(self.object.campaign.id)

    def test_func(self):
        img = self.get_object()
        if self.request.user == img.campaign.owner:
            return True
        return False
