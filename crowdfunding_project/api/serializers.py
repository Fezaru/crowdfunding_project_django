from rest_framework import serializers
from django.contrib.auth.models import User
from campaigns.models import (
    Campaign,
    Bonus,
    Image,
    News,
)


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = ['name', 'price', 'description']


class NewsSerializer(serializers.ModelSerializer):
    # добавить поле компании???
    class Meta:
        model = News
        fields = ['title', 'content', 'date_posted', 'image']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


# class UserSerializer(serializers.ModelSerializer):
#     profile_image = serializers.SerializerMethodField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'profile_image']
#
#     def get_profile_image(self, user):
#         return user.profile.image


class CampaignSerializer(serializers.ModelSerializer):
    bonuses = BonusSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    owner_username = serializers.SerializerMethodField()

    class Meta:
        model = Campaign
        fields = ['name', 'description', 'theme', 'tags', 'video_URL', 'target_money', 'created_date', 'end_date',
                  'bonuses', 'images', 'owner_username']

    def get_owner_username(self, campaign):
        return campaign.owner.username
