from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# TODO: add tags model, add get_absolute_url, ADD COMMENTS

CAMPAIGN_THEME_CHOICES = (
    ('all', 'All'),
    ('education', 'Education'),
    ('electronics', 'Electronics'),
    ('entertainment', 'Entertainment'),
    ('sport', 'Sport'),
    ('IT', 'IT'),
)


class Campaign(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    theme = models.CharField(max_length=255, choices=CAMPAIGN_THEME_CHOICES, default='all')
    tags = models.CharField(max_length=255)
    video_URL = models.CharField(max_length=255)
    target_money = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('campaigns-detail', kwargs={'pk': self.pk})

    @property
    def get_video(self):
        url = str(self.video_URL)
        parts = url.split('watch?v=')
        try:
            return parts[0] + 'embed/' + parts[1] + '?rel=0'
        except Exception:
            return 'error'


def upload_gallery_image(instance, filename):  # change when the gallery is in the cloud
    return f"images/{instance.campaign.name}/gallery/{filename}"


class Bonus(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="bonuses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('campaigns-detail', kwargs={'pk': self.campaign.pk})


class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="images")

    def get_absolute_url(self):
        return reverse('campaigns-detail', kwargs={'pk': self.campaign.pk})


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='news_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return '/'


class UserBonus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE)
