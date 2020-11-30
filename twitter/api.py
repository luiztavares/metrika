import tweepy
import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class TwitterAPI(metaclass=Singleton):
    def __init__(self):
        self.keys = [['2m2IZIw55y8XMTRLep2gx6van','kcF8ZCrA6yK4zZFVkGYSkEd7W5sopi5GFjJoQLg1n75WA22Vlc'],
                    ['3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys'],
                    ['IQKbtAYlXLripLGPWd0HUA','GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU'],
                    ['CjulERsDeqhhjSme66ECg','IQWdVyqFxghAtURHGeGiWAsmCAGmdW3WmbEx6Hck'],
                    ['3rJOl1ODzm9yZy63FACdg','5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8'],
                    ['3nVuSoBZnx6U4vzUxf5w','Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys'],
                    ['d0CTc4Zg9pufCnMkteDc7w','z4FMZhP87U5QEwycggDe5JN6TDDh7xEyhnAcEpdWk'],
                    ['SrVuVUogZ2spEwJzEB6UaYu4y','9FXUIFP0n7YRj1F1l6MFNws4iuYYWCvUjSh1kW5UUtt5srfeEE'],
                    ['CVbiuNGV6MeQCsku7SUZnejVb','AXzQ9ZSxu1JPWbQNXHj4Zn1uI32fMDviLDYyKM6RihwPjGz6i9'],
                    ['53aMoQiFaQfoUtxyJIkGdw','Twnh3SnDdtQZkJwJ3p8Tu5rPbL5Gt1I0dEMBBtQ6w'],
                    ['7Uifmz2gkHF8RcOcMtItTJRoF', 'YmcL95Yy15zvwAfGVaCrbGaUkcWo6wv0OT9RXCOxWfoHwuY1RT'],
                    ['dtPUzX4qL11DSsLBC6wvduH59', 'A4hcreygBSbDDtghi34JeGZAyTLq0PSUbRTKCJbreTLkdaBd8x'],
                    ]
                    
        self.apis = []
        for x in self.keys:
            try:
                auth = tweepy.AppAuthHandler(x[0], x[1]) 
                authenticated = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
                self.apis.append(authenticated)
            except:
                print(f'Failure on {x[0]}, does not work any more')

    @property
    def keysLen(self,):
        return len(self.keys)

    def splitList(self,alist, wanted_parts=1):
        length = len(alist)
        return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts) ]

    def statuses_lookup(self,ids):
        #implement max 100 ids per request
        response = self.apis[0].statuses_lookup(ids,tweet_mode="extended",)
        return response

    def user_timeline(self,screen_name):
        
        for x in tweepy.Cursor(self.apis[0].user_timeline, screen_name=screen_name,tweet_mode="extended",count=200).items():
            return [x]

    def get_status(self,tweet_id):
        #implement max 100 ids per request
        response = self.apis[0].get_status(tweet_id,tweet_mode="extended",)
        return response

    def get_user(self,user_id):
        #implement max 100 ids per request
        response = self.apis[0].get_user(
            user_id = user_id,
            tweet_mode="extended",
        )
        return response

    def get_friends(self,user_id):
        for x in tweepy.Cursor(self.apis[0].friends, user_id=user_id,tweet_mode="extended",count=100).items():
            yield x._json

    
    def get_followers(self,user_id):
        for x in tweepy.Cursor(self.apis[0].followers, user_id=user_id,tweet_mode="extended",count=100).items():
            yield x._json

    