import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'rKgQvLS3WokrzuONphsztM1zA'
consumer_secret = 'dyjrNsGUbgutppZQq5KmqoxmY36qnFXGRNJgT4cEZH1HsDJLEN'
access_token = '46877872-ayb0RgZ47CVT8y8jGeQZnxsQrncf59h1w68x7WI90'
access_secret = 'bhENufVqvqVudGLGFsid8Df6H0ouPmIpraB8AKsg8vySG'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#Read last 10 twits of a page
#we would like to store the twits in out database  for each particular page
# we are to provide functionality
# Ultimetly, we will implement the streaming Twitter API, and save twits in out database
# as users log in to the system, we would keep track to the information he has seen,
# and display him the information he havent seen yet.
# an option to see "seen posts" will be provided
def read_neo_feed(screen_name):

    # steps not shown where you set up api
    # u = api.get_user(783214)
    # print (u.screen_name)

    status_list=[]
    for status in tweepy.Cursor(api.user_timeline,  screen_name=screen_name).items(10):
        status_list.append(status.text)

    return status_list


def read_python_user_stream():
    class MyListener(StreamListener):

        def on_data(self, data):
            try:
                print(data)
                with open('python.json', 'a') as f:
                    f.write(data)
                    return True
            except BaseException as e:
                print("Error on_data: %s" % str(e))
            return True

        def on_error(self, status):
            print(status)
            return True

    twitter_stream = Stream(auth, MyListener())
    # The data will be pushed to the on_data method for the user_id defined in the list below
    twitter_stream.filter(follow=['46877872'])