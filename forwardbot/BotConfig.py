from os import environ
class Config(object):
    API_ID = int(environ.get("API_ID", '7767744')) 
    API_HASH = environ.get("API_HASH", '7e5504b4fcaa6ad4515b52a66c09ceb1')
    BOT_TOKEN = environ.get("BOT_TOKEN", "1948692090:AAFwNBZnXEnywIvSOyNJQQ6QbANPl5PDcQA")
    STRING_SESSION = environ.get("STRING", "1AZWarzsBu4bCBLjivPP55D0tlHFYWKErI6ws4aFHFGsMi7AcTTaQvCyofvPhmAw2pohOJCT9bjWMdyIFY-PTJZhPjKAK5nrJSZYVXGqAVNs4z5dc0PNp3pvIdCMHvnsDW2_NhzYcGp36EP2sQQm82NIM0OqLe3qDRXBjIxIcBk42PSxuQftyZBH_ez7f6cjqge-bGTeqy7m7fH7z2_aztLBDcNRVSLnsAbt1tD7hd4OZh75TynIslCwDgYdoVsNqSxGsXy3QxXFOEYgXbtv2g0l3uAF_MTR2TnOjU8zbkMj4dw5qPfYmAcYborWXY3EKifUXrY5G_kKCX1vRzTXbYvOIFZ-UpF8=")
    SUDO_USERS = environ.get("SUDO_USERS", "1770970698")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
