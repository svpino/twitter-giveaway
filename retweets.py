import pandas as pd
import glob
import tweepy
import time

API_KEY = "<API_KEY>"
API_KEY_SECRET = "<API_KEY_SECRET>"
ACCESS_TOKEN = "<ACCESS_TOKEN>"
ACCESS_TOKEN_SECRET = "<ACCESS_TOKEN_SECRET>"

USER = "<USER SCREEN NAME>"
STATUS = 0 #<ID OF THE GIVEAWAY TWEET>

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


def capture():
    """ This function will loop indefinitely while retrieving the last 100
    retweets of the supplied status. Each time the function runs, it creates
    a new CSV file and stores it in the current folder.
    """
    index = 199
    while True:
        users = api.retweeters(STATUS)
        dataframe = pd.DataFrame(users)
        dataframe.to_csv(f"retweeters{str(index).zfill(4)}.csv", index=False)

        # Let's sleep for a while to avoid hitting Twitter's API limit. We need
        # to make sure we don't sleep for two long and miss some of the retweets.
        time.sleep(5 * 60)
        index += 1


def merge():
    """ This function loads all the CSV files stored in the local folder and 
    combines them in a single CSV file after removing any duplicates.
    """

    retweets = []
    for filename in glob.glob("*.csv"):
        dataframe = pd.read_csv(filename)
        retweets.extend(dataframe["0"].tolist())

    dataframe = pd.DataFrame(list(set(retweets)))
    dataframe.to_csv("retweeters.csv", index=False)

capture()
# merge()