# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID =  6709394 # integer value, dont use ""
    API_HASH = "c97848ba434f04ce62ed2a3251787d71"
    TOKEN = "2048163647:AAFz-fe105piOprjei3WuEyo5uDWkOimltY"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 923790989  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Insane_akashm"
    SUPPORT_CHAT = "greatopfr"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001792860190
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001792860190
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://mkmilaprqakqlr:ed21f0a2bc0b81ad68631bcefbda4f67e299a90a221c299e8fecc86723e904ec@ec2-54-163-158-194.compute-1.amazonaws.com:5432/d7lb0mn7c1ht48"  # needed for any database modules
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "IvBUwPZbvBWPoZFU7knd5FraR_bkNHK2FbyWZjyceqD1bRlYz0dWKIWZI7QpEy7X"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgUAAxkBAAEDI4ZhdG-7ejeylBxYkYLQ6Gt6X3L3PgACFAADywzcOnRv2m1YdEkWIQQ"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "B1N1XTHY0D8FBPO3"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "J85OW1U31RPT"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "hmmm"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "df46af7df8c4227634754104d0797213a380c95c5a889eb991e8e29c6d9bfbf5ac4a0557a72b17c1dc0aae0004c70e716bcb53730409c6346e1db807d88088ff"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
