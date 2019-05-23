"""
Main script for botdelaradio.
"""

# external modules
import tweepy
import configparser
import os


def fetch_broadcasting_infos():
    """
    Fetch information about radio broadcasting.
    Output:
        -broadcasting_infos     str
    """

    return "this bot is still in development"


if __name__ == "__main__":

    # read config file
    botdelaradio_project_path = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read(os.path.join(botdelaradio_project_path, "config", "config.ini"))
    consumer_key = config.get("access", "consumer_key")
    consumer_secret = config.get("access", "consumer_secret")
    access_token = config.get("access", "access_token")
    access_token_secret = config.get("access", "access_token_secret")

    # twitter authentification
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    shows_infos_string = fetch_shows_infos()

    api.update_status(status=shows_infos_string)
