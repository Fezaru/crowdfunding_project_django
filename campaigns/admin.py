from django.contrib import admin
from .models import Campaign, Bonus, Image, News, UserBonus

admin.site.register(Campaign)
admin.site.register(Bonus)
admin.site.register(Image)
admin.site.register(News)
admin.site.register(UserBonus)
