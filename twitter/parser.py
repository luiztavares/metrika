import json
from .models import *
from datetime import datetime

def user_parse(input_json):
    
    user = User(
        created_at =  datetime.strptime(input_json['created_at'][:19] + input_json['created_at'][25:],'%c',),
        user_id = input_json['id'],
        name = input_json['name'],
        screen_name = input_json['screen_name'],
        location = input_json['location'],
        description = input_json['description'],
        followers_count = input_json['followers_count'],
        friends_count = input_json['friends_count'],
        listed_count = input_json['listed_count'],
        favourites_count = input_json['favourites_count'],
        statuses_count = input_json['statuses_count'],
        avatar = input_json['profile_image_url'],
    )
    user.save()

    return user

def user_url_parse(user_id,input_json):
    list_of_urls_on_url = input_json.get('url',{}).get('urls',[])
    list_of_urls_on_description = input_json.get('description',{}).get('urls',[])
    list_of_urls = list_of_urls_on_url + list_of_urls_on_description
    list_of_urls = [
        UserUrl(
            url=url.get('expanded_url'),
            user_id = user_id, 
            id ='{}_{}'.format(url.get("expanded_url"),user_id)
        ).save() for url in list_of_urls
    ]

def tweet_parse(input_json):
    tweet = Tweet(
        tweet_creation = datetime.strptime(input_json['created_at'][:19] + input_json['created_at'][25:],'%c',),
        tweet_id = input_json['id'],
        user_id = input_json['user']['id'],
        content = input_json['full_text'],
        retweet_count = input_json['retweet_count'],
        favorite_count = input_json['favorite_count'],
        retweet_id = input_json.get('retweeted_status',{}).get('id',None),
        lang = input_json['lang'],
    )
    if(tweet.retweet_id):
        tweet.content = f"RT @{input_json['retweeted_status']['user']['screen_name']}: {input_json['retweeted_status']['full_text']}"

    tweet.save()

    return tweet

def hashtag_parse(tweet_id,input_json):
    hashtag = [
        Hashtag(
            tweet_id = tweet_id,
            hashtag = hashtag['text'],
            id = f"{hashtag['text']}_{tweet_id}"
        ).save() for hashtag in input_json['hashtags']
    ]
    pass

def mention_parse(tweet_id,input_json):
    mention = [
        Mention(
            tweet_id = tweet_id,
            user_id = user['id'],
            id = f"{user['id']}_{tweet_id}"
        ).save() for user in input_json['user_mentions']
    ]


def tweet_url_parse(tweet_id,input_json):
    tweet_url = [
        TweetUrl(
            tweet_id = tweet_id,
            url = url['expanded_url'],
            id = f"{url['expanded_url']}_{tweet_id}"
        ).save() for url in input_json['urls']
    ]

def status_parse(input_json):
    user = user_parse(input_json['user'])
    user_url_parse(user.user_id,input_json['user']['entities'])
   
    tweet = tweet_parse(input_json)
    if(tweet.retweet_id):
        retweet = tweet_parse(input_json['retweeted_status'])
        user_retweet = user_parse(input_json['retweeted_status']['user'])
        
        user_url_parse(user_retweet.user_id,input_json['retweeted_status']['user']['entities'])

        mention_parse(retweet.tweet_id,input_json['retweeted_status']['entities'])
        tweet_url = tweet_url_parse(retweet.tweet_id,input_json['retweeted_status']['entities'])
        hashtag = hashtag_parse(retweet.tweet_id,input_json['retweeted_status']['entities'])
        
        mention_parse(tweet.tweet_id,input_json['retweeted_status']['entities'])
        tweet_url = tweet_url_parse(tweet.tweet_id,input_json['retweeted_status']['entities'])
        hashtag = hashtag_parse(tweet.tweet_id,input_json['retweeted_status']['entities'])
    
    else:

        mention_parse(tweet.tweet_id,input_json['entities'])
        tweet_url = tweet_url_parse(tweet.tweet_id,input_json['entities'])
        hashtag = hashtag_parse(tweet.tweet_id,input_json['entities'])

def follow_parse(source = None, target = None):
    if(source):
        user = user_parse(target)
        follow = Follow(
            source= source,
            target= user.user_id,
            id= f'{source}_{user.user_id}'
        )

    elif(target):
        user = user_parse(source)
        follow = Follow(
            source= user.user_id,
            target= target,
            id= f'{user.user_id}_{target}'
        )
    else:
        return
    
    follow.save()




