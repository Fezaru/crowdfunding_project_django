from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from campaigns.models import (
    Campaign,
)
from crowdfunding_project.api.serializers import (
    BonusSerializer,
    ImageSerializer,
    CampaignSerializer,
)


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()

    def list(self, request):
        serializer = CampaignSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        campaign = get_object_or_404(self.queryset, pk=pk)
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)
