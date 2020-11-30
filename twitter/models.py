from django.db import models

class Hashtag(models.Model):
    hashtag = models.TextField()
    tweet_id = models.BigIntegerField()
    id = models.TextField(primary_key=True)

    def __str__(self):
        return self.hashtag

class UserUrl(models.Model):
    url = models.URLField()
    user_id = models.BigIntegerField()
    id = models.TextField(primary_key=True)

class TweetUrl(models.Model):
    url = models.URLField()
    tweet_id = models.BigIntegerField()
    id = models.TextField(primary_key=True)

class User(models.Model):
    created_at = models.DateTimeField()
    user_id = models.BigIntegerField(primary_key=True)
    name = models.TextField(null=True,blank=True)
    screen_name = models.TextField()
    location = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    followers_count = models.BigIntegerField()
    friends_count = models.BigIntegerField()
    listed_count = models.BigIntegerField()
    favourites_count = models.BigIntegerField()
    statuses_count = models.BigIntegerField()
    avatar = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.screen_name

class Tweet(models.Model):
    tweet_creation = models.DateTimeField()
    tweet_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    content = models.TextField(null =True,blank=True)
    retweet_count = models.BigIntegerField()
    favorite_count = models.BigIntegerField()
    retweet_id = models.BigIntegerField(null=True,blank=True)
    lang = models.CharField(max_length=10)

    def __str__(self):
        return self.content

class Mention(models.Model):
    tweet_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    id = models.TextField(primary_key=True)


class TwitterList(models.Model):
    slug = models.TextField()
    name = models.TextField()
    created_at = models.DateTimeField()
    uri = models.URLField()
    subscriber_count = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True)
    full_name = models.TextField()
    description = models.TextField()
    user_id = models.BigIntegerField()

class Follow(models.Model):
    source = models.BigIntegerField()
    target = models.BigIntegerField()
    id = models.TextField(primary_key=True)