from pymongo import MongoClient
import json
from pykafka import KafkaClient

try:
   mongo_client = mongo_client = MongoClient('mongodb://root:example@localhost:27017/')
   mongo_db = mongo_client['streamingtwitter']
   mongo_collection = mongo_db['tweets_bolso_lula']
   mongo_collection_count = mongo_db['tweets_bolso_lula_count']
   print("Connected successfully!!!")
except:  
   print("Could not connect to MongoDB")

client = KafkaClient(hosts="localhost:9092")

# Set up a Kafka topic consumer
topic = client.topics[b'ktwitter']
consumer = topic.get_simple_consumer()

# Read messages from the topic and print them to the console
for message in consumer:
    if message is not None:
        value = message.value.decode()
        json_obj = json.loads(value)
        mongo_collection.insert_one(json_obj)
        #word count - to produce "world cloud" into report:
        arr = json_obj["tweet_text"].split(" ")
        word_count = {}
        for word in arr:
           if word not in word_count:
              word_count[word] = 1
           else:
              word_count[word] += 1
        word_list = [{'word': word, 'count': count} for word, count in word_count.items()]
        json_string = json.dumps(word_list)
        for i in word_list:
           mongo_collection_count.insert_one(i)
        
