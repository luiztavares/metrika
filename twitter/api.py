import tweepy
import json

class TwitterAPI:
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
        response = self.apis[0].statuses_lookup(ids)
        return response