import json
from .models import *
from datetime import datetime

def user(input_json):
    
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

    list_of_urls_on_url = input_json.get('entities',{}).get('url',{}).get('urls',[])
    list_of_urls_on_description = input_json.get('entities',{}).get('description',{}).get('urls',[])
    print(list_of_urls_on_description)
    list_of_urls = list_of_urls_on_url + list_of_urls_on_description
    list_of_urls = [UserUrl(url=url.get('expanded_url'),user_id = user.user_id, id ='{}_{}'.format(url.get("expanded_url"),user.user_id)) for url in list_of_urls]
    [url.save() for url in list_of_urls]

    return user
