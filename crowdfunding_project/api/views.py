from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers
from rest_framework import permissions
from django.contrib.auth.models import User
from crowdfunding_project.api.permissions import ModifyIfOwnerOrRead
from campaigns.models import (
    Campaign,
    Bonus,
    News,
)
from crowdfunding_project.api.serializers import (
    BonusSerializer,
    CampaignSerializer,
    NewsSerializer,
)


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()
    permission_classes = [ModifyIfOwnerOrRead]

    def list(self, request):
        serializer = CampaignSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        campaign = get_object_or_404(self.queryset, pk=pk)
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BonusViewSet(viewsets.ModelViewSet):
    serializer_class = BonusSerializer
    queryset = Bonus.objects.all()
    permission_classes = [ModifyIfOwnerOrRead]

    def list(self, request):
        serializer = BonusSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        bonus = get_object_or_404(self.queryset, pk=pk)
        serializer = BonusSerializer(bonus)
        return Response(serializer.data)

    def perform_create(self, serializer):
        campaign = Campaign.objects.get(name=self.request.data['campaign_name'])
        if campaign in Campaign.objects.filter(owner=self.request.user):
            serializer.save(campaign=Campaign.objects.get(name=self.request.data['campaign_name']))
        else:
            raise serializers.ValidationError({"detail": "You are not the owner of this campaign"})


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = [ModifyIfOwnerOrRead]

    def list(self, request):
        serializer = NewsSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        news = get_object_or_404(self.queryset, pk=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def perform_create(self, serializer):
        campaign = Campaign.objects.get(name=self.request.data['campaign_name'])
        if campaign in Campaign.objects.filter(owner=self.request.user):
            serializer.save(campaign=Campaign.objects.get(name=self.request.data['campaign_name']))
        else:
            raise serializers.ValidationError({"detail": "You are not the owner of this campaign"})
