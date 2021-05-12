from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# TODO: add tags model, add get_absolute_url


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    theme = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    video_URL = models.CharField(max_length=255)
    target_money = models.IntegerField()
    end_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def upload_gallery_image(instance, filename):  # change when the gallery is in the cloud
    return f"images/{instance.campaign.name}/gallery/{filename}"


class Bonus(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="bonuses")

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="images")


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
