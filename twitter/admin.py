from django.contrib import admin
from twitter.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Hashtag)
admin.site.register(UserUrl)
admin.site.register(TweetUrl)
admin.site.register(Mention)