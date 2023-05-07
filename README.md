# Twitter Streaming Data Processing with Python, Kafka, and MongoDB

This repository contains Python scripts that enable the processing of real-time Twitter data using Kafka and MongoDB. The scripts are designed to fetch data from the Twitter API, filter the data based on specific criteria, and store the filtered data into a MongoDB database.

## Requirements

To use these scripts, you will need the following:

- Python 3.x
- `tweepy` package: This is a Python wrapper for the Twitter API.
- `pymongo` package: This is a Python driver for MongoDB.
- `kafka-python` package: This is a Python client for Apache Kafka.
- `json` package: This is a Python client for JSON.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/twitter-kafka-mongodb.git
   
Create a Twitter developer account and create a new app to get the required API keys and access tokens.

Create a MongoDB database and collection to store the Twitter data.

Create a Kafka topic to receive the Twitter data.

Update the config.py file with your Twitter API keys, access tokens, MongoDB connection details, and Kafka topic name.
