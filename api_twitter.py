import config
import tweepy
import time
client = tweepy.Client(bearer_token=config.BEARER_TOKEN,
                       api_key=config.API_KEY,
                       api_secret=config.API_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET
                       )

auth = tweepy.OAuth1UserHandler(config.API_KEY,
                                config.API_SECRET,
                                config.ACCESS_TOKEN,
                                config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

search_terms = ["bolsonaro"]

class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print("connected!")
    def on_tweet(self, tweet):
        if tweet.referenced_tweets==None:
            print("original tweet> ",tweet.text)
            time.sleep(0.2)

stream = MyStream(bearer_token=config.BEARER_TOKEN)

#delete previous rules!
rules = stream.get_rules()

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])





for i in rules.data:
    print(i.id)
    stream.delete_rules(ids=i.id)

#searching last tweets (100)
#query = "lisboa"
#response = client.search_recent_tweets(query,max_results=100,tweet_fields=["created_at","lang"])
#for i in response.data:
#    print(i.id,i.lang)